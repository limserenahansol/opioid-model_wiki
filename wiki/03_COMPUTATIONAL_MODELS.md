# Computational Models

Full proposal: [../PROPOSAL_WORKFLOW_KR_EN.md](../PROPOSAL_WORKFLOW_KR_EN.md)

## Design principle

| Do | Don't |
|----|-------|
| Hidden latent **engagement value** updated by events | Assume mouse computes global PR ratio |
| Separate `x_t` from **observed lick rate** | Let lick rate go negative |
| Compare models by **held-out sessions / AIC** | Hand-tune only until “looks OK” |
| Group-specific parameters (active vs passive) | Single parameter set forced across groups |

## Model 0 — Single-state drift (colleague start)

**State:** `x_t` = hidden engagement / motivational value

```
dx/dt = (α + r(t)) / τ  +  (σ/τ) · noise
```

**Per-lick input:**

```
r(t) = +R   if rewarded lick
r(t) = −L   if unrewarded lick
```

**PR-smoothed (optional):**

```
r(t) ≈ R·(1/T) − L·((T−1)/T)
```

**Policy:** continue if `x_t > θ`; disengage if below threshold.

| Param | Meaning | Active (expect) | Passive (expect) |
|-------|---------|-----------------|------------------|
| R | Reward bump | ↑ | ↓ |
| L | Failure cost | ↓ or slower | ↑ |
| τ | Memory time constant | ↑ (slower decay) | ↓ |
| α | Baseline drift | phase-dependent | ↑ in withdrawal (generalized) |
| σ | Noise | fit | fit |
| θ | Quit / re-engage threshold | ↓ re-engage | ↑ quit |

## Model 1 — Hidden value → lick output

```
λ_t = softplus(x_t)     # lick rate
# or
P(lick_t) = logistic(x_t)
```

Fixes: internal value may be negative; observation stays ≥ 0.

## Model 2 — Dual-state (core addiction)

```
V_t  ← opioid reward / action value   (reward, contingent history)
D_t  ← deficit / withdrawal burden    (failure, pause, withdrawal phase)
M_t  = V_t − D_t
seek / engage if M_t > θ
```

**Active re-exposure:** high `V_t` (prior contingency) × high `D_t` (withdrawal) → amplified seeking.

**Fit test:** V + D + interaction > V-only on re-exposure sessions.

## Model 3 — Passive PIT / context gain

```
Seeking_t ∝ C_t × G_withdrawal
```

- `C_t`: Pavlovian cue/context memory (passive During)
- `G_withdrawal`: generalized motivational gain

**Contrast active:**

```
Seeking_t ∝ V_t × W_t
```

Use to explain **passive withdrawal ↑ PR** without strong `V_t`.

## Model 4 — Pause / re-engagement (optional)

- During pause: decay `x_t` or `M_t`
- After reward: short positive bump
- Addresses discrete **effort count + pause** limitation of pure drift

## Fitting

**Preferred:** simulation-based inference — MNLE, MCMC, LAN.

**Inputs:** lick-level event stream + group/phase labels.

**Outputs:** posterior / MLE parameters per group; simulated vs observed engagement; model comparison table.

## Foraging paper relation

- Foraging DDM: **stay vs leave patch**
- This PR task: **no patch switch** — same as single patch; model **lick / pause / quit**, not leave decision.

## Implementation pseudocode (target)

```python
# Intended structure — NOT YET IN REPO
def update_x(x, rewarded, params):
    r = params.R if rewarded else -params.L
    x += (params.alpha + r) / params.tau + noise(params.sigma)
    return x

def lick_rate(x):
    return softplus(x)

def simulate_session(licks, rewards, params):
    ...
```

Agents implementing: add `src/modeling/` with tests on one JSONL session first.
