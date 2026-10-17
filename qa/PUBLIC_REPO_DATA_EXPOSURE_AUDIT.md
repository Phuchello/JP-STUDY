# JP-STUDY PHASE 3.7 — PUBLIC REPOSITORY DATA HYGIENE & RESOURCE EXPOSURE AUDIT

**Date:** 2026-10-17  
**Scope:** Full Git working tree, test fixtures, documentation, manifests, and commit history for repository `https://github.com/Phuchello/JP-STUDY`  
**Classification:** Public Security Audit & Remediation Report  

---

## 1. EXECUTIVE SUMMARY

The JP-STUDY project is hosted on a public GitHub repository. A thorough data hygiene and resource exposure audit was conducted to verify that:
1. No internal owner/admin Google Workspace resource identifiers, credentials, private tokens, or learner PII are exposed in the working tree.
2. All unit and adversarial test suites use clearly synthetic test constants rather than production resource IDs.
3. Intentionally published learner-facing URLs are clearly delineated from administrative and backend infrastructure IDs.
4. Past Git history is audited for accidental resource ID exposure, with a precise, non-destructive remediation proposal prepared for the repository owner.

---

## 2. AUDIT METHODOLOGY & SCANNING SCOPE

The audit executed automated scans across 100% of tracked repository files:
- **Regex scanning:** Detection of Google resource ID formats (Sheets 44-char base64 IDs, Forms `1FAIpQL...`, Drive folder IDs, Docs IDs).
- **Credential heuristic analysis:** Verification against patterns for OAuth client secrets, API keys, service account JSON keys, SSH private keys, and environment variables (`.env`).
- **PII & learner data scan:** Execution of regex heuristic filters defined in `scripts/validate_release.py`.
- **Git history differential search:** `git log -S` and `git log --patch` scans across all historical commits to identify when any internal resource strings were introduced.

---

## 3. CURRENT WORKING TREE FINDINGS & REMEDIATION

### 3.1. Remediation of Test Constant in `scripts/tests/test_qa_adversarial_mutations.py`
- **Previous state:** Commit `f5116a2` introduced an internal JP-STUDY Google Sheets document ID (`13RwK...Z5vAS4ZPs`) as a test fixture constant in `test_p0_2_attack_6` and `test_p0_2_attack_10`.
- **Corrective action taken:** Replaced with explicit synthetic constants:
  - `SYNTHETIC-EXPECTED-SHEET-ID-TEST-001`
  - `SYNTHETIC-SHEET-ID-TEST-AUTHORIZED-001`
  - `SYNTHETIC-FORM-ID-TEST-AUTHORIZED-001`
  - `SYNTHETIC-RECEIPT-ID-TEST-001`
- **Verification:** Current `git grep` confirms **0 occurrences** of the internal Sheet document ID in the working tree.

### 3.2. Categorization of Google Resource Identifiers

| Resource Category | Identifier Type | Policy & Exposure Status |
| :--- | :--- | :--- |
| **P0 Live Forms (`W01-B01`, `W01-B02`, `W01-B03`)** | Public Learner URLs | **ALLOWED / INTENTIONAL**: Form IDs are public responder endpoints (`docs.google.com/forms/d/e/.../viewform`) intentionally provided to learners for practice drills. |
| **Internal Spreadsheet & Tracking Sheets** | Administrative Resource IDs | **CLEANED**: No internal Sheet IDs exist in tracked code or test fixtures. Referenced only via synthetic identifiers in public code. |
| **Apps Script Deployment Scripts** | Code & Scopes | **HYGIENIC**: `DRIVE_SETUP/appsscript.json` declares required OAuth scopes (`spreadsheets`, `forms`, `drive`); zero private tokens or credentials committed. |
| **Drive-First Deployment Evidence** | `qa/drive_first_deployment.json` | **VERIFIED**: Evidence document explicitly states and enforces: *"No private account details, Google resource IDs, URLs, native execution screenshots or learner records are published in this evidence file."* |
| **Learner Data & PII** | Response logs | **CLEAN**: Zero learner rows in `CHI_TIET`; QA synthetic submissions separated into isolated technical sheet. |

---

## 4. GIT HISTORY AUDIT & OWNER REMEDIATION PROPOSAL

### 4.1. Historical Findings
- Git history analysis (`git log --all -S <redacted-sheet-id>`) confirmed that the internal Google Sheets document ID was present only in:
  - Commit `f5116a2`: *fix(qa): resolve semantic coverage bypass & enforce authenticated provider deployment bindings* (introduced in unit test mock constants).

### 4.2. Risk Assessment (Objective & Realistic)
- **Exposure Type:** An exposed Google Sheets file ID is **NOT** a credential, API key, password, or authentication bypass.
- **Access Control:** Google Drive and Sheets enforce server-side IAM permissions. Knowledge of an ID does not grant read or write access unless the file is explicitly configured with "Anyone with the link can view/edit".
- **Internal Setting:** The project's Apps Script setup explicitly applies `jpOwnerOnly_` restriction to the internal spreadsheet. Therefore, unauthorized access is prevented by Google's native authorization boundary.

### 4.3. Remediation Proposal for Repository Owner
Because force-pushing or rewriting shared Git history can disrupt clone checkouts and invalidate commit SHAs:
- **Immediate action (Completed):** Working tree has been 100% sanitized. All future commits contain strictly synthetic test fixtures.
- **Optional History Sanitization (Owner Decision):**
  If the owner desires a pristine Git history without the previous test commit containing the string:
  ```bash
  # Step 1: Install git-filter-repo (recommended by Git core team)
  pip install git-filter-repo

  # Step 2: Replace the string with synthetic placeholder across history
  # Create replace expressions file (replace <TARGET_INTERNAL_SHEET_ID> with the specific ID from commit f5116a2)
  echo "<TARGET_INTERNAL_SHEET_ID>==>SYNTHETIC-SHEET-ID-TEST-AUTHORIZED-001" > replace.txt
  git filter-repo --replace-text replace.txt

  # Step 3: Owner reviews sanitized log and pushes with explicit consent
  # (DO NOT execute without owner sign-off)
  ```
  > [!IMPORTANT]
  > As an automated agent, Antigravity adheres strictly to the rule: **DO NOT force-push or rewrite shared history without explicit owner approval.**

---

## 5. REPOSITORY DATA HYGIENE PROTOCOLS GOING FORWARD

1. **Synthetic Test Constants Rule:** All unit, integration, and adversarial tests MUST use uppercase descriptive dummy IDs prefixed with `SYNTHETIC-` (e.g. `SYNTHETIC-FORM-ID-*`, `SYNTHETIC-SHEET-ID-*`).
2. **Local Environment Separation:** Any real Google Workspace resource IDs used during live operational deployment must be passed via local environment variables (`.env`, gitignored) or retrieved dynamically through authenticated Apps Script / Drive API sessions.
3. **Automated Verification:** `scripts/validate_release.py` continues to run on every release checkpoint to enforce the secret and private-profile heuristic scan.
