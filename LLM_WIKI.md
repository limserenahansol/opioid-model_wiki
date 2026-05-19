# LLM Wiki — Addiction Motivational Model (AMM)

**GitHub:** [github.com/limserenahansol/opioid-model_wiki](https://github.com/limserenahansol/opioid-model_wiki)

> **Read `model/` first.** This repo is a **computational addiction model spec**, not email or grant drafts.

---

## Canonical model documentation

| # | Document | Content |
|---|----------|---------|
| — | [model/00_OVERVIEW.md](./model/00_OVERVIEW.md) | AMM index |
| 1 | [model/01_LOGIC_FLOW.md](./model/01_LOGIC_FLOW.md) | Question → motifs → groups → behavior |
| 2 | [model/02_STATE_ARCHITECTURE.md](./model/02_STATE_ARCHITECTURE.md) | V, D, C, G, x; motifs A–D |
| 3 | [model/03_MATHEMATICAL_MODELS.md](./model/03_MATHEMATICAL_MODELS.md) | **M0–M4 equations & parameters** |
| 4 | [model/04_GROUP_AND_PHASE.md](./model/04_GROUP_AND_PHASE.md) | Active vs passive × 18-day phases |
| 5 | [model/05_FITTING_WORKFLOW.md](./model/05_FITTING_WORKFLOW.md) | JSONL → SBI → model comparison |
| 6 | [model/06_PREDICTIONS.md](./model/06_PREDICTIONS.md) | H0–H4 falsifiable tests |

---

## Supporting wiki

| Doc | Use |
|-----|-----|
| [wiki/01_SCIENCE_AND_HYPOTHESES.md](./wiki/01_SCIENCE_AND_HYPOTHESES.md) | Narrative science (points to `model/`) |
| [wiki/02_EXPERIMENT_AND_DATA.md](./wiki/02_EXPERIMENT_AND_DATA.md) | JSONL, phases, data columns |
| [wiki/05_GLOSSARY.md](./wiki/05_GLOSSARY.md) | Terms |
| [wiki/06_AGENT_PLAYBOOK.md](./wiki/06_AGENT_PLAYBOOK.md) | Coding rules |
| [docs/MORPHINE_PR_EXPERIMENT.md](./docs/MORPHINE_PR_EXPERIMENT.md) | Experiment reference |

---

## Model in one diagram

```
Normative Q → Motifs (V, D, C, engagement, context gain)
           → Group architecture (active: V×D  |  passive: C×G)
           → Implementations M0→M1→M2→M3→M4
           → Fit on lick data (SBI)
           → Test H0–H4
```

**Implementations:** M0 drift `x_t` → M1 `λ=f(x)` → M2 `V_t,D_t` → M3 passive `C×G` → M4 pause.

---

## Core rules (do not contradict)

1. No explicit full-PR-schema representation in v1.
2. `x_t` is hidden value; lick rate = `softplus(x_t)` or logistic.
3. Active re-exposure: **V × D interaction**, not exposure alone.
4. Passive withdrawal ↑ seeking: **C × G** (PIT-like), not strong V.
5. PR task = continue / pause / quit (not foraging patch-leave).

---

## Repository layout

```
opioid-model_wiki/
├── model/              ← CANONICAL addiction model
├── wiki/               ← science, data, glossary, agents
├── docs/               ← experiment + grant summary
├── LLM_WIKI.md         ← this file
├── logic_flow_schematic.png
└── src/                ← (planned) code from model/05
```

---

## For agents

- Implement from [model/03_MATHEMATICAL_MODELS.md](./model/03_MATHEMATICAL_MODELS.md) and [model/05_FITTING_WORKFLOW.md](./model/05_FITTING_WORKFLOW.md).
- Do **not** add email threads to the repo.
- Regenerate figure: `python3 generate_logic_schematic.py`

**Code status:** spec complete; `src/` not yet built.
