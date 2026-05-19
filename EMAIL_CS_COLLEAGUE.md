# Email draft — CS colleague (modeling PR / opioid seeking)

**Subject:** Re: Modeling active vs passive opioid seeking — drift model, extensions, and meeting

---

Hi [Name],

Thank you again — this is very helpful, and your framing aligns closely with what I want to test.

## Agreement

Conceptually, I agree that mice may not explicitly represent the full PR schedule. A drift-like model in which each lick updates an internal valuation / engagement state is a good **first implementation**. This matches our hypothesis that opioid seeking reflects a **low-dimensional latent motivational state**, not independent trial-by-trial responses.

## One clarification: treat x as hidden value, not lick rate

Since x can become negative, I suggest we treat **x_t as a hidden motivational value** and model observed licking as an output. For example:

**State update (continuous-time form):**

    dx/dt = (α + r(t)) / τ  +  (σ/τ) · noise

**Observed behavior (one option):**

    lick rate λ_t = softplus(x_t)

    — or —

    P(lick at t) = logistic(x_t)

Then x may fall below zero without implying a negative lick rate. Crossing a lower threshold can still mean disengagement or “give up.”

## Reward input

Per-lick update:

    r(t) = +R   if rewarded lick
    r(t) = −L   if unrewarded lick

Smoothed PR-stage approximation (when T is the current requirement):

    r(t) ≈ R·(1/T) − L·((T−1)/T)

As PR progresses, unrewarded licks become more frequent, so expected value drifts down — without assuming the mouse “knows” the schedule.

## Proposed model comparison (staged)

I suggest we fit models in this order:

1. **Single-state drift model** (your minimal starting point)  
2. **Hidden-value output model** (x_t → λ_t or P(lick))  
3. **Dual-state model:** V_t = opioid reward / action value, D_t = withdrawal / deficit burden, decision on M_t = V_t − D_t  
4. **Passive-specific extension:** Pavlovian context memory × withdrawal gain (for elevated withdrawal seeking in passive animals)

This staged approach keeps the first fit simple while leaving room for group-specific mechanisms.

## Passive group — why we care beyond “control”

In our paradigm, the passive group is not only a control. It may reflect a **patient-relevant route**: non-contingent opioid exposure during the yoked phase, then later instrumental opportunity. We see **elevated PR during withdrawal in passive mice**, which may reflect **PIT-like generalized invigoration** from prior opioid-paired context — not the same mechanism as active-group, contingency-dependent rebound at re-exposure.

So I would like to test whether a **context / Pavlovian gain term** improves fit in passive withdrawal sessions, separate from opioid-specific action value in active animals.

## Data and meeting

I can share raw data with the newer timing / lockout fields. I may not be able to come to CNC tomorrow; **Thursday morning at CNC** or **Friday** would work better for me (happy to meet in person or Zoom).

Thanks again — I really appreciate your help thinking this through.

Best,  
Hansol

---

## Parameter cheat sheet (for discussion)

| Symbol | Meaning |
|--------|---------|
| x_t | Hidden engagement / motivational value |
| λ_t | Observed lick rate (from softplus or similar) |
| α | Baseline drift (may differ by phase / group) |
| τ | Time constant (memory persistence) |
| R | Reward bump per rewarded lick |
| L | Cost per unrewarded lick / failure |
| σ | Noise scale |
| θ | Disengagement threshold |
| V_t | Opioid reward / action value (dual model) |
| D_t | Deficit / withdrawal burden (dual model) |
| C_t | Pavlovian context memory (passive extension) |
