# src/clarion/domain — implementation blueprint

> Architecture-only: no functionality or test success is claimed.

**Phase:** P1–P4
**Scope:** Typed immutable Bitcoin, graph, evidence, entity, scoring and case objects.

## Inputs and outputs
**Consumes:** Validated source records, schema definitions, provenance  
**Provides:** Strongly typed value objects; explicit uncertainty, abstention and cutoff

## Planned file responsibilities
| File | Required work |
|---|---|
| `__init__.py` | Public domain types and schema version |
| `evidence.py` | Source references, hashes, observation time precision |
| `bitcoin.py` | Exact TXID/outpoint, amount_sats, transaction inputs/outputs |
| `graph.py` | Six node types and permitted temporal evidence edges |
| `entity.py` | Candidate clusters, constraints and lineage |
| `scoring.py` | Score types, Δ/Π, frozen seed, propagation output |
| `investigation.py` | Lead, case dossier and review state |

## Dependencies and security
No imports from ML, DuckDB, FastAPI, UI; relay never equals wallet controller.

## Test and completion gate
Validation/invariant tests for sats, time, source IDs, score kinds.

Review [complete project structure](../../../docs/architecture/repository-structure.md) before implementing. Commit real code and its tests in the relevant phase PR; replace comment-only placeholders deliberately.
