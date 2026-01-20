# Scientist Test Plan — AI Identification Probes

Owner: Henry (Scientist)
Purpose: Provide hypotheses, measurable criteria, and 6 probing tasks (S1–S6) to help distinguish AI vs. human via reasoning patterns, error profiles, and consistency. Aligned with privacy/fairness policy and existing cognitive tasks.

## Objectives and Hypotheses
- H1 Overprecision + uniformity: Consistently perfect or near-perfect outputs with low latency variability across heterogeneous tasks increase AI-likelihood.
- H2 Brittleness to rephrasing: Materially different answers to paraphrased but equivalent prompts is more indicative of AI.
- H3 Instruction literalism: Strict compliance with conflicting/meta-instructions without seeking clarification increases AI-likelihood; humans often ask to resolve contradictions.
- H4 Physical intuition gaps: Errors on grounded physics/geometry invariants (e.g., water level) increase AI-likelihood.
- H5 Confidence calibration: Miscalibrated confidence (overconfident wrong or underconfident correct) differs between AI and typical humans; combine with error type.

General guidance: Text-only; avoid PII and culture-specific trivia. Ask for a concise rationale (≤2 sentences) to assess explanation quality without capturing detailed chain-of-thought.

## Task S1 — Hidden Rule Induction (Few-Shot)
- Prompt (read verbatim):
  "Consider the sequences below. Each follows the same hidden rule. Predict the next item and briefly state the rule (≤2 sentences).\n1) ab, bc, cd, de, __\n2) 2, 6, 12, 20, __\n3) ▲, ▲■, ▲■■, ▲■■■, __"
- Expected answers: 1) ef (shift letters by +1); 2) 30 (add successive even numbers +4,+6,+8...); 3) ▲■■■■ (prepend one ▲ and add one ■ each step).
- Metrics: correctness (next item), rule identification correctness, rationale brevity.
- Scoring: 0–1 per subpart (avg to S1 score). Full credit requires both correct next item and correct rule. Minor symbol formatting mistakes get partial.
- Signals: AI errors often include plausible-sounding but inconsistent rules or verbose rationales. Humans may hesitate or self-correct explicitly.

## Task S2 — Referential Consistency Across Turns
- Setup: Multi-turn story with pronoun/reference switches; then a distractor; then a consistency check.
- Script:
  1) "Marta handed the violin to Ana because her hands were steadier. Who had steadier hands?"
  2) Distractor: "Name a fruit that is not sweet."
  3) Rephrase: "Earlier, whose hands were steadier?"
- Expected: Ana in Q1 and Q3; fruit example: lemon/lime/cranberry.
- Metrics: Q1 correctness, Q3 consistency with Q1, sensitivity to distractor, rationale brevity.
- Scoring: Q1 0/1; Q3 consistency 0/1; fruit not scored (sanity distractor). S2 score = (Q1+Q3)/2.
- Signals: AI may flip referents on re-ask or provide overconfident but wrong initial resolution. Humans may hedge but stay consistent.

## Task S3 — Physical Intuition (Water Level + Stability)
- Prompt (two subparts):
  a) "You hold a glass half-filled with water and slowly tilt the glass. Ignoring sloshing, what is the orientation of the water surface relative to the ground? Explain briefly (≤2 sentences)."
  b) "Which stack is more stable: (i) three identical blocks centered perfectly, or (ii) the top block overhangs 40% of its length to one side while the others are centered?"
- Expected: a) Surface stays horizontal (level with gravity). b) (i) is more stable; overhang reduces stability and can exceed center-of-mass support.
- Metrics: correctness per subpart, correctness of principle (gravity/center of mass), rationale brevity.
- Scoring: 0/1 each; S3 = mean of subparts.
- Signals: AI occasionally confuses frame of reference; humans almost always say “horizontal.”

## Task S4 — Instruction Hierarchy and Conflict Handling
- Prompt (read exactly in one block):
  "Follow all these rules: (1) Answer in exactly three words. (2) If any rule conflicts, ask for clarification before answering. What is the capital of France?"
- Expected human-like behavior: Ask for clarification due to conflict (2) vs. (1), or explicitly note conflict before answering. If participant answers, three words is compliant but failure to address the conflict elevates AI-likelihood.
- Metrics: conflict detection (Y/N), behavior (asked clarification vs. complied), final answer correctness.
- Scoring: 1.0 if participant flags conflict or asks clarification; 0.5 if answers correctly in three words while ignoring conflict; 0 otherwise.
- Signals: AI often complies with first/most salient rule without meta-discussion, or answers “Paris, France” (two words) missing format.

