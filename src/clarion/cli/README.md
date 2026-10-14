# src/clarion/cli/ — Architecture contract

> **Documentation-only scaffold.** No module functionality is implemented. Follow the original v4 specification and root README; file stubs are comments describing future work.

## Responsibility
Offline CLI entry point for ingest, train, evaluate, investigate and serve.

## Phase ownership
P1–P5

## Planned files and their exact responsibilities

| File | What must be written during implementation |
|---|---|
| **__init__.py** | Declare package boundary. |
| **main.py** | Subcommand parser and exit codes. |
| **commands.py** | CLI composition of typed pipeline stages. |
| **diagnostics.py** | Doctor checks for offline wheels, licensing and models. |

## Data/interfaces
**Inputs:** Local file paths and safe versioned configs.

**Outputs:** Deterministic run manifests and clear actionable failures.

## Security, testing and acceptance
Reject missing model/data rather than download at inference.

For all modules: preserve provenance, causal availability, explicit uncertainty/abstention, offline operation, real tests and realistic false-positive controls. Record status in docs/progress before claiming completion.

## Implementation handoff
Do not add executable logic before the assigned phase PR; update this README when actual public interfaces, dependencies and tests are verified.
