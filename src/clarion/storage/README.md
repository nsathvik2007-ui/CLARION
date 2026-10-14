# src/clarion/storage/ — Architecture contract

> **Documentation-only scaffold.** No module functionality is implemented. Follow the original v4 specification and root README; file stubs are comments describing future work.

## Responsibility
Storage abstraction for immutable Parquet evidence, local DuckDB and run snapshots.

## Phase ownership
P1

## Planned files and their exact responsibilities

| File | What must be written during implementation |
|---|---|
| **__init__.py** | Declare package boundary. |
| **parquet_store.py** | Atomic normalized snapshot writes and content hashes. |
| **catalog.py** | DuckDB table registration, reader validation and schema migrations. |
| **manifest.py** | Dataset, model, config and artifact version manifest. |

## Data/interfaces
**Inputs:** Typed canonical records + run IDs.

**Outputs:** Read-only verifiable snapshots and queryable local catalog.

## Security, testing and acceptance
Reject mutation of raw evidence; test crash atomicity and migrations.

For all modules: preserve provenance, causal availability, explicit uncertainty/abstention, offline operation, real tests and realistic false-positive controls. Record status in docs/progress before claiming completion.

## Implementation handoff
Do not add executable logic before the assigned phase PR; update this README when actual public interfaces, dependencies and tests are verified.
