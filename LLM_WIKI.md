# LLM Wiki — Addiction Motivational Model (AMM)

**GitHub:** [github.com/limserenahansol/opioid-model_wiki](https://github.com/limserenahansol/opioid-model_wiki)

> **Read `model/` first.** Computational addiction model + **run_009 data rules** — not email archives.

---

## Canonical model documentation

| # | Document | Content |
|---|----------|---------|
| — | [model/00_OVERVIEW.md](./model/00_OVERVIEW.md) | AMM index |
| 1 | [model/01_LOGIC_FLOW.md](./model/01_LOGIC_FLOW.md) | Question → motifs → groups → behavior |
| 2 | [model/02_STATE_ARCHITECTURE.md](./model/02_STATE_ARCHITECTURE.md) | V, D, C, G, x; motifs A–D |
| 3 | [model/03_MATHEMATICAL_MODELS.md](./model/03_MATHEMATICAL_MODELS.md) | M0–M4 equations |
| 4 | [model/04_GROUP_AND_PHASE.md](./model/04_GROUP_AND_PHASE.md) | Active vs passive × days |
| 5 | [model/05_FITTING_WORKFLOW.md](./model/05_FITTING_WORKFLOW.md) | JSON → mask → SBI |
| 6 | [model/06_PREDICTIONS.md](./model/06_PREDICTIONS.md) | H0–H4 tests |
| **7** | [model/07_DATA_RULES_AND_LIKELIHOOD.md](./model/07_DATA_RULES_AND_LIKELIHOOD.md) | **day≥4, lockout mask, pairs** |
| **8** | [model/08_FITTING_PRIORITY.md](./model/08_FITTING_PRIORITY.md) | **Tier 1–4; Eli alignment** |
| **9** | [model/09_ELI_IMPLEMENTATION.md](./model/09_ELI_IMPLEMENTATION.md) | **Eli MLE implementation (live)** |

---

## Data & code (run_009)

| Resource | Link |
|----------|------|
| JSON for fitting | [Drive](https://drive.google.com/drive/folders/1tmojU4ahssZEvAdNGa5w6BfPAYERuYsV?usp=drive_link) |
| README_for_Eli | [Drive bundle](https://drive.google.com/drive/folders/12QMUiNDzg3gf822YJkQBE0D0QJrXH2Kf) |
| MATLAB analysis | [opioidaddiction-matlab](https://github.com/limserenahansol/opioidaddiction-matlab) |
| Full map | [docs/DATA_SOURCES.md](./docs/DATA_SOURCES.md) |

---

## Critical analysis rules (never violate)

1. **`day_index ≥ 4`** only (drop FR days 1–2 and unstable PR day 3).
2. **Passive During (days 6–10):** mask **Lick_TTL** from likelihood → **unobserved**, not zero.
3. **Reward / Injector_TTL** always valid (yoked rewards).
4. **`PairID`** = random effect for group inference.
5. **`x_t`** hidden; `λ_t = softplus(x_t)`; quit if `x_t < θ_stop`.
6. **Fit Tier 1 (M0–M1) before** dual-state or generalized-gain extensions.

---

## Fitting priority (summary)

```
NOW:     M0 drift → M1 output → MNLE/SBI
SANITY:  per-event r(t) vs E[r|T]
LATER:   M2 V×D only if identifiable (pupil / pair / passive V≈0 prior)
LATER:   M3b C×G for passive (not literal “PIT” label)
```

---

## Starter sessions

| Group | Mouse | Days |
|-------|-------|------|
| Active Post | `6099_orange` | 12 or 13 |
| Passive During | `6099_red` | 6–10 |

---

## Supporting wiki

| Doc | Use |
|-----|-----|
| [wiki/02_EXPERIMENT_AND_DATA.md](./wiki/02_EXPERIMENT_AND_DATA.md) | Pointers to model/07 |
| [wiki/05_GLOSSARY.md](./wiki/05_GLOSSARY.md) | Terms |
| [wiki/06_AGENT_PLAYBOOK.md](./wiki/06_AGENT_PLAYBOOK.md) | Agent rules |
| [docs/MORPHINE_PR_EXPERIMENT.md](./docs/MORPHINE_PR_EXPERIMENT.md) | Short experiment ref |

---

## Collaborators

- **Elijah Paul (Eli):** drift model, MNLE/SBI, Tier 1–2 fitting  
- **Hansol Lim:** run_009, lockout rules, paradigm  

Meeting target: **Monday 10:00 CNC** (confirm locally). Eli may start fitting before meeting.

---

## OMCR (Claude Code)

| Doc | Content |
|-----|---------|
| [omcr/INSTALL.md](./omcr/INSTALL.md) | Install [OMCR](https://github.com/youngeun1209/oh-my-claudecode-research) |
| [omcr/INSTALL.ko.md](./omcr/INSTALL.ko.md) | 한국어 가이드 |
| [CLAUDE.md](./CLAUDE.md) | Project context for `@supervisor`, `@analysis-implementer`, … |
| [examples/opioid-pr-behavior/](./examples/opioid-pr-behavior/) | Memory preset |

**MATLAB repo:** [opioidaddiction-matlab](https://github.com/limserenahansol/opioidaddiction-matlab) — same OMCR scaffold.

---

## For agents

- **Claude Code:** [CLAUDE.md](./CLAUDE.md) + OMCR agents
- Implement [model/07](./model/07_DATA_RULES_AND_LIKELIHOOD.md) before any likelihood code
- Do **not** commit email threads
- Regenerate schematic: `python3 generate_logic_schematic.py`

**Code status:** spec + data rules + OMCR scaffold complete; `src/` not in repo yet.
