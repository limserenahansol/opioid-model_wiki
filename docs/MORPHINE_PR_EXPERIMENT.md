# Morphine PR Experiment — Reference (condensed)

Self-contained summary for [opioid-model_wiki](https://github.com/limserenahansol/opioid-model_wiki).

**Full data rules:** [model/07_DATA_RULES_AND_LIKELIHOOD.md](../model/07_DATA_RULES_AND_LIKELIHOOD.md)  
**Data locations:** [DATA_SOURCES.md](./DATA_SOURCES.md)

## Analysis filter

- **Exclude** `day_index` 1–3 (FR + unstable first PR day)  
- **Include** `day_index ≥ 4`  
- **Passive During 6–10:** mask licks in likelihood; rewards still valid  

## Timeline (18 days)

| Days | Phase | Reward | Active | Passive |
|------|-------|--------|--------|---------|
| 1–2 | Habituation | Sucrose | FR1, FR3 | Same |
| 3–5 | Pre | Water | PR | PR |
| 6–10 | During | Morphine | PR (contingent) | Yoked (`valid: false` licks) |
| 11–13 | Post | Morphine | PR | PR |
| 14–16 | Withdrawal | Water | PR | PR |
| 17–18 | Re-exposure | Morphine | PR | PR |

## PR task

- PR1: requirement +1 per successful trial
- Session ~15 min
- Breakpoint: `requirementLast` (max requirement in session)

## JSONL events

| `tag` | Key fields |
|-------|------------|
| `meta` | paradigm, increment, lockout, reward duration |
| `trial_start` | `req` |
| `lick` | `n`, `valid`, `elapsed` |
| `reward_cmd` / `reward_end` | timing |
| `trial_end` | `requirement`, `counted`, `hit`, `rt_ms` |

Passive During phase: all licks `valid: false`; rewards yoked from paired active mouse.

## Modeling readouts

- Session: `requirementLast`, lick rate, ILI, bouts, pauses
- Lick-level: rewarded vs unrewarded, requirement `T`, phase, group

See [wiki/02_EXPERIMENT_AND_DATA.md](../wiki/02_EXPERIMENT_AND_DATA.md) for fitting checklist.
