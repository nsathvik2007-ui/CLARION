# .github/ — Architecture contract (GitHub automation)

> **Documentation-only scaffold.** No module functionality is implemented. Follow the original v4 specification and root README; file stubs are comments describing future work.

## Responsibility
GitHub collaboration, PR review and repository automation; workflows remain documentation only until implementation.

## Phase ownership
cross-phase

## Planned files and their exact responsibilities

| File | What must be written during implementation |
|---|---|
| **pull_request_template.md** | Require linked phase, architecture block, changed contracts, real test evidence, security impact and rollback. |

## Data/interfaces
**Inputs:** See parent modules and the architecture specification.

**Outputs:** Versioned artifacts or typed interfaces; no implementation exists yet.

## Security, testing and acceptance
Require executable tests, provenance and review before marking complete.

For all modules: preserve provenance, causal availability, explicit uncertainty/abstention, offline operation, real tests and realistic false-positive controls. Record status in docs/progress before claiming completion.

## Implementation handoff
Do not add executable logic before the assigned phase PR; update this README when actual public interfaces, dependencies and tests are verified.
