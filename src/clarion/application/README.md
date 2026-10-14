# src/clarion/application — implementation blueprint

> Architecture-only: no functionality or test success is claimed.

**Phase:** P1–P4
**Scope:** One orchestrator and lifecycle for entire local investigation pipeline.

## Inputs and outputs
**Consumes:** Domain contracts, readiness, immutable snapshots, injected services  
**Provides:** Deterministic run manifests, routed stages, reproducible cases

## Planned file responsibilities
| File | Required work |
|---|---|
| `__init__.py` | Module API |
| `pipeline.py` | Ingest→ready→graph→features→MCER→motifs→stack/Δ/Π→freeze→MLRP→final risk→dossier |
| `stages.py` | Typed stage prerequisites, status and abstention |
| `run_manager.py` | Atomic jobs, resume, checkpoint, hash/version ledger |
| `mode_policy.py` | Cross-layer/chain-only and supervised/unsupervised routing |

## Dependencies and security
Coordinates modules; no algorithm duplication, no inference-time network, no pass-2 feedback.

## Test and completion gate
End-to-end fixtures, no-wire/labels/goal fallbacks, deterministic restart.

Review [complete project structure](../../../docs/architecture/repository-structure.md) before implementing. Commit real code and its tests in the relevant phase PR; replace comment-only placeholders deliberately.
