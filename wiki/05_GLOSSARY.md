# Glossary

Bilingual where useful for this lab.

| Term | EN | KO / notes |
|------|-----|------------|
| **PR** | Progressive Ratio — effort requirement increases after each earned reward | 점진적 비율 과제 |
| **Breakpoint** | `requirementLast` — max ratio achieved in session | 세션 최대 요구 lick 수 |
| **Active** | Mouse controls morphine delivery via operant | 능동(자가투여)군 |
| **Passive / yoked** | Rewards replayed from paired active; licks not counted Days 6–10 | 패시브(요크)군 |
| **During phase** | Days 6–10; morphine; group manipulation | 투여 기간 |
| **Withdrawal** | Days 14–16; water reward; no morphine | 금단 기간 |
| **Re-exposure** | Days 17–18; morphine returns | 재노출 |
| **V_t** | Opioid reward / action–outcome value state | opioid 가치 적분 상태 |
| **D_t** | Deficit / withdrawal burden state | 결핍·금단 적분 상태 |
| **x_t** | Single hidden engagement value (Model 0–1) | 잠재 참여 가치 |
| **PIT** | Pavlovian-instrumental transfer-like invigoration | PIT 유사 일반화 동기 |
| **C_t** | Pavlovian context / cue memory (passive model) | 맥락·단서 기억 |
| **Contingency** | Action causes outcome | 행동–결과 연속성 |
| **SBI** | Simulation-based inference (MNLE, MCMC, LAN) | 시뮬레이션 기반 추론 |
| **Drift–diffusion** | Continuous latent variable with noise + drift | 드리프트–확산 |
| **ILI** | Inter-lick interval | lick 간격 |
| **Bout** | Cluster of licks with short ILIs | lick bout |
| **Motif A–D** | Seminar framework: reward, deficit, seeking rhythm, context | 세미나 4모티프 |
| **requirementLast** | JSONL-derived motivation index | PR breakpoint 변수명 |

## Abbreviations (pharmacology)

| Abbrev | Test |
|--------|------|
| TI | Tail immersion |
| TST | Tail suspension |
| HP | Hotplate |

Not central to v1 computational fit.

## Common confusions (avoid)

| Wrong | Right |
|-------|-------|
| “Passive has no learning” | Pavlovian/context learning; weak instrumental V_t |
| “x_t = lick rate” | x_t hidden; λ_t = f(x_t) |
| “Withdrawal ↑ = craving only in active” | Passive may ↑ via PIT-like gain |
| “Fit full PR schedule” | v1 integrates local reward/nonreward only |
