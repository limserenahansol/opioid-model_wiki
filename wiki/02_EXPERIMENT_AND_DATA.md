# Experiment & Data

**Canonical:** [../model/07_DATA_RULES_AND_LIKELIHOOD.md](../model/07_DATA_RULES_AND_LIKELIHOOD.md) · [../docs/DATA_SOURCES.md](../docs/DATA_SOURCES.md)

---

## Cohort

**run_009** (Dec 2025) — lockout annotated for passive During.

---

## Analysis rules (summary)

| Rule | Value |
|------|-------|
| Drop days | 1, 2, 3 |
| Analyze | `day_index ≥ 4` |
| Passive lockout | days 6–10 During: **mask licks**, keep rewards |
| Pairs | `PairID` random effect |
| Phase focus days | 4, 7, 12, 15, 18 (2nd day of phase) |

---

## Starter mice

- **Active:** `6099_orange`, day 12 or 13 (Post)  
- **Passive:** `6099_red`, day 6–10 (During)

---

## JSON / events

See [../docs/MORPHINE_PR_EXPERIMENT.md](../docs/MORPHINE_PR_EXPERIMENT.md) for event tags; run_009 uses TTL fields (`Lick_TTL`, `Injector_TTL`) per Drive README.
