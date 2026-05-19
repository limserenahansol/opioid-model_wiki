# Agent Playbook

Instructions for LLMs working on this project.

## Before you edit

1. Read [../LLM_WIKI.md](../LLM_WIKI.md)
2. For data/schema: [02_EXPERIMENT_AND_DATA.md](./02_EXPERIMENT_AND_DATA.md) + [docs/MORPHINE_PR_EXPERIMENT.md](../docs/MORPHINE_PR_EXPERIMENT.md)
3. For equations: [03_COMPUTATIONAL_MODELS.md](./03_COMPUTATIONAL_MODELS.md)

## Do

- Keep **active vs passive** mechanisms distinct in text and code
- Treat passive withdrawal ↑ seeking as **hypothesis (PIT)**, not noise
- Use **staged models** (0 → 1 → 2 → 3)
- Write human-facing math as **plain text** in `.md` email/Word
- Regenerate `logic_flow_schematic.png` if logic diagram changes
- Match JSONL field names from experiment doc (`valid`, `requirement`, `tag`)
- Say clearly when code is **planned vs implemented**

## Don't

- Assume neural/imaging data exist
- Build full schedule POMDP as v1 default
- Conflate **relevance** with **journal quality** (that's the semantic-ranking project — different repo folder)
- Force one parameter set for both groups without justification
- Use unreadable LaTeX-only blocks in emails (`\rightarrow` stacks)

## Common tasks

| User ask | Action |
|----------|--------|
| “Draft email to CS colleague” | Start from `EMAIL_CS_COLLEAGUE.md`; plain equations |
| “Update grant aims” | Pull H0–H3 + passive patient angle from `01_SCIENCE` |
| “Implement parser” | Follow parent doc `JSONLSessionParser`; output lick table |
| “Fit drift model” | Model 0 in `03_COMPUTATIONAL_MODELS`; plan SBI interface |
| “Explain passive withdrawal PR” | PIT: C_t × G; cite predictions table |
| “Add figure” | Run `generate_logic_schematic.py` or extend it |

## Tone

- Scientific, precise, bilingual OK for this PI
- Proposals: complete sentences; hypotheses as testable claims
- Acknowledge **v1 limitations** (pause/count) without undermining project value

## File creation conventions

- New modeling code: prefer `morphine_pr_analysis/` at repo root (per parent doc), or `opioid_behavioral_model/src/` if user wants colocated — **ask if unclear**
- New wiki pages: add to `wiki/` and link from `LLM_WIKI.md`
- Do not create unsolicited README dumps outside this structure

## Cross-project note

`LLM_semanticRanking/` is a **separate** project (literature hybrid ranking). Do not merge unless user asks.
