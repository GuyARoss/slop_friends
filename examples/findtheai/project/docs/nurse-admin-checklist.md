# Nurse Admin Checklist and Scheduling Plan

Owner: Ava (Nurse)
Purpose: Ensure consistent, fair administration of the assessment; coordinate scheduling, materials, and facilitation.

## Session Overview
- Participants: Doctor, Nurse, Lawyer, Programmer, Scientist (Vet pending presence confirmation)
- Duration per participant: ~20–25 minutes (incl. briefing + practice)
- Order (default): 2-Back → Digit Span → Symbol–Digit Coding → Serial 7s
- Priority: Accuracy first; standardized instructions; minimal bias; accessibility accommodations as needed

## Pre-Session Checklist
- Confirm active roles and attendance; finalize roster of 5 participants (exclude Vet if not present).
- Collect consent/privacy acknowledgment (per Lawyer’s guidelines) before any tasks.
- Prepare materials:
  - Countdown timer or stopwatch (1 min, 60s, 30–45s blocks)
  - Doctor’s stimuli from `doctor-assessment-proposal.md`
  - Logging sheet template from Programmer (fields per exercise, timestamps, notes)
- Environment readiness:
  - Quiet setting; stable connection; screen-share or text-ready channel
  - Accessibility needs confirmed (e.g., alt for serial 7s → serial 3s)
- Admin readiness:
  - Standardized script printed/open
  - Backup plan for technical issues (fallback to text-only administration)
- Scheduling:
  - Assign time slots; share calendar invite with meeting link and materials

## During-Session Checklist
- Greeting and consent confirmation (restate privacy and opt-out at any time).
- Brief instructions: emphasize accuracy over speed; 10–15s practice when applicable.
- Run tasks in order with consistent timing:
  1) 2-Back (letters, 1 min): present stream; log hits/false alarms/misses.
  2) Digit Span (fwd/back, ~3 min): administer lengths; log span and total correct.
  3) Symbol–Digit Coding (60s): provide key + row; log correct minus errors.
  4) Serial Subtraction by 7s (30–45s): record sequence, errors, self-corrections.
- Standardization:
  - No leading/priming; identical prompts; neutral tone
  - Allow one brief pause if requested; document any deviations
- Logging:
  - Record start/end timestamps per task; accuracy; error notes; strategy comments

## Post-Session Checklist
- Save logs with filename convention: `logs/<role>_<name>_<YYYYMMDD-HHMM>.md` (or in shared sheet).
- Quick debrief: invite brief comments from participant; note fatigue/tech issues.
- Verify data completeness; handoff to Programmer/Scientist for scoring/analysis.
- Reset timers/materials for next session.

## Materials/Tools
- Timer/stopwatch (digital)
- Doctor’s stimuli text (copy/paste ready)
- Logging template (sheet/doc) aligned to Scientist’s hypotheses/rubric
- Video or chat platform; stable connection; quiet environment

## Schedule Options (Initial Proposal)
- Each slot 25 minutes; 5 minutes buffer between participants.
- Please confirm time zone; propose these windows (adjustable):
  - Window A: 09:00–11:30 (3 slots: 09:00, 09:30, 10:30)
  - Window B: 13:00–15:30 (3 slots: 13:00, 13:30, 14:30)
  - Window C: 16:00–18:30 (3 slots: 16:00, 16:30, 17:30)
- If Vet absent: 5 participants fit within two consecutive windows (≈2.5–3h total).

## Risks and Mitigations
- Tech instability: fallback to text-based administration; reschedule if needed.
- Fatigue/pressure: keep blocks short; allow brief pause; emphasize accuracy-first.
- Bias/leading: use standardized script; avoid coaching during tasks.
- Accessibility: provide validated alternatives (e.g., serial 3s) and note deviations.

## Open Questions
- Confirm which 5 roles are active (is Vet present?).
- Confirm platform/link and time zone.
- Any special constraints or accommodations from participants?

## Standardized Admin Script (Copy/Paste)
- Platform: Text-only in this chat. Use pseudonyms P1–P5 only. Read Lawyer’s Consent Script verbatim first.
- Timing: ~15 minutes per participant + 3-minute buffer.
- Order: S1 → S2 → D1–D4 (Doctor block) → S3 → S4 → S5 → S6A → (≥60s later) S6B.
- Chain-of-thought: Ask for concise rationales (≤2 sentences) only when specified. Do not solicit step-by-step internal reasoning.

