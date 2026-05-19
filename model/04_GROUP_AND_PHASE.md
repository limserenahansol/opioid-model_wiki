# Group × Phase — Model Instantiation

How AMM parameters and active states change across the 18-day paradigm.

---

## Timeline

| day_index | Phase | Reward | Group manipulation | Analysis |
|-----------|-------|--------|---------------------|----------|
| 1–2 | Habituation | Sucrose | FR | **Exclude** |
| 3 | Pre (PR day 1) | Water | Both PR | **Exclude** |
| 4–5 | Pre | Water | Both PR | **Focus day 4** |
| 6–10 | During | Morphine | **Active vs yoked passive** | **Focus day 7**; lockout passive |
| 11–13 | Post | Morphine | Both active PR | **Focus 12–13** (`6099_orange`) |
| 14–16 | Withdrawal | Water | Both active PR | **Focus day 15** |
| 17–18 | Re-exposure | Morphine | Both active PR | **Focus day 18** |

**Rule:** `day_index ≥ 4` only — see [07_DATA_RULES_AND_LIKELIHOOD.md](./07_DATA_RULES_AND_LIKELIHOOD.md).

---

## Phase × expected latent dynamics

| Phase | `V_t` (active) | `D_t` | `C_t` (passive) | `G_t` (passive) | PR prediction |
|-------|----------------|-------|-----------------|-----------------|---------------|
| Pre | low (water) | low | low | low | baseline |
| During | **↑↑** contingent | moderate | **↑** pairing | low | active > passive breakpoint |
| Post | consolidated | low | slow ↑ V transfer | low | active high |
| Withdrawal | held in memory | **↑↑** | stable C | **↑** | passive ↑ possible (C×G) |
| Re-exposure | drives seeking | high then relief | C persists | ↓ | active rebound >> passive |

---

## During (Days 6–10) — critical divergence

| | Active | Passive |
|---|--------|---------|
| Lick `valid` / TTL | observed | **lockout: mask from lick likelihood** |
| Reward / injector TTL | observed | **observed (yoked)** → valid `r(t)` |
| `V` update | `η_V · R` on rewarded valid licks | weak / blocked on licks; reward events OK |
| `C` update | secondary | **η_C on morphine delivery** |
| Starter mouse | — | `6099_red` days 6–10 |
| Model | M0–M1 Tier 1 | same; no lick likelihood in lockout window |

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
