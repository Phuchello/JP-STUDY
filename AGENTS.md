# JP-STUDY checkpoint instructions

The owner authorizes organizing, committing and pushing meaningful completed and validated checkpoints to `https://github.com/Phuchello/JP-STUDY`, branch `main`. This authorization persists; do not ask again for routine checkpoint sync.

Before each checkpoint:
1. Inspect remote state and preserve existing history. Never force-push. Integrate concurrent changes safely.
2. Keep real learner records, schedules, exam credentials, identifying profile details, account entitlements, API keys and tokens local. Publish blank templates or explicitly synthetic examples. Link third-party books/exam PDFs/audio; do not redistribute downloaded copies.
3. Keep stable question IDs, keys, explanations, sources, pattern mappings and embedded offline assets consistent. Run checks appropriate to changed behavior. Independent AI QA is not native-speaker review or learner calibration.
4. Update `PROJECT_STATUS.md`, `FILE_INDEX.md`, QA and `MANIFEST.json`. Use only DRAFT / QA_PENDING / VERIFIED with explicit scope. Historical scripts are DRAFT, not a supported release pipeline. Do not claim the 300–500 expansion or N3/N2 banks exist while absent.
5. Make a descriptive commit, push `origin main`, fetch and compare local/remote SHA; verify important files remotely. Report commit SHA and GitHub URL. If push fails, retain changes and give the exact error; do not claim sync success.

Batch milestones. Do not commit each generated item, private exports, test fixtures, caches, previews, dependency directories, repeated binary artifacts or giant archives. Do not overwrite source originals outside this checkout. `scripts/update_manifest.py` regenerates the file index and manifest; then run `scripts/validate_release.py` and affected tests before commit.
