# Experiment & Data

Canonical detail: [../docs/MORPHINE_PR_EXPERIMENT.md](../docs/MORPHINE_PR_EXPERIMENT.md)

## Timeline (18 days)

| Days | Phase | Reward | Notes |
|------|-------|--------|-------|
| 1–2 | Habituation | Sucrose | FR1, FR3 |
| 3–5 | Pre | Water | PR baseline |
| 6–10 | During | Morphine | **Active vs yoked passive** |
| 11–13 | Post | Morphine | Both groups active PR |
| 14–16 | Withdrawal | Water | Abstinence from morphine |
| 17–18 | Re-exposure | Morphine | Reinstatement test |

## Active vs passive (Days 6–10)

| | Active | Passive (yoked) |
|---|--------|-----------------|
| Licks counted | Yes (`valid: true`) | No (`valid: false`) |
| Rewards | Contingent on PR | Replay from paired active mouse |
| Learning | Action–outcome | Exposure + context (Pavlovian) |

## PR task

- Schedule: **PR1** — requirement increases by 1 per successful trial (trial 0 → 1 lick, trial 1 → 2 licks, …)
- Session ~15 min
- **Breakpoint:** `requirementLast` = max requirement achieved

## JSONL events (behavioral)

File pattern: `{cage}{mouse}_{phase}{day}.jsonl`

| `tag` | Use |
|-------|-----|
| `meta` | Session parameters (increment, lockout, reward duration) |
| `trial_start` | `req` = current requirement |
| `lick` | `n`, `valid`, `elapsed` |
| `reward_cmd` / `reward_end` | Reward timing |
| `trial_end` | `requirement`, `counted`, `hit`, `rt_ms` |

## Derived features (for modeling)

**Session-level:** `requirementLast`, total rewards, lick rate, mean/median ILI, bout counts, session duration

**Lick-level (for drift fit):** timestamp, rewarded vs unrewarded, trial index, current requirement `T`, pause duration

**Phase labels:** `pre | during | post | withdrawal | reexposure` + `group: active | passive`

## Data checklist for CS / SBI fitting

Required:

- `mouse_id`, `group`, `phase`, `day`
- Lick timestamps; reward timestamps
- Rewarded vs unrewarded per lick (or infer from trial structure)
- PR requirement `T` per trial / lick
- Breakpoint per session

Highly useful:

- Pause duration, bout onsets/offsets
- Latency to first lick, re-engagement after pause
- Lockout timing (newer cohort)
- Cue / drug availability flags

## Pharmacology (parallel, not v1 model core)

- TI (days 5–18), TST/HP/Straub at phase endpoints — link later, not required for first drift fit.

## Planned code layout (not yet in repo)

From parent doc — implement under e.g. `morphine_pr_analysis/`:

```
src/data_processing/jsonl_parser.py
src/feature_extraction/behavioral_features.py
src/modeling/   ← drift, dual-state, SBI wrappers (TO BUILD)
```

## Raw data location

User-specific. Agents: **ask** or use paths given in session; do not invent cage IDs.
