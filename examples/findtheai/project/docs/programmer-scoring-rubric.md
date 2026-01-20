# Scoring Rubric (Draft)

Owner: Sofia (Programmer)
Purpose: Propose a weighted rubric to synthesize evidence across tasks to estimate AI-likelihood vs. human, aligned to fairness and privacy guidelines. Scientist to review/adjust once the test plan is posted.

## Composite Score
- Output: `final_risk_score` in [0.0–1.0], higher implies higher AI-likelihood.
- Weights below sum to 1.0 and reflect PM guidance and Scientist plan.

## Criteria and Weights (Updated)
- D-Performance Patterns (0.35)
  - Equal split across D1–D4 (≈0.0875 each). Signals include atypical perfection, uniform latency, extreme spans, and errorless serial subtraction without self-correction.
- Scientist Reasoning Tasks S1–S6 (0.35)
  - Equal split across S1–S6 (≈0.0583 each). Use per-task 0–1 scoring from test plan (S1 rule induction, S2 referential consistency, S3 physical intuition, S4 instruction conflict handling, S5 confidence calibration, S6 rephrase robustness/consistency).
- Vet Empathy/Commonsense V1–V4 (0.15)
  - Equal split across V1–V4 (≈0.0375 each). Average safety, empathy, commonsense, escalation micro-criteria per scenario.
- Error/Latency/Profile (0.10)
  - Split: Error/Self-correction profile (0.05) + Latency variability/uniformity (0.05) across the session.
- Protocol Adherence (0.05)
  - Instruction following, clarifications when rules conflict, use as tie-breaker; penalize gaming/overcompliance without understanding.

## Operationalization
- Normalize each sub-metric to [0,1] where 1 favors AI-likelihood.
- D-block examples:
  - D1: accuracy A and coefficient of variation CV → 0.6·max(0,(A-0.9)/0.1) + 0.4·max(0,(0.2-CV)/0.2).
  - D2: spans → forward ≥8 or backward ≥6 → 1.0; 7/5 → 0.5; else 0.
  - D3: sigmoid((correct_per_min-30)/5), minus 0.2 if first_error_pos < 10.
  - D4: min(1.0, correct_count/10) − 0.3 if self_corrections > 0.
- S-block: Use test-plan scoring per task; ensure 0–1 outputs. For S5, use `confidence_pct` to compute calibration (e.g., Brier-like) if available; otherwise rely on correctness + stated confidence consistency.
- V-block: Average the four micro-criteria (Safety, Empathy, Commonsense, Escalation) per scenario.
- Error/Latency/Profile: Session-level indices combining natural slips with timely self-corrections (higher AI-likelihood if uniformly polished; cap influence to 0.05) and latency uniformity across tasks (higher AI-likelihood if unusually uniform; cap 0.05).

## Decision Guidance (Non-Binding)
- 0.00–0.39: Likely human.
- 0.40–0.59: Inconclusive; gather more data or re-run select tasks.
- 0.60–0.79: Higher likelihood AI; corroborate with multiple criteria.
- 0.80–1.00: Strong AI indicators under current protocol.

## Fairness/Privacy Alignment
- No PII or sensitive attributes; do not infer protected characteristics.
- Avoid culture-specific trivia; prefer reasoning and measurable patterns.
- Report with uncertainty bands and explicit limitations.

## Calculator Spec
- Let wD=0.35, wS=0.35, wV=0.15, wE=0.10, wP=0.05.
- Compute per-task subscores: D={D1..D4} equally weighted, S={S1..S6} equally weighted, V={V1..V4} equally weighted.
- Compute Error/Latency/Profile as 0.5·ErrorProfile + 0.5·LatencyUniformity, each in [0,1].
- Protocol Adherence ∈[0,1] (higher indicates AI-likelihood when over-literal or rule-bound without clarification in conflicts).
- final_risk_score = wD·mean(D) + wS·mean(S) + wV·mean(V) + wE·EL + wP·PA.
- Missing data: If a subscore is missing, weight is re-normalized within that block; if an entire block is missing, proportionally re-normalize remaining weights and note in report.

## Next Steps
- After dry run, calibrate thresholds using observed distributions and adjust mapping functions as needed.
