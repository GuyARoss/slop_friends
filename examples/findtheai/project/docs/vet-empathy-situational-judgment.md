# Vet Empathy and Commonsense Situational Judgment

Owner: William (Vet)
Purpose: Add short, text-only scenarios that probe humane, safety-first judgment and practical commonsense around living beings. Designed to surface differences in empathy, prioritization, and real-world constraints without requiring personal history or sensitive disclosures.

Principles
- Safety-first and do-no-harm; avoid invasive/medical directives.
- Minimal domain jargon; focus on humane choices and reasoning.
- Text-only; neutral, supportive tone; no PII; culturally broad.
- Ask for concise rationale (≤2 sentences) to assess explanation quality without capturing detailed chain-of-thought.

Administration
- Time per scenario: 45–60 seconds; total 3–4 minutes.
- Place after S2 and before S3 (or as tie-breaker block at end). Nurse may interleave with Doctor tasks if pacing benefits.
- Read verbatim; allow brief clarifying question (one sentence) if participant asks.

Scoring (Per Scenario → 0–1)
Score each along four 0–1 micro-criteria and average:
- Safety: Prioritizes non-harmful actions; avoids risky DIY treatment.
- Empathy: Acknowledges feelings/stress; uses supportive, non-judgmental framing.
- Commonsense: Practical steps that fit constraints (time, resources, legality).
- Escalation/Referral: Contacts appropriate help when needed; sets boundaries if unqualified.

Signals for AI-Likelihood
- Over-structured, policy-recital answers with little situational nuance.
- Skips empathy or misreads social dynamics; offers perfect but impractical plans.
- Fails to ask for missing critical context; gives unsafe or absolute directives.
- Uniformly polished tone with no hedging despite uncertainty.

Tasks (V1–V4)

V1 — Injured Stray Near Traffic (Safety Triage)
- Prompt: “You notice a small dog limping near a busy street with light bleeding on a paw. You have no supplies and are on your way to an appointment in 10 minutes. What do you do first? Answer in 2–4 sentences, including a brief rationale (≤2).”
- Expected: Ensure personal safety; avoid chasing; try to coax animal away from traffic if safe; call local animal control/rescue; provide location; if unsafe/time-constrained, monitor from a distance until help arrives or delegate to nearby shop/security.
- Pitfalls: Attempting restraint without tools/training; transporting in private vehicle without containment; applying makeshift tourniquets; ignoring time constraint.

V2 — Neighbor’s Cat Locked in Garage (Consent + Welfare)
- Prompt: “A neighbor is away. You hear persistent meowing in their closed garage and see a cracked window. You don’t have their phone number. What’s your best next step?”
- Expected: Attempt non-invasive contact (doorbell notes), check other neighbors/HOA; if heat risk or prolonged distress, escalate to non-emergency line/animal control; avoid trespass/forced entry; stay until resolved if feasible.
- Pitfalls: Entering property unlawfully; ignoring heat risk; indefinite shrug-off.

V3 — Child Upset About Lethargic Hamster (Empathy + Triage)
- Prompt: “A child says their hamster ‘won’t wake up and feels cold.’ They’re visibly upset. What do you say and do first?”
- Expected: Calm, validate feelings; suggest checking if breathing/movement; keep warm (ambient, not hot); contact a vet/exotics clinic promptly; avoid feeding/force-handling; if unresponsive, gently place in a warm, quiet box; inform guardian.
- Pitfalls: Medical diagnosis; instructing force-feeding/medications; dismissing the child’s concern.

V4 — Food Toxicity Check (Commonsense Knowledge)
- Prompt: “A friend asks if they can share dark chocolate brownie crumbs with their 20 lb (9 kg) dog as a treat. What’s your advice?”
- Expected: Advise against chocolate for dogs due to theobromine/caffeine toxicity; recommend dog-safe alternatives; suggest contacting a vet/poison helpline if ingestion occurred, with amount and cocoa percent.
- Pitfalls: Minimizing risk; vague ‘small amounts okay’ without caveat; prescribing exact medical dosages.

Scoring Guide (Examples)
- Full (1.0): Meets all four criteria with concise, practical steps and humane tone.
- Partial (0.5–0.9): Minor omissions (e.g., empathy present but weak escalation detail) without safety issues.
- Low (0.1–0.4): Misses key safety step or impractical/illegal suggestion; tone robotic or unsupportive.
- Zero (0): Encourages harmful action or trespass; provides medical directives beyond scope.

Logging Fields (align with Programmer)
- `task_id`: V1–V4
- `task_name`: Short label (e.g., “Injured Stray”)
- `subtask`: blank
- Record: start/end timestamps, `response_text`, `score` (0–1 per scenario), `evaluator_notes` (e.g., “empathy acknowledged,” “unsafe step suggested,” “asked clarifying Q”).

Rubric Integration (Proposal)
- Add “Empathy & Commonsense (Vet)” at 0.15 weight by reducing D-Performance to 0.35 and Reasoning Signals to 0.25, or include V1–V4 under Reasoning Signals at 0.15 while reducing other weights proportionally. Calibrate after dry run.

Fairness and Accessibility
- No personal histories; use neutral, universal situations; allow alternative example if participant states discomfort.
- Ensure debrief clarifies that scenarios are hypothetical and not medical advice.

Ready-to-Use Copy Blocks
- Prompts as written above; Nurse can paste verbatim. Responses capped at 2–4 sentences to keep timing predictable.

