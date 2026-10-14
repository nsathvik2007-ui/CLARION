# src/clarion/security/ — Architecture contract

> **Documentation-only scaffold.** No module functionality is implemented. Follow the original v4 specification and root README; file stubs are comments describing future work.

## Responsibility
Offline boundaries, path safety, sanitization, access control and audit.

## Phase ownership
P1/P4

## Planned files and their exact responsibilities

| File | What must be written during implementation |
|---|---|
| **__init__.py** | Declare package boundary. |
| **parsers.py** | Upload limits, XXE and nested-data bomb rejection. |
| **audit.py** | Tamper-evident case and evidence log. |
| **access.py** | Loopback-only by default, optional RBAC before remote exposure. |
| **redaction.py** | PII and IP export limits, CSV/PDF sanitization. |

## Data/interfaces
**Inputs:** Policies, incoming files, case access context.

**Outputs:** Security decisions/audit entries and safe exports.

## Security, testing and acceptance
Offline test, fuzz parsing, forbid untrusted pickled model loading.

For all modules: preserve provenance, causal availability, explicit uncertainty/abstention, offline operation, real tests and realistic false-positive controls. Record status in docs/progress before claiming completion.

## Implementation handoff
Do not add executable logic before the assigned phase PR; update this README when actual public interfaces, dependencies and tests are verified.
