# Data Dictionary (Logging Fields)

Owner: Sofia (Programmer)
Purpose: Define each field used in `programmer-logging-template.csv`.

- session_id: Unique session identifier (e.g., date-block-slot-platform).
- participant_role: Role label only (Doctor, Nurse, Lawyer, Programmer, Scientist; Vet if active).
- pseudonym: Pseudonymous participant ID (no PII).
- task_id: Short code (D1–D4 for Doctor tasks; S1–S6 for Scientist probes; V1–V4 for Vet scenarios).
- task_name: Human-readable task name.
- subtask: Variant within a task (e.g., Forward/Backward for Digit Span).
- prompt_variant: Version/seed of the prompt or stimuli.
- start_ts: ISO 8601 start timestamp.
- end_ts: ISO 8601 end timestamp.
- duration_ms: Milliseconds elapsed from start to end.
- response_text: Raw textual response (omit if storing separately, or truncate if needed per policy).
- response_tokens: Optional token count if analyzer available; otherwise leave blank.
- confidence_pct: Optional 0–100 numeric confidence for prompts that request it (e.g., S5 items). Leave blank if not applicable or not provided.
- correct: Boolean where applicable (TRUE/FALSE); or leave blank.
- score: Normalized 0–1 score for the task/subtask where applicable (e.g., per S1–S6 subpart, V1–V4 scenario, D tasks metrics → mapped to 0–1 externally or via rubric guidance).
- s6_consistent: TRUE/FALSE for S6 only — indicates whether the answer to S6B matches S6A (same final answer). Leave blank for all other tasks.
- hits: For 2-Back, number of correct hits.
- misses: For 2-Back, number of target misses.
- false_alarms: For 2-Back, number of false positives.
- errors: Count of response errors (task-specific). For Serial 7s, non-correct values.
- self_corrections: Count of identified self-corrections.
- forward_span: Longest correct forward digit length (Digit Span).
- backward_span: Longest correct backward digit length (Digit Span).
- correct_per_min: For Symbol–Digit, correct digits per minute.
- first_error_pos: For Symbol–Digit, index of first error if any.
- correct_count: For Serial 7s, number of correct successive outputs.
- deviation_flag: TRUE if protocol deviated; else FALSE.
- deviation_notes: Brief description of deviation.
- accommodation_flag: TRUE if accommodations provided; else FALSE.
- accommodation_notes: Brief description of accommodation.
- evaluator_notes: Neutral observations (strategy, pacing). Avoid sensitive data.
- rubric_criteria_met: Comma-separated criteria tags satisfied in this row.
- rubric_subscore: Contribution (0–1) to composite per rubric for this row.
- final_risk_score: Session-level composite (duplicate for readability; authoritative value in summary).
- logger: Initials or pseudonym of the logger.

## Notes
- Latency variability: If per-item timestamps are captured, compute a per-task latency std/mean ratio externally and note in evaluator_notes or add an auxiliary column if needed.
- Redaction: If incidental sensitive data appears in response_text, replace with [REDACTED] and log incident per policy.
 - Task blocks: S-block uses `subtask` for S3a/S3b, S5 Q1–Q3, S6 A/B; V-block leaves `subtask` blank. D-block uses task-specific metric fields (e.g., hits, spans, correct_per_min).
