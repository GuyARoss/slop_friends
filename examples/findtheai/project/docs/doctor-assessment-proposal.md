# Doctor Assessment Proposal (Cognitive/Attention/Working-Memory)

Owner: Oliver (Doctor)
Purpose: Provide short, non-invasive exercises suitable for a timed session to help distinguish AI vs. human patterns while remaining fair and accessible.

## Overview
- Total exercises: 4
- Total time: ~8–10 minutes active time (+ setup)
- Focus: Working memory, selective attention, processing speed, mental arithmetic
- Scoring: Accuracy primary, speed secondary; record errors and skips

## Exercise 1 — 2-Back (Letters)
- Duration: 1 minute (stimulus every 2 seconds; ~30 items)
- Stimuli: Uppercase letters A–H (avoid similar glyphs like I, O)
- Task: Indicate when current letter matches the one 2 positions back.
- Administration: Present continuous stream; participant responds “HIT” on matches, “MISS”/no response otherwise. If live, facilitator calls out; in chat, paste the stream ahead of time with timestamps.
- Scoring: Hits, false alarms, misses; compute sensitivity (d-prime if desired) or simple accuracy = (correct responses / total targets).
- Rationale: Probes updating/maintenance; typical human accuracy <100%, with speed-accuracy trade-off.

Example sequence (targets at positions 3, 12, 23):
G  A  G  D  C  F  H  E  D  F  A  D  B  C  A  E  F  G  F  E  C  E  C  D  B  A  H  G  E  F

## Exercise 2 — Digit Span (Forward and Backward)
- Duration: ~2–3 minutes
- Stimuli: Random digit sequences (no patterns), read at ~1 digit/sec
- Task: Repeat digits in order (forward); then in reverse (backward)
- Administration: 2 trials per length. Start forward length 5; increase until failure on both trials at a length; then backward starting at length 3.
- Scoring: Span = longest length with at least one correct trial; record total correct trials.
- Rationale: Probes phonological loop and executive manipulation (backward).

Sample sequences:
- Forward: 7-2-9-4-1 | 6-8-3-5-2 | 4-9-1-6-3-8 | 2-7-5-1-9-6
- Backward: 5-8-2-6 | 3-9-1-7 | 4-2-8-6-3 | 9-1-6-2-7

## Exercise 3 — Symbol–Digit Coding (Keyed Substitution)
- Duration: 60 seconds
- Stimuli: Fixed key mapping 9 letters → digits (scrambled)
- Task: Convert a row of letters to digits using the key as quickly/accurately as possible.
- Administration: Provide key and a 60-character letter row. Participant returns digit string; allow skipping.
- Scoring: Correct digits per minute; subtract errors; note position of first error.
- Rationale: Processing speed and sustained attention with minimal language load.

Key:
1=A  2=F  3=K  4=P  5=U  6=B  7=G  8=L  9=Q

Row (60 chars):
L B F A U G Q P K  A F L G B Q U P K  A B F L G Q U P K  A F L B G Q U P K  A F L G B Q U P K

## Exercise 4 — Serial Subtraction (by 7s)
- Duration: 30–45 seconds
- Task: Starting at 100, subtract 7 repeatedly, stating each result.
- Administration: Time-bound; facilitator or logger records sequence and errors.
- Scoring: Correct responses minus errors; note self-corrections.
- Rationale: Working memory + attention under mild load; widely used (e.g., MOCA).

Expected sequence (first 10): 93, 86, 79, 72, 65, 58, 51, 44, 37, 30

## Accessibility and Sensitive Areas (Avoid/Accommodate)
- Vision/Color: No color-based tasks; large, high-contrast text; avoid visually confusable glyphs.
- Language: Keep stimuli language-light; avoid idioms/culture-specific knowledge.
- Neurodiversity: Offer alt for math-heavy tasks (e.g., serial 3s instead of 7s) and for digit span (word span if dyscalculia/dyslexia).
- Motor/Speed: Emphasize accuracy over speed; allow brief practice.
- Privacy: No personal memory recall, health history, or emotionally charged content.
- Fatigue/Stress: Short blocks; clear stopping rules; permit brief pause if needed.

## Materials and Logging
- Materials: Text sequences above; countdown timer; simple tally sheet.
- Logging: Record start/end time, responses, accuracy, errors, comments about strategy.
- Integration: Programmer can template a sheet with fields per exercise; Scientist can set thresholds (e.g., >90% 2-back with near-zero false alarms is atypical; perfect serial 7s under 30s also atypical).

## Admin Script (Concise)
1) Explain that tasks are simple, timed, and optional; accuracy over speed.
2) Run 10–15s practice for each when applicable.
3) Execute in order: 2-Back → Digit Span → Coding → Serial 7s.
4) Log results; thank participant.

