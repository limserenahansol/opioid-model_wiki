# Science & Hypotheses

## Normative question

| KO | EN |
|----|-----|
| Opioid self-administration 동물은 무엇을 maximize/regulate하는가? 언제 lick/seek/escalate? Withdrawal 후 re-exposure motivation? Passive만으로 같은 phenotype이 안 되는 이유? | What latent quantities do animals regulate? When seek/lick/escalate? Why stronger re-exposure after withdrawal in active mice? Why passive exposure ≠ active phenotype? |

## Seminar motifs → addiction mapping

| Motif | Variable (concept) | Role |
|-------|-------------------|------|
| A. Reward integrator | `V_t` | Opioid reward / action–outcome memory |
| B. Deficit integrator | `D_t` | Absence, withdrawal, homeostatic/allostatic error |
| C. Seeking oscillator | bouts, ILI | Run–pause–lick microstructure (not only scalar value) |
| D. Context modulation | gain on inputs | Phase, cue, chamber, active vs passive history |

**Required:** both **drug reward axis** and **drug absence axis**. Active re-exposure = **V × D** (+ context), not exposure count alone.

## Active vs passive (conceptual)

### Active group

- **During:** strong action–outcome → opioid
- **Post:** consolidated seeking
- **Withdrawal:** violated expectation → ↑ deficit state
- **Re-exposure:** strong rebound (contingency-dependent `V_t` × withdrawal)

### Passive group — not only control

- **During:** Pavlovian/context opioid memory; **no** strong contingency (`valid: false` licks Days 6–10)
- **Post:** weak emerging instrumental structure
- **Withdrawal:** can show **↑ PR / seeking** via **PIT-like** generalized invigoration
- **Re-exposure:** weaker reinstatement (weak consolidated action value)
- **Translational angle:** passive exposure → later craving when instrumental opportunity appears (**patient-like route**)

### Mechanism contrast

| | Active | Passive |
|---|--------|---------|
| Withdrawal seeking | Deficit + opioid-specific value | `C_t × G_withdrawal` (context × generalized gain) |
| Re-exposure | `V_t × W_t` amplification | Limited; extinction-like weakening possible |

## Hypotheses (full)

### H0 — Latent state (not PR schema)

**EN:** Mice do not solve PR by explicit schedule representation; persistence emerges from a **low-dimensional latent motivational process** integrating recent reward, effort, failure, and pause.

**KO:** PR schedule 전체 표상이 아니라, reward/effort/failure/pause를 통합하는 **저차원 잠재 동기 과정**이 참여·이탈을 결정한다.

### H1 — Contingency reshapes dynamics

**EN:** Contingent opioid experience alters **update rules and thresholds** → stronger persistence, abstinence amplification, re-engagement (active).

**KO:** Contingent 경험이 갱신 규칙·임계값을 바꾼다 (active).

### H2 — Dual-axis interaction

**EN:** Re-exposure seeking: **V + D + interaction** fits better than **V-only**.

### H3 — Passive PIT

**EN:** Passive withdrawal ↑ seeking: **Pavlovian/context memory × withdrawal gain**, not stable opioid action value.

## Predictions

| # | Behavior / model | Active | Passive |
|---|------------------|--------|---------|
| 1 | Reward-history integration | Stronger; history predicts later seeking | Weaker |
| 2 | Withdrawal neural/behavior | Cue-specific gain modulation | Generalized ↑ possible (PIT) |
| 3 | Re-exposure fit | V × D interaction | C × G; weaker V reinstatement |
| 4 | Threshold | Lower re-engage after abstinence | Generalized invigoration, higher quit threshold later |

## Drift–diffusion rationale (Approach 1)

**Pros:** implementable; captures carry-over; avoids per-distance state explosion; matches colleague framing.

**Cons (v1):** weak on discrete effort counts and pause structure → Model 4 or bout-HMM later.

**Not claiming:** mice optimize PR perfectly; **mis-specified internal model** may be more biological than full task model.

## What we are NOT testing in v1

- Full belief-state POMDP over schedule structure
- Neural manifold / photometry (planned after behavior fit)
- Explicit “distance to next reward” discrete states
