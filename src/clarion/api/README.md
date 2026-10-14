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
