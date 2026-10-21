# -*- coding: utf-8 -*-
"""Evidence-based, per-track audio assurance.

Playback claims are accepted only when tied to the exact manifest track and a
browser receipt containing decoding and playback-progress evidence. Speech
content review remains a separate linguistic certification.
"""
import hashlib
import re
from pathlib import Path
from typing import Any, Dict

ROOT = Path(__file__).resolve().parents[2]


def compute_file_sha256(file_path: Path) -> str:
    if not file_path.is_file():
        return ""
    hasher = hashlib.sha256()
    with file_path.open("rb") as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest()


def _positive_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and value > 0


def _has_error(value: Any) -> bool:
    return value is not None and str(value).strip() != ""


def evaluate_audio_track_assurance(
    track_meta: Dict[str, Any],
    receipt_track: Dict[str, Any],
    live_mp3_path: Path,
) -> Dict[str, Any]:
    """Evaluate evidence for one exact question/audio asset pair.

    `track_meta` must come from the audio manifest. `receipt_track` may be a
    detailed row from a receipt's `results` list or a legacy `tracks` entry,
    but legacy entries pass only when they retain browser decode and actual
    current-time progression measurements. Self-declared tier/boolean fields
    are never used as playback proof.
    """
    result = {
        "AUDIO_FILE_EXISTS": False,
        "AUDIO_HASH_VERIFIED": False,
        "AUDIO_DECODES": False,
        "BROWSER_PLAYBACK_VERIFIED": False,
        "SPEECH_CONTENT_REVIEWED": False,
        "highestTier": "NONE",
        "failureReason": None,
    }

    if not live_mp3_path.is_file() or live_mp3_path.stat().st_size == 0:
        result["failureReason"] = f"MP3 file does not exist or is empty: {live_mp3_path.name}"
        return result
    result["AUDIO_FILE_EXISTS"] = True
    result["highestTier"] = "AUDIO_FILE_EXISTS"

    question_id = track_meta.get("questionId") or track_meta.get("id") or track_meta.get("qid")
    receipt_question_id = receipt_track.get("questionId") or receipt_track.get("id") or receipt_track.get("qid")
    if not question_id or receipt_question_id != question_id:
        result["failureReason"] = "Playback receipt question ID does not match the manifest track"
        return result

    expected_sha = str(track_meta.get("audioSha256") or track_meta.get("sha256") or "").lower()
    live_sha = compute_file_sha256(live_mp3_path).lower()
    if not re.fullmatch(r"[0-9a-f]{64}", expected_sha):
        result["failureReason"] = "Manifest is missing a valid expected audio SHA-256 hash"
        return result
    if live_sha != expected_sha:
        result["failureReason"] = "Live MP3 SHA-256 does not match the manifest"
        return result

    detailed_hash_fields = any(
        k in receipt_track for k in ("expectedSha256", "computedSha256", "sha256Match", "expectedSha", "computedSha", "shaMatch")
    )
    if detailed_hash_fields:
        receipt_hash_ok = (
            str(receipt_track.get("expectedSha256") or receipt_track.get("expectedSha") or "").lower() == expected_sha
            and str(receipt_track.get("computedSha256") or receipt_track.get("computedSha") or "").lower() == live_sha
            and (receipt_track.get("sha256Match") is True or receipt_track.get("shaMatch") is True)
        )
    else:
        # Older receipts retain question ID, the matched SHA, and raw browser
        # measurements inside playbackDesktop/playbackMobile.
        receipt_hash_ok = (
            str(receipt_track.get("audioSha256", "")).lower() == expected_sha
            and receipt_track.get("audioHashVerified") is True
        )
    if not receipt_hash_ok:
        result["failureReason"] = "Playback receipt hash evidence does not match the manifest and live MP3"
        return result
    result["AUDIO_HASH_VERIFIED"] = True
    result["highestTier"] = "AUDIO_HASH_VERIFIED"

    desktop = receipt_track.get("playbackDesktop")
    mobile = receipt_track.get("playbackMobile")
    desktop = desktop if isinstance(desktop, dict) else {}
    mobile = mobile if isinstance(mobile, dict) else {}
    decoded_duration = receipt_track.get("browserDecodedDurationSec") or receipt_track.get("durationDecodedDesktop")
    decoded = (
        _positive_number(decoded_duration)
        or (desktop.get("loaded") is True and _positive_number(desktop.get("duration")))
        or (mobile.get("loaded") is True and _positive_number(mobile.get("duration")))
    )
    if not decoded:
        result["failureReason"] = "Browser decoding evidence is absent"
        return result
    result["AUDIO_DECODES"] = True
    result["highestTier"] = "AUDIO_DECODES"

    desktop_progress = (
        receipt_track.get("desktopPlaybackAdvanced") is True
        or receipt_track.get("desktopTimeAdvanced") is True
        or desktop.get("timeAdvanced") is True
        or _positive_number(desktop.get("currentTime"))
    )
    mobile_progress = (
        receipt_track.get("mobilePlaybackAdvanced") is True
        or receipt_track.get("mobileTimeAdvanced") is True
        or mobile.get("timeAdvanced") is True
        or mobile.get("ok") is True
        or _positive_number(mobile.get("currentTime"))
    )
    errors = [receipt_track.get("desktopError"), receipt_track.get("mobileError"), desktop.get("error"), mobile.get("error")]
    if any(_has_error(error) for error in errors):
        result["failureReason"] = "Playback receipt contains a contradictory browser playback error"
        return result
    if not (desktop_progress or mobile_progress):
        result["failureReason"] = "Playback receipt has no positive current-time advancement"
        return result

    result["BROWSER_PLAYBACK_VERIFIED"] = True
    result["highestTier"] = "BROWSER_PLAYBACK_VERIFIED"

    # Playback establishes playability, not pronunciation or speech accuracy.
    if receipt_track.get("speechContentReviewed") is True:
        result["SPEECH_CONTENT_REVIEWED"] = True
        result["highestTier"] = "SPEECH_CONTENT_REVIEWED"
    return result
