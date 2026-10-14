# frontend/src/features/ — Architecture contract

> **Documentation-only scaffold.** No module functionality is implemented. Follow the original v4 specification and root README; file stubs are comments describing future work.

## Responsibility
Feature-level investigator screens and flow orchestration.

## Phase ownership
P4

## Planned files and their exact responsibilities

| File | What must be written during implementation |
|---|---|
| **leadExplorer.tsx** | TODO: ranked leads, filters, provenance and P1–P4. |
| **graphExplorer.tsx** | TODO: time-bounded six-node heterograph visualization. |
| **caseDossier.tsx** | TODO: PDF/CSV export, warnings and redaction. |

## Data/interfaces
**Inputs:** See parent modules and the architecture specification.

**Outputs:** Versioned artifacts or typed interfaces; no implementation exists yet.

## Security, testing and acceptance
Require executable tests, provenance and review before marking complete.

For all modules: preserve provenance, causal availability, explicit uncertainty/abstention, offline operation, real tests and realistic false-positive controls. Record status in docs/progress before claiming completion.

## Implementation handoff
Do not add executable logic before the assigned phase PR; update this README when actual public interfaces, dependencies and tests are verified.

---

## Detailed screen design and feature routing (§11)

**leadExplorer.tsx:** readiness mode, P1–P4 queue, score type and uncertainty, filters for risk/ASN/country/pattern/window. **graphExplorer.tsx:** node kinds Transaction/Address/Entity/Host/ASN/Country, chain vs observed-relay edge styling, time slider, MLRP heat overlay and path provenance (Country context-only). **caseDossier.tsx:** itemized Δ/Π, stacked SHAP/meta contributions, separate local/propagation risk, source hashes, redaction and PDF/CSV export.

The final screen map also requires entity-cluster history, peel/mixing/layering timeline, model/ablation comparison, and source quality/abstention diagnostics. Proposed view models and endpoint contracts: [Dashboard design](../../../docs/architecture/investigator-dashboard-architecture.md).
