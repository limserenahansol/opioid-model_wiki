# Agent Playbook

## Read order

1. [../LLM_WIKI.md](../LLM_WIKI.md)
2. [../model/07_DATA_RULES_AND_LIKELIHOOD.md](../model/07_DATA_RULES_AND_LIKELIHOOD.md) **before any likelihood code**
3. [../model/08_FITTING_PRIORITY.md](../model/08_FITTING_PRIORITY.md)
4. [../model/03_MATHEMATICAL_MODELS.md](../model/03_MATHEMATICAL_MODELS.md)
5. [../model/05_FITTING_WORKFLOW.md](../model/05_FITTING_WORKFLOW.md)

## Do

- Implement **AMM M0–M4** from `model/` specs
- Keep active vs passive **separate parameter sets** where theory requires
- Parse JSONL per [docs/MORPHINE_PR_EXPERIMENT.md](../docs/MORPHINE_PR_EXPERIMENT.md)
- Add code under `src/` matching [model/05](../model/05_FITTING_WORKFLOW.md) layout

## Don't

- Add **email** or chat transcripts to the repo
- Treat `x_t` as lick rate
- Treat passive lockout licks as **zero** (must be **masked**)
- Include days 1–3 in fits
- Fit separate V_t and D_t without identifiability checks
- Label passive model “PIT” in publication text
- Skip M0–M1 before M2
- Claim neural results without data

## Common tasks

| Task | Location |
|------|----------|
| Add equation / state | `model/02`, `model/03` |
| Change group logic | `model/04` |
| Add hypothesis test | `model/06` |
| Parser | `src/ingest/` (create) |
| SBI fitter | `src/fit/` (create) |

## Cross-project

`LLM_semanticRanking/` is unrelated (literature ranking).
