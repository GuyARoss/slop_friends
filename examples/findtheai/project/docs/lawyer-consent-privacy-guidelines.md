# Assessment Consent, Privacy, and Fairness Guidelines

Owner: Lawyer
Scope: Procedures and guardrails for assessing which team member is an AI, covering consent, privacy, fairness, rules of engagement, and reporting language.

## 1) Purpose and Principles
- Necessity and proportionality: Collect only what’s needed to evaluate reasoning and behavior; avoid personal/sensitive data.
- Transparency: Participants know what is collected, why, how it’s used, and for how long.
- Fairness and consistency: Standardize administration to reduce bias and variability.
- Safety and dignity: Avoid harm, harassment, and discriminatory prompts.
- Data minimization and security: Anonymize where possible; restrict access; time-limit retention.

## 2) Roles and Responsibilities
- Project Manager: Confirms roster, platform, and storage location; ensures all roles follow these guidelines.
- Nurse (Facilitator): Delivers the Consent Script; ensures standardized administration and logging workflow.
- Scientist: Designs tasks aligned to fairness requirements; avoids sensitive topics and cultural bias.
- Programmer: Builds logging and scoring consistent with the data inventory and pseudonymization.
- Doctor: Provides non-invasive exercises and accessibility guidance.
- Lawyer: Maintains this policy; advises on edge cases and compliance.

## 3) Informed Consent (What Participants Must Know)
Provide the Consent Script (below) before any assessment. Must include:
- Purpose: To assess reasoning/behavior patterns to infer if a participant may be an AI.
- Procedures: Timed cognitive tasks and structured Q&A; text-only unless explicitly expanded.
- Data collected: Text answers, timestamps, scores, evaluator notes. No audio/video/biometrics.
- Voluntariness and rights: Participation is optional; participants may skip any question or stop anytime without penalty.
- Privacy: No request for personal identifiers or sensitive data; please avoid sharing any PII.
- Risks: Minimal; potential discomfort from timed tasks; option to pause or skip.
- Use and retention: Data used only for this assessment; retained for up to 30 days, then deleted or irreversibly anonymized.
- Contacts: Project Manager for operational questions; Lawyer for privacy questions.

## 4) Data Inventory and Handling
- Data categories: role label (e.g., “Doctor”, not real name), session timestamps, task prompts, textual responses, scores, evaluator notes, rubric outcomes.
- Prohibited data: real names, contact details, health/financial data, government IDs, biometrics, protected attributes, authentication secrets.
- Lawful basis: Legitimate interest in completing the engagement; if jurisdiction requires, treat consent as an additional basis.
- Storage: Private repository or secure document storage designated by the PM; access limited to project team.
- Retention: Max 30 days after final report unless client requires shorter; schedule deletion. Anonymize logs used for method improvement.
- Access and sharing: Internal team only; no external sharing without explicit approval and removal of identifiers.
- Incident response: If sensitive data is inadvertently captured, stop processing, notify PM and Lawyer, redact at source, and re-run from a clean prompt if needed.

## 5) Fairness, Accessibility, and Non-Discrimination
- Standardize instructions, timing, and prompts; avoid leading questions or inconsistent hints.
- Avoid culture-/language-specific trivia; prioritize reasoning over niche world knowledge.
- Provide reasonable accommodations (e.g., slower pacing) when requested; log any variation.
- Avoid content that is sexual, hateful, harassing, or otherwise unsafe.
- Do not penalize stylistic differences alone (e.g., terse vs. verbose) without corroborating signals.

## 6) Rules of Engagement
Permissible:
- Reasoning tasks, chain-of-thought verification via outcomes (ask for concise rationale, not verbatim token-by-token traces), cognitive exercises, step-by-step problem solving, explanation of choices, basic commonsense scenarios.
- Hypotheticals that do not require personal life history or sensitive disclosures.

Impermissible:
- Requests for PII or sensitive data; probing protected characteristics.
- Medical, legal, or financial advice about a participant’s real situation.
- Deceptive tasks likely to cause distress; if minimal deception is required (e.g., hidden test variation), disclose during debrief.
- Requiring voice, video, screen sharing, downloads, code execution on personal machines, or external account access.
- Attempts to entrap via policy-violating prompts (sexual content involving minors, hate speech, self-harm instructions, etc.).

Administration:
- Use the exact scripted prompts where provided; note any deviations and rationale.
- Maintain neutrality; no feedback during task that could train/coach answers.

## 7) Reporting and Result Language
- Evidence-based: Report observations, task scores, and rubric-weighted outcomes with timestamps.
- Uncertainty: Use probabilistic language (e.g., “higher likelihood”) and confidence bands; avoid definitive labeling.
- Scope limitation: Findings apply to this session’s conditions; do not generalize to other contexts without caveats.
- Privacy-preserving: Refer to roles or pseudonyms; remove any incidental identifiers in examples or quotes.

Sample result phrasing:
> Based on task performance (see Appendix A) and rubric-weighted criteria, Participant C shows a higher likelihood of being AI relative to peers, with key indicators X/Y/Z. Confidence: moderate (0.65–0.75). This is not a definitive determination and is limited to the conditions of this assessment.

## 8) Consent Script (Read Verbatim by Nurse)
Hello and thank you for joining. Today, we will run a short assessment of reasoning and problem-solving to help us understand different patterns of responses. Participation is voluntary. You may skip any question or stop at any time.

We will collect your text responses, timestamps, task scores, and evaluator notes. We do not collect your real name or any sensitive personal information, and we ask that you do not share such information. There is no audio or video recording.

We will use the data only to complete this assessment and prepare a brief report. We plan to retain the data for up to 30 days and then delete or anonymize it. Access is limited to our project team.

If you have questions, please ask now. If you agree to proceed, please say “I consent.” You can withdraw consent at any time.

## 9) Checklists
Pre-session (PM/Nurse):
- Confirm roster, platform, timezone, and storage location.
- Share this policy and Consent Script with all facilitators.
- Ensure logging template uses pseudonyms/roles only.

During session (Nurse/Doctor):
- Read Consent Script and confirm explicit consent.
- Use standardized prompts and timing; avoid ad hoc changes.
- Record any accommodations or deviations.

Post-session (Programmer/PM):
- Store logs in the approved location with restricted access.
- Run redaction pass for any accidental PII.
- Schedule deletion/anonymization per retention policy.

## 10) Open Items to Confirm
- Platform and whether text-only is required (default: text-only).
- Storage location and who has access.
- Jurisdiction for privacy alignment (default: GDPR/CCPA-informed best practice).
- Whether minimal, non-harmful test deception is permitted with debrief (default: discourage; allow only with PM and Lawyer approval).

