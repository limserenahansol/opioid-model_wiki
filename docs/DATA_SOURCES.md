# Data Sources & Code

Where files live for AMM fitting. **Not** email — operational map only.

---

## Primary cohort: run_009 (Dec 2025)

| Resource | Link / path |
|----------|-------------|
| **JSON extract (for Eli / Python)** | [Drive folder](https://drive.google.com/drive/folders/1tmojU4ahssZEvAdNGa5w6BfPAYERuYsV?usp=drive_link) |
| **Full dataset (~3.6 GB needed)** | [Drive — analysis bundle](https://drive.google.com/drive/folders/12QMUiNDzg3gf822YJkQBE0D0QJrXH2Kf) |
| **Start here on Drive** | `README_for_Eli.md` — 60s block: 5 files to grab, pandas event extract, four analysis rules |

**Why run_009:** Lockout window **annotated** for passive During (days 6–10) → direct mask in likelihood. Prefer over old lockout-free cohort unless reproducing legacy analyses.

---

## Analysis code (MATLAB)

| Resource | Link |
|----------|------|
| **Repository** | [github.com/limserenahansol/opioidaddiction-matlab](https://github.com/limserenahansol/opioidaddiction-matlab) |
| **Rulebook script** | `step10_pr_licking_trajectory_phenotype/run_step10_pr_lick_trajectory_phenotype.m` (constants at top = Hansol’s analysis rules) |

---

## Wiki / model spec (this repo)

| Resource | Link |
|----------|------|
| **AMM spec** | [github.com/limserenahansol/opioid-model_wiki](https://github.com/limserenahansol/opioid-model_wiki) |
| **Data rules** | [model/07_DATA_RULES_AND_LIKELIHOOD.md](../model/07_DATA_RULES_AND_LIKELIHOOD.md) |
| **Fit priority** | [model/08_FITTING_PRIORITY.md](../model/08_FITTING_PRIORITY.md) |

---

## Collaborator

| | |
|---|---|
| **Modeling** | Elijah Paul (Eli) — Tier 1 drift + sigmoid λ; MLE per mouse — see [model/09](../model/09_ELI_IMPLEMENTATION.md) |
| **Behavior / data** | Hansol Lim — paradigm, run_009, lockout rules, wiki updates |

---

## File types in JSON extract

- Per-lick / per-reward events (TTL-aligned)
- Fields include: `day_index`, `isPassive`, `Period`, `PairID`, `Lick_TTL`, `Injector_TTL` / reward TTL (exact names per manifest)

Cross-reference: mouse manifest in Drive for Active/Passive and pairs.

---

## Minimum files for pipeline dev

1. One **active Post** session: `6099_orange`, day 12 or 13  
2. One **passive During** session: `6099_red`, day 6–10  
3. Mouse manifest (group + `PairID`)

See [model/07](../model/07_DATA_RULES_AND_LIKELIHOOD.md) for likelihood rules.
