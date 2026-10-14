# CLARION Python backend

> DESIGN ONLY — planned files are comments, not functioning application code.

**Scope:** Typed modular monolith: one run orchestration layer, independent evidence and ML engines.

## File and folder responsibilities

- domain, core: immutable data and source/time/score invariants
- application: DAG, mode gates, checkpointing, frozen-seed order
- ingestion/adapters, readiness, chain, wire, storage: traceable evidence
- graph, features, representation, entity_resolution, patterns: graph and MCER
- training, detection, divergence, expenditure, fusion, propagation: ML and scores
- explanations, reporting, api/routers, cli: local case delivery
- security, observability, synthetic, evaluation: correctness and governance

## Contracts, dependencies and safeguards

Domain never depends on infrastructure; algorithm stages cannot import orchestration; source IP relay never proves wallet control.

## Exit criteria

Phase-wise integrated smoke, temporal leakage, transaction flow and air-gap tests.

For system-level dependency direction and migration rationale, consult the [production structure blueprint](../../docs/architecture/repository-structure.md).
