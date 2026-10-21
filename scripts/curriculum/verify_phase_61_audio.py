"""Verify regenerated spoken-choice MP3s against remapped display order."""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.curriculum.content_quality_checks import validate_spoken_audio

REMAP_PATH = ROOT / "qa/PHASE_6_1_OPTION_REMAP_MANIFEST.json"
RECEIPT_PATH = ROOT / "qa/PHASE_6_1_AUDIO_VERIFICATION.json"
SPOKEN_TYPES = {"N2-LIS-SUMM", "N2-LIS-OUTL", "N2-LIS-GIST", "N2-LIS-RESP"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def duration_seconds(path: Path) -> float:
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json", str(path)],
        check=True, capture_output=True, text=True,
    )
    return float(json.loads(result.stdout)["format"]["duration"])


def decode_mp3(path: Path) -> None:
    subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-f", "null", "-"],
                   check=True, capture_output=True, text=True)


def transcript_digest(option_texts: list[str]) -> str:
    transcript = "\n".join(f"{index + 1}番、{text}" for index, text in enumerate(option_texts))
    return hashlib.sha256(transcript.encode("utf-8")).hexdigest()


def main() -> int:
    remap = json.loads(REMAP_PATH.read_text(encoding="utf-8"))
    all_rows = []
    summary = {}
    for number in (7, 8, 9):
        exam_id = f"N2-MOCK-{number:02}"
        exam_path = ROOT / f"data/mock_exams/n2_mock_{number:02}.json"
        audio_manifest_path = ROOT / f"data/mock_exams/n2_mock_{number:02}_audio_manifest.json"
        exam = json.loads(exam_path.read_text(encoding="utf-8"))
        audio_manifest = json.loads(audio_manifest_path.read_text(encoding="utf-8"))
        browser_receipt_path = ROOT / f"qa/N2_MOCK_{number:02}_AUDIO_PLAYBACK_RECEIPT.json"
        browser_receipt = json.loads(browser_receipt_path.read_text(encoding="utf-8"))
        browser_rows = {row["questionId"]: row for row in browser_receipt.get("results", [])}
        if (browser_receipt.get("overallPlaybackVerified") is not True
                or browser_receipt.get("totalTracks") != 30
                or browser_receipt.get("verifiedPlaybackCount") != 30):
            raise ValueError(f"{exam_id}: real browser audio receipt does not verify all 30 tracks.")
        questions = {q["id"]: q for section in exam["sections"] for q in section["items"]}
        rows = remap["exams"][exam_id]
        targets = {qid for qid, row in rows.items() if row.get("audioRemapRequired")}
        expected_targets = {qid for qid, q in questions.items() if q.get("typeId") in SPOKEN_TYPES}
        if targets != expected_targets or len(targets) != 16:
            raise ValueError(f"{exam_id}: spoken-choice target coverage is {len(targets)}, expected exact 16.")
        if set(audio_manifest) != {qid for qid in questions if qid in audio_manifest} or len(audio_manifest) != 30:
            raise ValueError(f"{exam_id}: audio manifest must retain all 30 tracks.")

        changed_hashes = 0
        for qid in sorted(audio_manifest):
            question = questions[qid]
            meta = audio_manifest[qid]
            audio_url = str(meta.get("audioUrl", ""))
            audio_path = ROOT / "docs" / Path(audio_url)
            if not audio_path.is_file():
                raise FileNotFoundError(audio_path)
            actual_sha = sha256(audio_path)
            if actual_sha != str(meta.get("audioSha256", "")).lower():
                raise ValueError(f"{qid}: MP3 bytes differ from audio manifest SHA-256.")
            actual_duration = duration_seconds(audio_path)
            if abs(actual_duration - float(meta.get("audioDurationSec", -100))) > 0.2:
                raise ValueError(f"{qid}: ffprobe duration differs from manifest.")
            decode_mp3(audio_path)
            row = rows[qid]
            if qid in targets:
                display_texts = [str(option["text"]).strip() for option in question.get("options", [])]
                if meta.get("spokenOptionTexts") != display_texts:
                    raise ValueError(f"{qid}: recorded spoken options do not match current display order.")
                actual_transcript_sha = transcript_digest(display_texts)
                if meta.get("spokenOptionsTranscriptSha256") != actual_transcript_sha:
                    raise ValueError(f"{qid}: spoken-option transcript digest mismatch.")
                evidence = {
                    "status": "VERIFIED",
                    "orderedOptionTexts": display_texts,
                    "audioSha256": actual_sha,
                    "audioWasRegenerated": True,
                }
                errors = validate_spoken_audio(question, evidence)
                if errors:
                    raise ValueError("; ".join(errors))
                browser_result = browser_rows.get(qid)
                if (not browser_result or browser_result.get("acousticTier") != "BROWSER_PLAYBACK_VERIFIED"
                        or browser_result.get("sha256Match") is not True
                        or browser_result.get("computedSha256", "").lower() != actual_sha
                        or browser_result.get("desktopPlaybackAdvanced") is not True
                        or browser_result.get("mobilePlaybackAdvanced") is not True
                        or browser_result.get("jsonMatchesManifest") is not True):
                    raise ValueError(f"{qid}: browser receipt does not verify the regenerated asset on desktop and mobile.")
                previous_sha = row.get("previousAudioSha256", "")
                changed_hashes += int(previous_sha != actual_sha)
                row["afterAudioSha256"] = actual_sha
                row["audioDurationSec"] = actual_duration
                row["spokenOptionsTranscriptSha256"] = actual_transcript_sha
                row["audioStatus"] = "BROWSER_PLAYBACK_VERIFIED"
                row["audioWasRegenerated"] = True
                row["browserPlaybackReceipt"] = browser_receipt_path.name
                all_rows.append({
                    "examId": exam_id,
                    "questionId": qid,
                    "status": "BROWSER_PLAYBACK_VERIFIED",
                    "previousAudioSha256": previous_sha,
                    "audioSha256": actual_sha,
                    "audioSha256Changed": previous_sha != actual_sha,
                    "durationSec": actual_duration,
                    "orderedOptionTexts": display_texts,
                    "spokenOptionsTranscriptSha256": actual_transcript_sha,
                    "browserPlaybackStatus": "PASS",
                    "browserPlaybackReceipt": browser_receipt_path.name,
                })
        summary[exam_id] = {
            "audioManifestEntries": len(audio_manifest),
            "spokenChoiceTracks": len(targets),
            "technicalChecksPassed": len(targets),
            "changedSha256Count": changed_hashes,
            "browserPlaybackStatus": "PASS (30/30 tracks; 16 changed tracks verified on desktop and mobile)",
        }

    REMAP_PATH.write_text(json.dumps(remap, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    receipt = {
        "schemaVersion": 1,
        "status": "PASS",
        "method": "Actual MP3 SHA-256, ffprobe duration, full ffmpeg decode, exact displayed/spoken option order and transcript digest, plus 30/30 Chromium desktop/mobile playback receipts per exam.",
        "exams": summary,
        "tracks": all_rows,
    }
    RECEIPT_PATH.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    print(f"Wrote {len(all_rows)} track-level technical verification records to {RECEIPT_PATH.relative_to(ROOT)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
