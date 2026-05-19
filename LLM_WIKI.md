# LLM Wiki — Opioid Behavioral Modeling Project

**GitHub:** [github.com/limserenahansol/opioid-model_wiki](https://github.com/limserenahansol/opioid-model_wiki)

> **Audience:** Cursor agents, ChatGPT, collaborators writing code or grants.  
> **Read this file first** before editing models, parsers, or proposal text in this project.

---

## 30-second orientation

Head-fixed mice run a **Progressive Ratio (PR)** task across **18 days** with **morphine vs water** rewards and an **active vs yoked passive** manipulation (Days 6–10 only). The scientific goal is **not** “do mice understand the PR schedule?” but: **what low-dimensional latent motivational state** explains lick/seek persistence, withdrawal effects, and **different re-exposure** in active vs passive animals?

**v1 scope:** behavior-only models (drift / dual-state / passive PIT). **Neural data:** future extension after behavior fits.

---

## Wiki map

| Doc | Use when |
|-----|----------|
| [wiki/01_SCIENCE_AND_HYPOTHESES.md](./wiki/01_SCIENCE_AND_HYPOTHESES.md) | Framing, groups, hypotheses, predictions |
| [wiki/02_EXPERIMENT_AND_DATA.md](./wiki/02_EXPERIMENT_AND_DATA.md) | Timeline, JSONL fields, phases, fitting inputs |
| [wiki/03_COMPUTATIONAL_MODELS.md](./wiki/03_COMPUTATIONAL_MODELS.md) | Model 0–4, equations, parameters, fitting |
| [wiki/04_WORKFLOW_AND_ARTIFACTS.md](./wiki/04_WORKFLOW_AND_ARTIFACTS.md) | Pipeline, files, schematic, CS collaboration |
| [wiki/05_GLOSSARY.md](./wiki/05_GLOSSARY.md) | Terms (PR, PIT, V_t, passive yoked, etc.) |
| [wiki/06_AGENT_PLAYBOOK.md](./wiki/06_AGENT_PLAYBOOK.md) | Do / don’t, common tasks, tone for grants & email |

**Human proposal (bilingual):** [PROPOSAL_WORKFLOW_KR_EN.md](./PROPOSAL_WORKFLOW_KR_EN.md)  
**Experiment reference (in repo):** [docs/MORPHINE_PR_EXPERIMENT.md](./docs/MORPHINE_PR_EXPERIMENT.md)

---

## Core scientific claims (do not contradict)

1. **No explicit PR schedule representation** in v1 models — mice update an internal engagement/value state from **per-lick reward/nonreward**, not from “ratio = N.”
2. **Two slow axes** for active-like craving: **reward/action-value** (`V_t`) and **deficit/withdrawal** (`D_t`); re-exposure amplification is **interaction**, not exposure alone.
3. **Passive ≠ mere control:** patient-relevant **Pavlovian exposure → later instrumental vulnerability**; withdrawal ↑ seeking may be **PIT-like** (`C_t × G`), not consolidated opioid action value.
4. **PR ≠ foraging patch-leave:** single “patch”; decisions are **continue lick / pause / quit**, not switch patches.
5. **Hidden state `x_t` is not lick rate** — use `softplus(x_t)` or `sigmoid(x_t)` for observed licking.

---

## Model ladder (implementation order)

```
Model 0: single-state drift (x_t, colleague minimal)
    → Model 1: x_t → λ_t output (fix negative-rate issue)
        → Model 2: dual V_t, D_t (active re-exposure)
            → Model 3: passive C_t × G_withdrawal (PIT)
                → Model 4 (optional): pause / re-engagement
```

Fit with **simulation-based inference** (MNLE / MCMC / LAN), not hand-tuned plots only.

---

## Repository layout

```
opioid-model_wiki/                    ← GitHub repo root
├── LLM_WIKI.md                       ← you are here
├── README.md
├── wiki/                             ← modular wiki pages
├── docs/MORPHINE_PR_EXPERIMENT.md
├── PROPOSAL_WORKFLOW_KR_EN.md
├── EMAIL_CS_COLLEAGUE.md / .docx
├── generate_logic_schematic.py
└── logic_flow_schematic.png
```

**Status (code):** Wiki + proposal ready; **parsers and fitters** planned under future `src/` (see [wiki/04_WORKFLOW_AND_ARTIFACTS.md](./wiki/04_WORKFLOW_AND_ARTIFACTS.md)).

---

## Experimental timeline (quick ref)

| Days | Phase | Reward | Active | Passive (yoked Days 6–10) |
|------|-------|--------|--------|---------------------------|
| 1–2 | Habituation | Sucrose | FR1/FR3 | Same |
| 3–5 | Pre | Water | PR | PR |
| 6–10 | During | Morphine | PR (contingent) | Yoked (licks `valid: false`) |
| 11–13 | Post | Morphine | PR | PR |
| 14–16 | Withdrawal | Water | PR | PR |
| 17–18 | Re-exposure | Morphine | PR | PR |

**Primary behavioral readout:** `requirementLast` (PR breakpoint), lick bouts, re-engagement after pause.

---

## Hypotheses (one line each)

| ID | EN |
|----|-----|
| H0 | Seeking = low-D latent state integrating reward, effort, failure, pause — not full PR schema |
| H1 | Contingent opioid **reshapes update rules & thresholds** (active > persistent) |
| H2 | Re-exposure needs **V × withdrawal**, not V alone |
| H3 | Passive withdrawal = **Pavlovian context × generalized gain**, not strong V_t |

---

## For agents: default behaviors

- Prefer **staged model comparison** over jumping to full POMDP.
- When writing equations for humans, use **plain text** in email/Word (`dx/dt = (α + r(t))/τ`), not raw LaTeX blocks.
- Preserve **bilingual** labels when user works in KO+EN (see proposal).
- Cite experiment details from [docs/MORPHINE_PR_EXPERIMENT.md](./docs/MORPHINE_PR_EXPERIMENT.md) for JSONL schema.
- Do **not** claim neural results until data exist.
- Regenerate schematic: `python3 generate_logic_schematic.py` from `opioid_behavioral_model/`.

**Detailed playbook:** [wiki/06_AGENT_PLAYBOOK.md](./wiki/06_AGENT_PLAYBOOK.md)

---

## Key collaborators & context

- **CS colleague:** drift-like PR fit, MNLE/SBI; agreed on latent state framing; meeting CNC Thu AM or Fri.
- **Grant context:** Specific Aims may include behavior-only computational layer before neural Aim.
- **Related framing:** Seminar motifs A–D (reward integrator, deficit integrator, seeking dynamics, context gain).

---

*Last aligned with proposal draft in `opioid_behavioral_model/` and 18-day PR design in parent documentation.*
