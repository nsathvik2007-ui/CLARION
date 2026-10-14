# src/clarion/ingestion/ — Architecture contract

> **Documentation-only scaffold.** No module functionality is implemented. Follow the original v4 specification and root README; file stubs are comments describing future work.

## Responsibility
Secure CSV/JSON/XML importers; raw immutability, row diagnostics and schema adapters.

## Phase ownership
P1

## Planned files and their exact responsibilities

| File | What must be written during implementation |
|---|---|
| **__init__.py** | Declare package boundary. |
| **readers.py** | Stream bounded CSV, JSON and safe XML; DTD/XXE disabled. |
| **validation.py** | Strict schema checks, amount conversion, quarantined errors. |
| **adapters.py** | Elliptic++, BitcoinHeist, Bitcoin Core and SIH adapter interfaces. |

## Data/interfaces
**Inputs:** Local authorized files and declared input schema.

**Outputs:** Versioned normalized records and row-level validation report.

## Security, testing and acceptance
Fuzz dangerous XML, oversized arrays, mixed amount formats and duplicates.

For all modules: preserve provenance, causal availability, explicit uncertainty/abstention, offline operation, real tests and realistic false-positive controls. Record status in docs/progress before claiming completion.

## Implementation handoff
Do not add executable logic before the assigned phase PR; update this README when actual public interfaces, dependencies and tests are verified.
