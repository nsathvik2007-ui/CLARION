# src/clarion/core/ — Architecture contract

> **Documentation-only scaffold.** No module functionality is implemented. Follow the original v4 specification and root README; file stubs are comments describing future work.

## Responsibility
Shared immutable identifiers, typed errors, structured logging and run manifests.

## Phase ownership
P1

## Planned files and their exact responsibilities

| File | What must be written during implementation |
|---|---|
| **__init__.py** | Declare package boundary. |
| **identifiers.py** | Stable TXID, outpoint, entity, evidence and run identifier types. |
| **provenance.py** | Source hash and evidence reference ledger; never invent data. |
| **clock.py** | Timestamp semantics, UTC normalization, skew and precision budget. |
| **errors.py** | Typed validation, abstention and policy errors. |

## Data/interfaces
**Inputs:** Raw imported identifiers, timestamps and source hashes.

**Outputs:** Typed core contracts + auditable errors.

## Security, testing and acceptance
Test collisions, nulls, timezone ambiguity and manifest determinism.

For all modules: preserve provenance, causal availability, explicit uncertainty/abstention, offline operation, real tests and realistic false-positive controls. Record status in docs/progress before claiming completion.

## Implementation handoff
Do not add executable logic before the assigned phase PR; update this README when actual public interfaces, dependencies and tests are verified.
