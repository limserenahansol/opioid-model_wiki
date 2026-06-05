# Eli implementation status (Tier 1 MLE)

**Source:** Eli Paul update (2026). Living doc — update when new fits land.

**Wiki maintainer:** Hansol (periodic); **model code:** Eli.

---

## Model structure (current)

### Latent state (drift)

Between-lick continuous drift:

```
dx = α dt + σ dW
```

**Event jumps** (per lick; implied by fitted `R`, `L`):

```
x ← x + R   if rewarded lick
x ← x − L   if unrewarded lick
```

(Confirm in Eli's code whether jumps are additive on top of `α dt` integration.)

### Observation (M1 — sigmoid)

```
λ(x) = λ_max · sigmoid(β · x)
```

`x` is hidden motivation; **not** lick rate.

---

## Parameters (current fit)

### Fixed (may change later)

| Parameter | Status | Value |
|-----------|--------|-------|
| `λ_max` | fixed **per session** | `1 / P5_ILI` (inverse of 5th-percentile inter-lick interval) |
| `β` | fixed | `2.0` |
| `σ` | fixed | `0.0` (deterministic; no diffusion noise yet) |

### Free — MLE **per mouse** (log space for `R`, `L`)

| Parameter | Bounds | Notes |
|-----------|--------|-------|
| `x0` | (−6, 6) | Initial motivation at session start |
| `α` | (−0.05, −1e−5) | Drift; **forced negative** → baseline motivation decays over session |
| `R` | (e⁻⁴, e⁴) ≈ (0.02, 55) | Reward jump; fit in log space |
| `L` | (e⁻⁶, e²) ≈ (0.002, 7.4) | Penalty jump; fit in log space |

---

## Alignment with wiki spec

| Wiki (AMM) | Eli (current) | Match? |
|------------|---------------|--------|
| Hidden `x`, not lick rate | yes | ✓ |
| `λ = f(x)` output (M1) | sigmoid, not softplus | ✓ (equivalent role) |
| Per-lick `R` / `L` | fitted | ✓ |
| `σ > 0` stochastic | `σ = 0` for now | partial — Tier 1 deterministic |
| `τ` time constant | not separate; embedded in `α dt`? | simplify / clarify with Eli |
| SBI / MNLE | **MLE per mouse** (first pass) | ✓ pragmatic Tier 1 |
| Hierarchical / PairID RE | **planned** — Gaussian population means; correlation TBD | next step |
| Passive lockout mask (model/07) | confirm applied in Eli likelihood | **verify** |

---

## Planned extensions (Eli)

1. **`σ > 0`** — stochastic diffusion later
2. **Hierarchical model** — parameters as draws from group means (Gaussian); challenge: correlations, degeneracy
3. **Neural mapping** — goal: model parameters represented in brain (depends on neural data collection)

---

## Scientific read (for comparison across groups)

With **`α < 0` fixed in sign**: session-wide motivational decay; `R`/`L` shape how reward history perturbs `x`. Group/phase differences should appear in **`x0`, `α`, `R`, `L`** posteriors or MLE estimates once hierarchical structure is added.

**Active vs passive predictions (unchanged):** active → larger `R`, possibly slower effective decay; passive During → reward jumps without contingent lick likelihood (mask); compare after lockout-aware fit.

---

## Open questions for next Eli sync

1. Are `R`/`L` applied on every observed lick only (lockout masked for passive)?
2. One `(x0, α, R, L)` per mouse per session, or pooled across sessions?
3. When will starter mice (`6099_orange` Post, `6099_red` During) first fits be shareable?
4. Path to **PairID** hierarchical — population mean on which parameters first?

---

## Status

| Item | State |
|------|--------|
| Tier 1 deterministic MLE | **In progress** (Eli) |
| Wiki updated with this doc | yes |
| Group comparison results | pending |
| Neural link | future |
