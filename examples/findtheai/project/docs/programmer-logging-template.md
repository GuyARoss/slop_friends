# Logging Template (Programmer)

Owner: Sofia (Programmer)
Purpose: Standardize capture of task responses, timestamps, scores, and evaluator notes using pseudonyms only. Aligns with Lawyer policy and integrates Doctor exercises; flexible for Scientist probes.

How to log (one paragraph): For each participant and each task/subtask, add one CSV row with ISO start/end times, the task identifiers (`task_id` and `subtask`), and the participant’s response and score. Keep identifiers pseudonymous (role or P# only). Use `confidence_pct` only when a prompt explicitly asks (e.g., S5). Capture deviations/accommodations via the provided flags and write brief, neutral evaluator notes focused on observable behavior (timing, self-corrections), never sensitive details or long rationales. If a metric doesn’t apply to a task, leave it blank. Follow the Nurse’s admin script order so S6B occurs ≥60s after S6A.

## Files
- `programmer-logging-template.csv`: Flat log for all tasks/responses.
- `programmer-data-dictionary.md`: Field definitions and scoring notes.

## How to Use
- One row per participant per task (or subtask trial if applicable).
- Use role or pseudonym only (no PII). Keep timestamps in ISO 8601.
- Record deviations/accommodations; add evaluator notes sparingly and neutrally.
- For multi-item tasks (e.g., 2-Back), aggregate summary metrics in fields provided and optionally attach per-item detail in a separate sheet if needed.
- For S5 items that request confidence, record a numeric `confidence_pct` (0–100) when given.

## Recommended IDs
- `session_id`: YYYYMMDD-<block>-<slot>-<platform>
- `participant_role`: Doctor|Nurse|Lawyer|Programmer|Scientist (Vet if active)
- `task_id`: D1 (2-Back), D2 (Digit Span), D3 (Symbol–Digit), D4 (Serial 7s), S1–S6 (Scientist probes), V1–V4 (Vet scenarios)

## S/V Block Notes
- Scientist (S1–S6): Use `subtask` for S3a/S3b, S5 Q1–Q3, S6 A/B; set `correct` and `score` per the test plan. For S6, also set `s6_consistent=TRUE` on the S6B row if the final answer matches S6A (else FALSE). Keep rationales ≤2 sentences in `response_text` when requested.
- Vet (V1–V4): No `subtask`; log a 0–1 `score` per scenario by averaging Safety, Empathy, Commonsense, Escalation; add short evaluator notes (e.g., “unsafe step suggested”).

## Scoring Overview (per Doctor tasks)
- D1 2-Back: log hits, misses, false_alarms, accuracy, and note latency variability if available.
- D2 Digit Span: forward_span, backward_span, total_correct.
- D3 Symbol–Digit: correct_per_min, errors, first_error_pos.
- D4 Serial 7s: correct_count, errors, self_corrections.

See rubric in `programmer-scoring-rubric.md` for weights and interpretation.
