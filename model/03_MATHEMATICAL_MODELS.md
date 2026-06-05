# Mathematical Models M0–M4

Implementations of AMM.

**Fitting order (Hansol–Eli):** Lock **[M0 + M1](./08_FITTING_PRIORITY.md)** first → compare reward inputs → add M2/M3b only if [identifiable](./08_FITTING_PRIORITY.md#tier-3--dual-state-m2-identifiability-caveats). Apply [data rules](./07_DATA_RULES_AND_LIKELIHOOD.md) (lockout mask, `day_index ≥ 4`).

---

## Shared notation

| Symbol | Meaning |
|--------|---------|
| `t` | Continuous time or lick index |
| `T` | Current PR requirement (licks per reward) |
| `θ` | Disengagement threshold |
| `θ_eng` | Re-engagement threshold (≥ θ if hysteresis) |
| `Δt` | Inter-lick interval or simulation step |

---

## M0 — Single-state drift (minimal engagement)

**Latent:** `x_t` = hidden motivational value (**not** lick rate).

**Continuous form:**

```
dx/dt = (α + r(t)) / τ + (σ/τ) · ξ_t
```

**Discrete (per lick k):**

```
x_{k+1} = x_k + (α + r_k) / τ + ε_k,   ε_k ~ N(0, σ²/τ)
```

**Event input:**

```
r_k = +R    if lick k rewarded
r_k = −L    if lick k unrewarded
```

**PR expectation smoothing (optional, no explicit schedule in animal):**

```
r_k ≈ R · (1/T) − L · ((T−1)/T)
```

**Policy:**

```
state = ENGAGED  if x_k > θ_eng
state = QUIT     if x_k < θ_quit
```

| Parameter | Role | Active (prior) | Passive (prior) |
|-----------|------|----------------|-----------------|
| `R` | Reward bump | high | low |
| `L` | Failure cost | low | high |
| `τ` | Memory time constant | high | low |
| `α` | Baseline drift | phase-specific | ↑ withdrawal |
| `σ` | Noise | fit | fit |
| `θ_*` | Thresholds | low re-engage | high quit |

**Use:** first behavioral fit; group compares `R, τ, α` by phase.

---

## M1 — Hidden value with lick observation

Same `x_t` dynamics as M0. Observed behavior:

```
λ_k = softplus(x_k)           # wiki default
# or (Eli implementation — see model/09)
λ(x) = λ_max · sigmoid(β · x)
```

**Eli Tier-1 choices:** `λ_max = 1/P5_ILI` per session; `β = 2` fixed; `σ = 0` (deterministic drift).

**Constraint satisfied:** `x_k < 0` allowed; `λ_k > 0` always.

**Breakpoint:** session ends or enters QUIT when `x` crosses `θ_quit` for sustained window (if used; Eli fit may use continuous λ prediction vs ILI).

---

## M2 — Dual-axis addiction model (core)

**States:** `V_t`, `D_t`.

**Updates (per lick):**

```
V_{k+1} = V_k + η_V · R · g_V(phase) · 𝟙[rewarded ∧ valid]
D_{k+1} = D_k + η_D · L · g_D(phase) · 𝟙[unrewarded] + η_W · 𝟙[withdrawal]
```

**Motivation:**

```
M_k = V_k − D_k + β · V_k · D_k · 𝟙[phase ∈ {withdrawal, reexposure}]
```

**Policy:**

```
ENGAGED  if  M_k > θ_eng
```

**Lick output (optional):**

```
λ_k = λ_0 · softplus(M_k)
```

**Model comparison (H2):**

| Model | Predictor |
|-------|-----------|
| Null | constant |
| V-only | `V_k` |
| D-only | `D_k` |
| Additive | `V_k − D_k` |
| Interaction | `V_k − D_k + β V_k D_k` |

**Active re-exposure:** interaction term ↑ fit on days 17–18.

---

## M3 — Group-specific architecture (Tier 3–4, conditional)

> **Naming:** Do **not** call this “PIT” in manuscripts — use **generalized non-contingent motivation gain**. See [08_FITTING_PRIORITY.md](./08_FITTING_PRIORITY.md).

### Active (M3a) — requires M2 identifiable

```
drive_k = V_k − D_k + β_a · V_k · D_k · 𝟙[withdrawal ∨ reexposure]
```

### Passive (M3b) — generalized motivation

```
C_{k+1} = C_k + η_C · 𝟙[reward delivery during yoked/during]
G_k = G_base + η_G · 𝟙[withdrawal]
drive_k = C_k · G_k
```

**Likelihood note:** During passive lockout (days 6–10), update `C` from **injector/reward TTL**; mask licks ([07](./07_DATA_RULES_AND_LIKELIHOOD.md)).

**Post phase (passive):** optional transfer `V_k += η_transfer · C_k` when `valid` licks resume — tests **passive → instrumental** transition.

**H3 test:** M3b fits passive **withdrawal** sessions better than M2 with shared `V,D` only.

---

## M4 — Pause and re-engagement

Extend M0 or M2 between licks:

```
x_{k+1} = x_k · exp(−κ · pause_k) + update(lick_k)
```

Or bout HMM:

```
b_k ∈ {engage, pause}
P(pause → engage) = logistic(M_k − θ_reengage)
```

**Addresses:** effort count and pause structure (M0 limitation).

---

## Foraging analogy (do not implement as leave)

| Foraging | PR (AMM) |
|----------|----------|
| leave patch | quit / stop licking |
| stay | continue PR |
| patch value | `x_t` or `M_t` |
| travel cost | effort cost `L` |

---

## Simulation pseudocode (target `src/`)

```python
@dataclass
class AMMParams:
    R: float; L: float; tau: float; alpha: float; sigma: float
    eta_V: float; eta_D: float; eta_W: float; beta: float
    theta_eng: float; theta_quit: float

def step_m0(x, rewarded, p: AMMParams) -> float:
    r = p.R if rewarded else -p.L
    x += (p.alpha + r) / p.tau + rng.normal(0, p.sigma / p.tau)
    return x

def step_m2(V, D, rewarded, valid, phase, p) -> tuple[float, float]:
    if rewarded and valid:
        V += p.eta_V * p.R * g_V(phase)
    if not rewarded:
        D += p.eta_D * p.L
    if phase == "withdrawal":
        D += p.eta_W
  return V, D

def motivation(V, D, phase, p) -> float:
    M = V - D
    if phase in ("withdrawal", "reexposure"):
        M += p.beta * V * D
    return M
```

---

## Parameter vector for SBI

**M0/M1 per group × phase:** `{R, L, τ, α, σ, θ_eng, θ_quit}`  
**M2 add:** `{η_V, η_D, η_W, β}`  
**M3 passive add:** `{η_C, η_G, G_base}`  
**M3 transfer:** `{η_transfer}`

Hierarchical: population mean + mouse-level random effect on `R, τ` (optional).

Next: [04_GROUP_AND_PHASE.md](./04_GROUP_AND_PHASE.md) · [05_FITTING_WORKFLOW.md](./05_FITTING_WORKFLOW.md)
