# Predictions & Hypothesis Tests

Map scientific hypotheses to **model comparisons** and **observable outcomes**.

---

## H0 — Latent state (not PR schema)

**Claim:** Behavior arises from integrating reward, failure, pause — not explicit schedule.

**Test:**

| Comparison | Expect |
|------------|--------|
| M0 vs independent-lick model | M0 ↑ breakpoint likelihood |
| M0 with smoothed `r(T)` vs without | similar if animal ignores T |

**Fail if:** only trial-index model fits, not history-dependent M0.

---

## H1 — Contingency reshapes update rules

**Claim:** Active During changes `η_V`, `τ`, `θ_eng` vs passive.

**Test:**

| Parameter | Active > Passive? |
|-----------|-------------------|
| `R`, `η_V` | yes |
| `τ` | yes (slower decay) |
| `θ_eng` (re-exposure) | lower (easier re-engage) |

**Data:** Post, Re-exposure sessions (both groups active PR).

---

## H2 — V × D interaction at re-exposure

**Claim:** Re-exposure seeking needs interaction, not V alone.

**Test:**

```
ΔAIC = AIC(V-only) − AIC(V − D + β·V·D)
```

**Expect:** ΔAIC > 0 on days 17–18, **active** mice.

**Behavior:** breakpoint correlates with prior-session `V` estimate × withdrawal `D`.

---

## H3 — Passive PIT (C × G)

**Claim:** Passive withdrawal ↑ PR via `C_t · G_t`, not high `V_t`.

**Test:**

| Model | Passive withdrawal sessions |
|-------|----------------------------|
| M2 shared V,D | poor fit |
| M3b C×G | better fit |
| M3b + transfer | better Post learning |

**Behavior:** passive withdrawal breakpoint ↑ without During `valid` licks.

---

## H4 — Threshold / re-engagement

**Claim:** Abstinence lowers `θ_eng` (active) or raises `G` (passive).

**Measure:** latency to first lick; re-engagement after long pause.

**Model:** M4 if M0 misses pause structure.

---

## Future neural (after behavior fit)

| Latent | Neural prediction |
|--------|-------------------|
| `V_t` | slow drift axis correlated with reward history (active) |
| `D_t` | withdrawal-specific gain modulation |
| Passive `C_t` | cue/context response without action-value axis |

**Not in v1 behavior repo.**

---

## Summary matrix

| ID | Model test | Key phase | Group |
|----|------------|-----------|-------|
| H0 | M0 > memoryless | all | both |
| H1 | param shift | post, reex | active > passive |
| H2 | interaction term | reexposure | active |
| H3 | M3b > M2 | withdrawal | passive |
| H4 | M4 pause | all | both |

See [01_LOGIC_FLOW.md](./01_LOGIC_FLOW.md) for conceptual diagram.
