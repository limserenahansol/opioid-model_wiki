# State Architecture

Formal definition of latent variables in the **Addiction Motivational Model (AMM)**.

---

## State vector (full model)

At time t within a session:

```
S_t = { V_t, D_t, C_t, x_t, b_t }
```

| Symbol | Name | Domain | Primary group |
|--------|------|--------|---------------|
| `V_t` | Opioid reward / action–outcome value | ℝ | Active >> Passive |
| `D_t` | Deficit / withdrawal burden | ℝ≥0 | Both; ↑ in withdrawal |
| `C_t` | Pavlovian context / cue memory | ℝ≥0 | Passive (During) |
| `x_t` | Scalar engagement (M0–M1) | ℝ | Both (implementation) |
| `b_t` | Bout / pause regime (optional M4) | discrete | Both |

**Motivation index (M2):**

```
M_t = V_t − D_t + β_VD · V_t · D_t · 𝟙[withdrawal ∨ reexposure]
```

Interaction term optional; test against additive `V_t − D_t` only.

---

## Motif A — Reward integrator (`V_t`)

**Role:** slow memory that contingent morphine was worth seeking.

**Updates (discrete lick event k):**

```
V_{t+1} = V_t + η_V · R_event · g_V(phase, group) · 𝟙[valid lick ∧ rewarded]
V_{t+1} = V_{t+1} · (1 − δ_V)   # optional decay each trial
```

| Parameter | Meaning |
|-----------|---------|
| `η_V` | Learning rate for reward |
| `δ_V` | Passive decay (may be > active) |
| `g_V` | Context gain on reward input |

**Active prediction:** `η_V_active > η_V_passive`; `V` persists across Post/Re-exposure.

---

## Motif B — Deficit integrator (`D_t`)

**Role:** accumulated negative internal state from absence, failure, withdrawal.

**Updates:**

```
D_{t+1} = D_t + η_D · 𝟙[unrewarded lick] + η_W · 𝟙[phase = withdrawal]
D_{t+1} = D_{t+1} · (1 − δ_D) + ε_D(phase)
```

| Parameter | Meaning |
|-----------|---------|
| `η_D` | Failure / omission cost |
| `η_W` | Withdrawal-phase injection |
| `ε_D` | Baseline deficit offset by phase |

**Active prediction:** withdrawal raises `D` and **amplifies** cue-driven seeking via interaction with `V`.

---

## Motif C — Engagement dynamics

Not always a single scalar. Observable structure:

- lick **bouts** (short ILI)
- **pauses** between bouts
- **re-engagement** after pause

**M4 extension:** during pause of duration `Δ`, `x_{t+Δ} = x_t − κ·Δ` (decay) or separate discrete state `b_t ∈ {engage, pause}`.

---

## Motif D — Context modulation

Multiplicative gains on inputs:

```
g(phase, cue, group) ∈ (0, ∞)
```

Examples:

| Condition | Effect on model |
|-----------|-----------------|
| `phase = withdrawal` | ↑ `η_W`, ↑ `G_t` (passive) |
| `phase = reexposure` | ↑ `g_V` on morphine cue (active) |
| `group = passive` during During | `g_contingency → 0` for V updates |
| chamber / cue on | scales `C_t` drive |

---

## Passive-specific: `C_t` and `G_t`

**Context memory:**

```
C_{t+1} = C_t + η_C · 𝟙[opioid delivery ∧ phase = during]
```

**Generalized withdrawal gain:**

```
G_t = G_0 + η_G · 𝟙[phase = withdrawal]
```

**Seeking driver (M3):**

```
drive_passive(t) = C_t · G_t
```

Distinct from `drive_active(t) = f(V_t, D_t)`.

---

## Policy layer (all implementations)

```
ENGAGE  if  drive(t) > θ_eng
QUIT    if  drive(t) < θ_quit
LICK    if  ENGAGE and hazard(λ_t) > u ~ Uniform(0,1)
```

Hysteresis optional: `θ_quit < θ_eng` to capture persistence.

---

## Model reduction map

| Implementation | States used |
|----------------|-------------|
| M0 | `x_t` only (absorbs V,D heuristically) |
| M1 | `x_t` + output `λ_t` |
| M2 | `V_t`, `D_t` → `M_t` |
| M3 | `C_t`, `G_t` (passive); `V_t`, `D_t` (active) |
| M4 | M2 or M0 + pause decay `κ` |

See [03_MATHEMATICAL_MODELS.md](./03_MATHEMATICAL_MODELS.md).
