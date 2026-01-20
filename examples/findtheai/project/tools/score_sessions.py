#!/usr/bin/env python3
"""
Score sessions from programmer-logging-template.csv and produce a per-participant summary.

Inputs:
- project/docs/programmer-logging-template.csv (log rows; may include rubric_subscore or score)

Outputs:
- project/docs/scoring-summary.csv (one row per participant with block means and final_risk_score)

Notes:
- If a row has rubric_subscore, it is preferred over score.
- Blocks: D={D1..D4}, S={S1..S6}, V={V1..V4} averaged within block.
- Error/Latency/Profile (EL) and Protocol Adherence (PA) are optional; default to 0.5 if not derivable.
  You can override via CLI flags.
"""

import argparse
import csv
from collections import defaultdict
from pathlib import Path

LOG_PATH = Path("project/docs/programmer-logging-template.csv")
OUT_PATH = Path("project/docs/scoring-summary.csv")

W_D = 0.35
W_S = 0.35
W_V = 0.15
W_EL = 0.10
W_PA = 0.05


def task_block(task_id: str) -> str | None:
    if task_id.startswith("D"):
        return "D"
    if task_id.startswith("S"):
        return "S"
    if task_id.startswith("V"):
        return "V"
    return None


def parse_float(val):
    try:
        return float(val)
    except Exception:
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--log", default=str(LOG_PATH), help="Path to logging CSV")
    ap.add_argument("--out", default=str(OUT_PATH), help="Output summary CSV path")
    ap.add_argument("--el", type=float, default=None, help="Override Error/Latency/Profile [0..1]")
    ap.add_argument("--pa", type=float, default=None, help="Override Protocol Adherence [0..1]")
    args = ap.parse_args()

    rows = []
    with open(args.log, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(r)

    # Group by participant/session
    sessions = defaultdict(list)
    for r in rows:
        key = (r.get("session_id", ""), r.get("pseudonym", ""))
        sessions[key].append(r)

    out_rows = []
    for (session_id, pseudonym), srows in sessions.items():
        # Collect per-task best subscore
        per_task_scores: dict[str, list[float]] = defaultdict(list)
        missing_notes = []

        for r in srows:
            tid = (r.get("task_id") or "").strip()
            if not tid:
                continue
            # Prefer rubric_subscore; fallback to score
            rs = parse_float(r.get("rubric_subscore"))
            if rs is None:
                rs = parse_float(r.get("score"))
            if rs is not None:
                per_task_scores[tid].append(rs)

        # Aggregate per task (mean of rows per task)
        def mean(vals: list[float]) -> float | None:
            return sum(vals) / len(vals) if vals else None

        per_task_mean: dict[str, float] = {k: mean(v) for k, v in per_task_scores.items()}

        # Compute block means with within-block renormalization for missing tasks
        def block_mean(prefix: str, expected_count: int) -> tuple[float | None, list[str]]:
            keys = [f"{prefix}{i}" for i in range(1, expected_count + 1)]
            vals = [per_task_mean.get(k) for k in keys if per_task_mean.get(k) is not None]
            if not vals:
                return None, [f"no {prefix}-block tasks scored"]
            return sum(vals) / len(vals), []

        D_mean, D_miss = block_mean("D", 4)
        S_mean, S_miss = block_mean("S", 6)
        V_mean, V_miss = block_mean("V", 4)

        # Error/Latency/Profile and Protocol Adherence
        EL = args.el if args.el is not None else 0.5
        PA = args.pa if args.pa is not None else 0.5

        # Adjust weights if entire blocks are missing
        weights = {"D": W_D if D_mean is not None else 0.0,
                   "S": W_S if S_mean is not None else 0.0,
                   "V": W_V if V_mean is not None else 0.0,
                   "EL": W_EL,
                   "PA": W_PA}
        total_w = sum(weights.values())
        if total_w == 0:
            final_score = None
        else:
            # Normalize weights proportionally
            for k in weights:
                weights[k] /= total_w
            final_score = (
                (D_mean or 0) * weights["D"] +
                (S_mean or 0) * weights["S"] +
                (V_mean or 0) * weights["V"] +
                EL * weights["EL"] +
                PA * weights["PA"]
            )

        note_parts = D_miss + S_miss + V_miss
        notes = "; ".join(note_parts)

        out_rows.append({
            "session_id": session_id,
            "pseudonym": pseudonym,
            "D_mean": f"{D_mean:.3f}" if D_mean is not None else "",
            "S_mean": f"{S_mean:.3f}" if S_mean is not None else "",
            "V_mean": f"{V_mean:.3f}" if V_mean is not None else "",
            "EL": f"{EL:.3f}",
            "PA": f"{PA:.3f}",
            "final_risk_score": f"{final_score:.3f}" if final_score is not None else "",
            "missing_data_notes": notes,
        })

    # Write output
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["session_id", "pseudonym", "D_mean", "S_mean", "V_mean", "EL", "PA", "final_risk_score", "missing_data_notes"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in out_rows:
            writer.writerow(r)

    print(f"Wrote {args.out} with {len(out_rows)} participant(s)")


if __name__ == "__main__":
    main()

