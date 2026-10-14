# src/clarion/divergence/ — Architecture contract

> **Documentation-only scaffold.** No module functionality is implemented. Follow the original v4 specification and root README; file stubs are comments describing future work.

## Responsibility
Δ1–Δ5 cross-layer residuals, paired-view baseline and robust abstention.

## Phase ownership
P3

## Planned files and their exact responsibilities

| File | What must be written during implementation |
|---|---|
| **__init__.py** | Declare package boundary. |
| **paired_views.py** | Join only high-quality paired chain/wire observations. |
| **cca.py** | Train-only CCA baseline and held-out residual calibration. |
| **components.py** | Sybil collapse, spray, rhythm, route, infrastructure checks. |
| **abstain.py** | Coverage, dependence and clock quality gates. |

## Data/interfaces
**Inputs:** Trusted observed TXID pairs and independent sensor evidence.

**Outputs:** Separate residual/component results or explicit abstention.

## Security, testing and acceptance
Shared public relays and geolocation uncertainty cannot infer identity.

For all modules: preserve provenance, causal availability, explicit uncertainty/abstention, offline operation, real tests and realistic false-positive controls. Record status in docs/progress before claiming completion.

## Implementation handoff
Do not add executable logic before the assigned phase PR; update this README when actual public interfaces, dependencies and tests are verified.
