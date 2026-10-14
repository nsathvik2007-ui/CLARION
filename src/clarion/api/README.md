# Local investigator API and routers

> DESIGN ONLY — planned files are comments, not functioning application code.

**Scope:** FastAPI composition with bounded, authorized, read-only investigation queries.

## File and folder responsibilities

- main.py: FastAPI factory, offline/loopback defaults.
- dependencies.py: read-only DuckDB/result/model version injection and role context.
- schemas.py: DTO mapping and abstention/score type.
- routers/runs.py, leads.py, graph.py, entities.py, patterns.py: dataset/run and investigation.
- routers/signals.py, propagation.py, cases.py, models.py, evaluations.py: calibrated/novelty signals, safe risk paths, dossier and evidence metrics.

## Contracts, dependencies and safeguards

Each router owns its endpoint DTO; no training or scoring computation in HTTP handlers. API cannot expose private raw paths or unbounded graph neighborhoods.

## Exit criteria

OpenAPI/contract, role/access, paging, no egress and case export integration tests.

For system-level dependency direction and migration rationale, consult the [production structure blueprint](../../../docs/architecture/repository-structure.md).
