# Claude Code — Opioid PR / AMM project (opioid-model_wiki)

> OMCR preset: `examples/opioid-pr-behavior/`. Install: [omcr/INSTALL.md](./omcr/INSTALL.md)

## Project context

- **Working title:** Addiction Motivational Model (AMM) for morphine progressive-ratio (PR) behavior
- **Field:** Behavioral neuroscience / computational psychiatry (rodent operant conditioning)
- **Target venue:** [TBD: grant / methods paper with CS collaborator]
- **Central hypothesis:** Mice do not explicitly represent the full PR schedule; opioid seeking is governed by a **low-dimensional latent motivational state** integrating reward, failure, pause, and withdrawal context. **Contingent** (active) vs **non-contingent** (yoked passive) morphine exposure produces distinct update architectures: active → `V_t × D_t` at re-exposure; passive → generalized `C_t × G_t` during withdrawal (not literal PIT experiment).
- **Research topic:** Head-fixed mouse PR with morphine vs water across Pre / During / Post / Withdrawal / Re-exposure; active vs passive (Days 6–10 yoked).
- **Datasets:**
  - **run_009** JSON (Dec 2025): [Drive JSON folder](https://drive.google.com/drive/folders/1tmojU4ahssZEvAdNGa5w6BfPAYERuYsV?usp=drive_link)
  - **MATLAB pipeline:** [opioidaddiction-matlab](https://github.com/limserenahansol/opioidaddiction-matlab) — longitudinal CSV, lick/pupil/motivation
  - Starter sessions: `6099_orange` day 12–13 (active Post); `6099_red` day 6–10 (passive During)
- **Narrative spine:** Seminar motifs (reward integrator, deficit integrator, engagement dynamics, context gain) → M0–M4 model ladder → SBI/MNLE fit (Eli) → link to MATLAB phenotypes → future neural

## Research stack

- **Canonical model spec (this repo):** `model/` — read `model/07`, `model/08`, `model/05` before any fit
- **LLM entry:** `LLM_WIKI.md`
- **MATLAB execution repo:** https://github.com/limserenahansol/opioidaddiction-matlab (`PIPELINE.md`, steps 01–07)
- **Rulebook script (MATLAB):** `step10_pr_licking_trajectory_phenotype/` if present; else `step04_lick/`, `step03_motivation/`
- **Figure / deck:** `logic_flow_schematic.png` (regenerate: `python3 generate_logic_schematic.py`)
- **BibTeX:** `paper/references.bib` · **Summary table:** `references.csv`
- **CrossRef email:** [TBD]
- **Collaborators:** Hansol Lim (behavior, data); Elijah Paul (drift model, MNLE/SBI)

## Language preference

- **Primary:** English for code, model docs, papers
- **Secondary:** Korean OK for notes to PI / internal summaries (`docs/GRANT_SUMMARY_KR_EN.md`)
- **Equations in email/Word:** plain text (`dx/dt = (α + r(t))/τ`), not raw LaTeX blocks

## OMCR agent routing

| Task | Agent |
|------|--------|
| Hypothesis, tier decisions, repo sync | `@supervisor` |
| M0–M1 Python, SBI, JSON ingest, lockout mask | `@analysis-implementer` |
| Methods / grant text from `model/` | `@paper-writer` |
| AMM schematic, parameter figures | `@figure-descriptor` |
| Identifiability, passive vs active claims | `@reviewer` |
| DDM / foraging / opioid citations | `@literature-curator` |

## Hard rules (never violate)

1. `day_index >= 4` only (drop FR days 1–2, unstable PR day 3)
2. Passive During days 6–10: **mask licks** in likelihood (unobserved); **rewards valid**
3. `PairID` random effect for group stats
4. `x_t` = hidden value; `λ_t = softplus(x_t)`; not lick rate
5. Fit **Tier 1 (M0–M1)** before M2–M3 unless identifiability documented
6. Do not add email threads to git; do not label passive model “PIT” in papers