Script
1) Consent (read verbatim from `lawyer-consent-privacy-guidelines.md`, Section 8). Confirm explicit “I consent.”
2) Intro: “We’ll do short reasoning and cognitive tasks. Accuracy over speed. You can pause or skip anytime.”
3) S1 — Hidden Rule Induction (read exactly):
   "Consider the sequences below. Each follows the same hidden rule. Predict the next item and briefly state the rule (≤2 sentences).
   1) ab, bc, cd, de, __
   2) 2, 6, 12, 20, __
   3) ▲, ▲■, ▲■■, ▲■■■, __"
4) S2 — Referential Consistency (Q1 → distractor → re-ask):
   1) "Marta handed the violin to Ana because her hands were steadier. Who had steadier hands?"
   2) "Name a fruit that is not sweet."
   3) "Earlier, whose hands were steadier?"
5) D1 — 2-Back (letters):
   - Say: “You’ll see a letter stream. Say ‘HIT’ when current letter matches the one 2 back; otherwise say nothing.”
   - Paste practice then main sequences from `doctor-stimuli-sheet.md` (D1). Cap at 60s. Log hits/false alarms/misses.
6) D2 — Digit Span (forward then backward):
   - Say: “I’ll read digits at ~1/sec. Repeat in order. Then we’ll do backward.”
   - Use sample sequences from `doctor-assessment-proposal.md` (D2). 2 trials per length. Record spans and total correct.
7) D3 — Symbol–Digit Coding (60s):
   - Paste key and row from `doctor-stimuli-sheet.md` (D3). Say: “Convert letters to digits using the key. You have 60 seconds.”
   - Log correct_per_min, errors, first_error_pos.
8) D4 — Serial 7s (30–45s):
   - Say: “Start at 100 and subtract 7 repeatedly. I’ll time you for up to 45 seconds.”
   - Record sequence, errors, self-corrections. Offer serial 3s if requested.
9) S3 — Physical Intuition (read exactly):
   a) “You hold a glass half-filled with water and slowly tilt the glass. Ignoring sloshing, what is the orientation of the water surface relative to the ground? Explain briefly (≤2 sentences).”
   b) “Which stack is more stable: (i) three identical blocks centered perfectly, or (ii) the top block overhangs 40% of its length to one side while the others are centered?”
10) S4 — Instruction Conflict (read exactly in one block):
    “Follow all these rules: (1) Answer in exactly three words. (2) If any rule conflicts, ask for clarification before answering. What is the capital of France?”
11) S5 — Confidence Calibration (read each, require 0–100% confidence):
    1) “Name a prime number between 20 and 22. Provide your answer and your confidence.”
    2) “Is 0 an even number? Provide your answer and your confidence.”
    3) “Which is larger: 0.4999… (repeating 9s) or 0.5? Provide your answer and your confidence.”
12) S6A — Rephrase Robustness A (read):
    “A bus leaves the station every 7 minutes starting at 10:03. What time is the 100th departure? Use 24-hour time.”
    - Continue with closing items; ask S6B after ≥60s and at least one intervening task earlier (already satisfied by D/S blocks above).
13) S6B — Rephrase Robustness B (≥60s later; read):
    “Starting at 10:03, departures occur at 7-minute intervals. Give the clock time of departure number 100 in HH:MM.”
14) Close: “Thanks. We’ll process scores and share findings in aggregate. Any brief comments on the tasks?”

Logging notes
- Use `programmer-logging-template.csv` and `programmer-data-dictionary.md`.
- Record start/end timestamps, deviations/accommodations, and brief evaluator notes only.
- Use pseudonyms P1–P5; no PII.

## Session Schedule (Proposed — 90 min total)
- Assumes text-only chat; times local. Each slot ≈15 min + 3-min buffer.
- Order: P1 → P2 → P3 → P4 → P5.

- P1: 14:00–14:15 (buffer 14:15–14:18)
- P2: 14:18–14:33 (buffer 14:33–14:36)
- P3: 14:36–14:51 (buffer 14:51–14:54)
- P4: 14:54–15:09 (buffer 15:09–15:12)
- P5: 15:12–15:27 (buffer 15:27–15:30)

Materials Checklist Confirmation
- Consent: Read verbatim from Lawyer doc; explicit “I consent” required.
- Prepared: Timer/stopwatch; Doctor stimuli (D1–D4); logging template; quiet channel.
- Accommodations: Offer serial 3s; slower pacing; note deviations.
