# Data Rules & Likelihood (run_009 cohort)

Formal analysis rules for fitting AMM to **run_009** (Dec 2025). These govern what enters the likelihood — not optional QC.

**Data folder (JSON extract):** [Google Drive — JSON cohort](https://drive.google.com/drive/folders/1tmojU4ahssZEvAdNGa5w6BfPAYERuYsV?usp=drive_link)

---

## 1. Day inclusion

| Rule | Detail |
|------|--------|
| **Exclude** | `day_index ∈ {1, 2, 3}` |
| **Reason** | Days 1–2 = Fixed Ratio (habituation), not PR; day 3 = first PR day (unstable) |
| **Analyze** | `day_index ≥ 4` only |

### Phase “stable” days (optional focus)

First day of each phase can be noisy. For phase-level summaries, prefer **second day of phase**:

| Phase | Preferred `day_index` |
|-------|------------------------|
| Pre | 4 |
| During | 7 |
| Post | 12 |
| Withdrawal | 15 |
| Re-exposure | 18 |

---

## 2. Passive During lockout (critical for likelihood)

**Window:**

```
day_index ∈ {6, 7, 8, 9, 10}
AND isPassive == 1
AND Period == 'During'
```

| Channel | Treatment |
|---------|-----------|
| **Lick_TTL** | Hardware-locked / forced invalid — **does not reflect real licking** |
| **Likelihood** | **Mask** lick observations — treat as **unobserved**, **not as zero** |
| **Reward / Injector_TTL** | **Valid** — passive rewards are yoked from active partner |
| **r(t) from rewards** | **Valid** — update latent state from reward timestamps |

```python
def lick_observed(row) -> bool:
    if row.isPassive and row.Period == "During" and row.day_index in (6, 7, 8, 9, 10):
        return False  # masked — not in lick likelihood
    return True

def reward_observed(row) -> bool:
    return True  # both groups; yoked delivery during passive lockout
```

**Model implication:** During passive lockout, fit **reward-driven updates** to `x_t` (or `V_t`) without requiring observed licks. Do not impute lick rate = 0.

---

## 3. Yoked pairs

| Field | Use |
|-------|-----|
| `PairID` | Links active ↔ passive partner |
| **Statistics** | Treat **pair** as random effect for group-level inference |
| **r(t)** | Passive reward times follow partner; valid for both |

---

## 4. Reward vs response in the model

| Signal | Role in AMM |
|--------|-------------|
| Rewarded lick (active, valid) | `r_k = +R` and lick likelihood |
| Unrewarded lick (observed) | `r_k = −L` and lick likelihood |
| Reward delivery (injector), no lick | `r_k = +R` on state only; **no** lick term |
| Masked lick window | State may still get `r` from injector; **skip** `P(lick)` |

---

## 5. Starter sessions (first fits)

Keep Eli’s “one JSON per type” principle; expand for validation later.

| Type | Mouse | Days | Phase |
|------|-------|------|-------|
| **Active PR** | `6099_orange` | 12 or 13 | Post |
| **Passive PR** | `6099_red` | 6, 7, 8, 9, or 10 | During |

Minimum for pipeline smoke test: **one active Post + one passive During** (non-lockout lick days still need masking on 6–10 for passive).

---

## 6. Two reward-input modes (sanity check)

Fit **side by side** on the same sessions:

| Mode | Update |
|------|--------|
| **Per-event** | `r_k = +R` or `−L` on each observed lick / reward event |
| **Smoothed PR** | `E[r \| T] = R·(1/T) − L·((T−1)/T)` on each lick in trial with requirement `T` |

**Expectation:** If model is well-specified, shared parameters (`τ`, `α`, `σ`) should be **similar** across modes; smoothed mode links to Eli’s closed-form noise-free solution (exponential integral) for intuition.

---

## 7. Empirical motivation: within-trial lick slowing

Observed: **lick rate slows within trial** as trial index increases (distinct from between-trial effects). Supports a **drifting internal value** under diminishing reward probability — not independent licks only.

Feature for validation / summaries:

- lick rate vs position within trial
- compare to simulated `λ_k` from M1

---

## 8. Manifest & metadata

Use mouse ID manifest for:

- `Active` vs `Passive`
- `PairID`
- cohort / run id (`run_009`)

**MATLAB rulebook (constants):** `opioidaddiction-matlab` → `step10_pr_licking_trajectory_phenotype/run_step10_pr_lick_trajectory_phenotype.m`

See [../docs/DATA_SOURCES.md](../docs/DATA_SOURCES.md).

---

## 9. Checklist before SBI

- [ ] `day_index >= 4`
- [ ] Passive During lockout: licks masked, rewards kept
- [ ] `PairID` in hierarchy for group stats
- [ ] Per-event vs smoothed `r` compared
- [ ] Starter sessions run end-to-end on M0 → M1

Next: [05_FITTING_WORKFLOW.md](./05_FITTING_WORKFLOW.md) · [08_FITTING_PRIORITY.md](./08_FITTING_PRIORITY.md)
