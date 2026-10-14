# src/clarion/api/ — Architecture contract

> **Documentation-only scaffold.** No module functionality is implemented. Follow the original v4 specification and root README; file stubs are comments describing future work.

## Responsibility
Local REST application, typed DTOs and bounded investigation query contracts.

## Phase ownership
P4

## Planned files and their exact responsibilities

| File | What must be written during implementation |
|---|---|
| **__init__.py** | Declare package boundary. |
| **main.py** | FastAPI composition root with no network calls. |
| **routes.py** | Health readiness jobs graph lead entity case endpoints. |
| **schemas.py** | Typed pagination, confidence, abstention and errors. |
| **dependencies.py** | Local catalog, authorization and model inference injection. |

## Data/interfaces
**Inputs:** Stored run artifacts and approved local model versions.

**Outputs:** Read-only investigation APIs and export task status.

## Security, testing and acceptance
No unauthenticated remote exposure; enforce pagination and CSP.

For all modules: preserve provenance, causal availability, explicit uncertainty/abstention, offline operation, real tests and realistic false-positive controls. Record status in docs/progress before claiming completion.

## Implementation handoff
Do not add executable logic before the assigned phase PR; update this README when actual public interfaces, dependencies and tests are verified.

---

## Investigator API contracts (§11)

Local-only, typed FastAPI endpoints (tentative route names): runs/readiness, paginated leads, bounded graph neighborhood and risk path, MCER versions, motif and Δ/Π signal detail, model versions/metrics and authorized dossier export. Each response must carry run_id, cutoff_time, evidence IDs, source/score type, confidence/abstentions, provenance and redaction state.

**Security:** bind localhost by default; role authorization before any remote access; enforce maximum graph nodes/hops, path sanitization, request sizes, immutable run artifacts, XSS-safe presentation, protected PDF/CSV export. Never assert wallet ownership from a TXID relay. Proposed routes and view models: [Dashboard design](../../../docs/architecture/investigator-dashboard-architecture.md).
