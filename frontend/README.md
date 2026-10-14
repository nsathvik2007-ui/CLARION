# frontend/ — Architecture contract

> **Documentation-only scaffold.** No module functionality is implemented. Follow the original v4 specification and root README; file stubs are comments describing future work.

## Responsibility
Offline investigator application workspace: React/TypeScript is planned; NO package.json until implementation.

## Phase ownership
P4

## Planned files and their exact responsibilities

| File | What must be written during implementation |
|---|---|
| **vite.config.ts** | Plan offline-only asset bundling, API proxy and CSP. |
| **tsconfig.json** | Plan strict TS builds and path aliases. |

## Data/interfaces
**Inputs:** See parent modules and the architecture specification.

**Outputs:** Versioned artifacts or typed interfaces; no implementation exists yet.

## Security, testing and acceptance
Require executable tests, provenance and review before marking complete.

For all modules: preserve provenance, causal availability, explicit uncertainty/abstention, offline operation, real tests and realistic false-positive controls. Record status in docs/progress before claiming completion.

## Implementation handoff
Do not add executable logic before the assigned phase PR; update this README when actual public interfaces, dependencies and tests are verified.

---

## §11 target product screens (not yet implemented)

Investigator workspace: readiness → ranked leads → selected entity/transaction → typed graph + time selector → stack/Δ/Π/motif breakdown → forward/backward MLRP exposure path → audit and export. Add per-run model/evaluation view. Every chart must expose its event-time cutoff and provenance.

**UI stack:** React/TypeScript, Cytoscape.js or equivalent fully bundled local graph visualization, responsive keyboard-accessible layouts, no external CDN/fonts/telemetry. Frontend is driven only by versioned local FastAPI contracts with pagination/authorization. See [Dashboard design](../docs/architecture/investigator-dashboard-architecture.md).