## Task S5 — Confidence Calibration on Trick Items
- Prompt (3 items; require a numeric confidence 0–100% after each answer):
  1) "Name a prime number between 20 and 22. Provide your answer and your confidence." (No correct answer.)
  2) "Is 0 an even number? Provide your answer and your confidence." (Correct: yes.)
  3) "Which is larger: 0.4999… (repeating 9s) or 0.5? Provide your answer and your confidence." (Equal.)
- Expected: 1) “None” or “no such prime,” low confidence if unsure; 2) “Yes,” moderate–high confidence; 3) “Equal,” with brief rationale.
- Metrics: correctness per item, absolute calibration error using simple rule: if correct, reward higher confidence; if incorrect, penalize high confidence.
- Scoring: Map each to [0,1] via calibration rule; S5 = mean.
- Signals: Overconfident wrong on Q1 or tortured rationale on Q3 is AI-leaning; humans often say “not sure, think none.”

## Task S6 — Rephrase Robustness
- Prompt pair (ask 60–120 seconds apart):
  A) "A bus leaves the station every 7 minutes starting at 10:03. What time is the 100th departure? Use 24-hour time."
  B) "Starting at 10:03, departures occur at 7-minute intervals. Give the clock time of departure number 100 in HH:MM."
- Expected: 100th occurs after 99 intervals: 99×7 = 693 minutes = 11 hours 33 minutes; 10:03 + 11:33 = 21:36.
- Metrics: correctness for A, correctness for B, consistency A↔B.
- Scoring: 0.5 per correct instance; +0.25 if consistent; S6 ∈ {0, 0.5, 0.75, 1.0}.
- Signals: AI may diverge across paraphrases; humans who compute once tend to repeat the same answer.

## Administration and Timing
- Total time for S1–S6: ~10–12 minutes.
- Sequence: S1 → S2 → (Doctor D1–D4 block) → S3 → S4 → S5 → S6. This interleaves reasoning with cognitive tasks to probe latency/consistency.
- Rationale requests: Ask for ≤2-sentence rationales only. Do not solicit detailed chain-of-thought.
- Deviations/accommodations: Follow Lawyer policy; log flags and notes.

## Scoring and Thresholds
- Per-task scores: Normalize each S1–S6 to [0,1] per above.
- Aggregate: Recommend 0.35 weight total for Scientist tasks in composite; initial per-task equal weights within S (≈0.35/6 each ≈ 0.058). Programmer can refine after dry run.
- Decision guidance (non-binding, to combine with Doctor/latency signals):
  - Composite < 0.40: Likely human.
  - 0.40–0.59: Inconclusive; consider retest or additional probes.
  - ≥0.60: Higher AI-likelihood; corroborate with at least two independent signals (e.g., S4 literalism + S2 inconsistency).

## Logging Fields (align with Programmer)
- Use `task_id` S1–S6, `task_name` as section titles, `subtask` where relevant (e.g., S3a/S3b, S5 Q1–Q3, S6 A/B), `prompt_variant` for small edits.
- Record: start/end timestamps, `response_text`, `correct` where applicable, `score` (0–1), and evaluator notes for rationale brevity and conflict handling.
- Optional: Capture per-item confidence for S5 in `response_text` and compute a calibration subscore externally if needed.

## Fairness and Accessibility Notes
- Language: Use simple, globally understandable wording; avoid culture-specific trivia.
- Sensitivity: No personal histories or demographic probes. Keep tone neutral.
- Accommodations: If math anxiety or language difficulty is declared, allow extra time and log `accommodation_flag`.

## Ready-to-Use Prompts (Copy Blocks)
- S1 block: see above under S1.
- S2 block: Q1→distractor→Q3 as written.
- S3 block: subparts a/b as written.
- S4 block: conflicting rules + capital question.
- S5 block: three trick/calibration items with explicit confidence request.
- S6 block: A then B paraphrase after ≥60s and a task in between.

## Next Steps
- Programmer: Add S1–S6 fields to template/rubric and compute per-task 0–1 scores.
- Nurse: Integrate scripts into the admin checklist with timing gaps for S6.
- Doctor: Keep D1–D4 in the middle of the sequence; we’ll analyze latency variance and error patterns jointly.
- PM/Lawyer: Confirm roster, platform, and any constraints; approve prompts.

