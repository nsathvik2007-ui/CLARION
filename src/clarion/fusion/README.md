# src/clarion/fusion/ — Architecture contract

> **Documentation-only scaffold.** No module functionality is implemented. Follow the original v4 specification and root README; file stubs are comments describing future work.

## Responsibility
Two-pass calibrated local and capped propagation fusion and typology.

## Phase ownership
P3/P4

## Planned files and their exact responsibilities

| File | What must be written during implementation |
|---|---|
| **__init__.py** | Declare package boundary. |
| **local.py** | Calibrate eligible local evidence without raw Π+Δ addition. |
| **typology.py** | Π–Δ quadrants, only when both axes valid. |
| **final.py** | Freeze seeds, cap MLRP <=25/100, priority P1–P4. |

## Data/interfaces
**Inputs:** Stack, patterns, Δ/Π, then independent frozen MLRP exposure.

**Outputs:** Provisional/final lead score with contribution explanation.

## Security, testing and acceptance
No circular propagation feeding pass-1 predictor.

For all modules: preserve provenance, causal availability, explicit uncertainty/abstention, offline operation, real tests and realistic false-positive controls. Record status in docs/progress before claiming completion.

## Implementation handoff
Do not add executable logic before the assigned phase PR; update this README when actual public interfaces, dependencies and tests are verified.

---

## Full §9 two-pass fusion contract

**Pass 1:** consume local stacked score (or honest novelty rank), motif evidence, valid Δ residual/components, and valid itemized Π bills, plus missingness/coverage. Do not raw-add Π and Δ, or use unsupported conformal p-values. The scored result can be uncalibrated if labels are missing. Freeze and hash provisional seed vector s.

**§10 propagation:** deterministic causal value-flow and separate network-context channel, service boundaries, bounded paths. No pass-1 feedback.

**Pass 2:** combine frozen local score with a **maximum 25/100-point** contribution from validated propagation, exactly once; show the local contribution, propagation points, final risk 0–100 (only if justified), calibration uncertainty and P1–P4 triage band. Thresholds and normalization must be empirically validated. When no trusted calibration is available, label as *priority/rank*, not an illegal-activity probability.

**Typology:** Δ and Π remain two explanatory axes with ABSENT/ABSTAIN states; legitimate exchange batching, VPN users and CoinJoin are false-positive controls. See [MLRP architecture](../../../docs/architecture/risk-propagation-architecture.md), [stacking architecture](../../../docs/architecture/stacking-architecture.md).
