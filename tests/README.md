# Complete verification layout

> DESIGN ONLY — planned files are comments, not functioning application code.

**Scope:** Source/ML/security/testing controls aligned with architecture blocks 0–12.

## File and folder responsibilities

- unit: parser and local math tests.
- contracts: domain schema/API compatibility.
- integration: deterministic full chain-only and validated-wire pipelines.
- property: graph conservation, no time travel or fan-out amplification.
- leakage: temporal OOF and per-fold graph/MCER feature cutoffs.
- adversarial: XXE/CSV/model poisoning, false wallet ownership.
- offline: air-gapped operation.
- e2e: local case UI and report export.
- performance: measured RAM, p50/p95 and throughput.
- fixtures: sealed synthetic truths and benign service controls.

## Contracts, dependencies and safeguards

Tests are comment-only blueprints today. Performance and incident accuracy must never be asserted without real measured runs.

## Exit criteria

Every phase needs real executable tests, CI evidence and failure disclosure.

For system-level dependency direction and migration rationale, consult the [production structure blueprint](../docs/architecture/repository-structure.md).
