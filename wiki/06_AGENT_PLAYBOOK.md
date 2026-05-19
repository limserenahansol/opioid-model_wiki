# Agent Playbook

## Read order

1. [../LLM_WIKI.md](../LLM_WIKI.md)
2. [../model/00_OVERVIEW.md](../model/00_OVERVIEW.md)
3. [../model/03_MATHEMATICAL_MODELS.md](../model/03_MATHEMATICAL_MODELS.md) before writing code
4. [../model/05_FITTING_WORKFLOW.md](../model/05_FITTING_WORKFLOW.md) for pipeline

## Do

- Implement **AMM M0–M4** from `model/` specs
- Keep active vs passive **separate parameter sets** where theory requires
- Parse JSONL per [docs/MORPHINE_PR_EXPERIMENT.md](../docs/MORPHINE_PR_EXPERIMENT.md)
- Add code under `src/` matching [model/05](../model/05_FITTING_WORKFLOW.md) layout

## Don't

- Add **email** or chat transcripts to the repo
- Treat `x_t` as lick rate
- Skip M0 baseline before M2
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
