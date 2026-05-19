# Group × Phase — Model Instantiation

How AMM parameters and active states change across the 18-day paradigm.

---

## Timeline

| Days | Phase | Reward | Group manipulation |
|------|-------|--------|-------------------|
| 1–2 | Habituation | Sucrose | None |
| 3–5 | Pre | Water | Both active PR |
| 6–10 | During | Morphine | **Active vs yoked passive** |
| 11–13 | Post | Morphine | Both active PR |
| 14–16 | Withdrawal | Water | Both active PR |
| 17–18 | Re-exposure | Morphine | Both active PR |

---

## Phase × expected latent dynamics

| Phase | `V_t` (active) | `D_t` | `C_t` (passive) | `G_t` (passive) | PR prediction |
|-------|----------------|-------|-----------------|-----------------|---------------|
| Pre | low (water) | low | low | low | baseline |
| During | **↑↑** contingent | moderate | **↑** pairing | low | active > passive breakpoint |
| Post | consolidated | low | slow ↑ V transfer | low | active high |
| Withdrawal | held in memory | **↑↑** | stable C | **↑** | passive ↑ possible (PIT) |
| Re-exposure | drives seeking | high then relief | C persists | ↓ | active rebound >> passive |

---

## During (Days 6–10) — critical divergence

| | Active | Passive |
|---|--------|---------|
| Lick `valid` | true | **false** |
| `V` update | `η_V · R` on rewarded valid licks | **blocked** or tiny |
| `C` update | secondary | **η_C on morphine delivery** |
| PR breakpoint | normal progression | disrupted / lower |
| Model | M2 active params | M3b or M0 with `R≈0` for V |

---

## Withdrawal — mechanistic split

**Active:** violated opioid expectation → `D_t` rises → same chamber/cue with water reward → generalized suppression OR cue-triggered **amplification** if morphine-associated cues present → test `β·V·D`.

**Passive:** no strong `V_t` → elevated PR if `C_t · G_t` explains data → **not** mislabeled active craving.

---

## Re-exposure — mechanistic split

**Active:** `V_t` (prior contingency) × `D_t` (abstinence) → high `M_t` → low `θ_eng` → more licks / higher breakpoint.

**Passive:** weak `V_t`; possible **extinction** from withdrawal → lower reinstatement than active.

---

## Passive → instrumental transition (translational)

**Hypothesis:** After During, passive mice lack `V` but retain `C`. When Post gives valid licks again:

```
V_{post} starts low but η_transfer · C_t > 0
```

**Test:** Post-day learning rate `η_V_passive` vs `η_V_active`; breakpoint convergence or permanent gap.

---

## Phase indicators for code

```python
PHASE_ORDER = ["habituation", "pre", "during", "post", "withdrawal", "reexposure"]

def g_V(phase: str, group: str) -> float:
    if phase == "during" and group == "passive":
        return 0.0  # no contingency for V
    if phase == "reexposure":
        return g_reex  # fit
    return 1.0

def inject_withdrawal(D, phase, eta_W):
    if phase == "withdrawal":
        return D + eta_W
    return D
```

---

## Observable signatures (qualitative)

| Signature | Active | Passive |
|-----------|--------|---------|
| Breakpoint During | high | low / flat PR |
| Breakpoint Withdrawal | variable | **can increase** |
| Breakpoint Re-exposure | **highest** | moderate / below active |
| Lick bout structure | organized seek–consume | more variable |

Next: [05_FITTING_WORKFLOW.md](./05_FITTING_WORKFLOW.md) · [06_PREDICTIONS.md](./06_PREDICTIONS.md)
