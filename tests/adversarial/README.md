# tests/adversarial/ — Architecture contract

> **Documentation-only scaffold.** No module functionality is implemented. Follow the original v4 specification and root README; file stubs are comments describing future work.

## Responsibility
File parser abuse, graph contamination, false associations and poisoning tests.

## Phase ownership
P1–P5

## Planned files and their exact responsibilities

| File | What must be written during implementation |
|---|---|
| **test_xxe_and_upload.py** | TODO: entity expansion, zip bombs, CSV formula, path traversal. |
| **test_false_ownership.py** | TODO: relay sees TXID does not imply wallet owner. |

## Data/interfaces
**Inputs:** See parent modules and the architecture specification.

**Outputs:** Versioned artifacts or typed interfaces; no implementation exists yet.

## Security, testing and acceptance
Require executable tests, provenance and review before marking complete.

For all modules: preserve provenance, causal availability, explicit uncertainty/abstention, offline operation, real tests and realistic false-positive controls. Record status in docs/progress before claiming completion.

## Implementation handoff
Do not add executable logic before the assigned phase PR; update this README when actual public interfaces, dependencies and tests are verified.
