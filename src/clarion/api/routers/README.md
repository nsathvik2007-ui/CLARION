# src/clarion/api/routers — implementation blueprint

> Architecture-only: no functionality or test success is claimed.

**Phase:** P4
**Scope:** Separate versioned offline investigation HTTP query surfaces.

## Inputs and outputs
**Consumes:** Authenticated local reader, run model/evidence, finite query params  
**Provides:** Typed response DTOs, read-only investigation and authorized export

## Planned file responsibilities
| File | Required work |
|---|---|
| `__init__.py` | Router composition |
| `runs.py` | Runs, jobs and status |
| `leads.py` | Ranked leads and filters |
| `graph.py` | Bounded graph neighborhoods, evidence paths |
| `entities.py` | MCER candidate history/conflicts |
| `patterns.py` | Motif witness subgraphs |
| `signals.py` | Model, Δ/Π and typology results |
| `propagation.py` | Frozen seeds, bounded paths and risk layers |
| `cases.py` | Evidence dossier review/export |
| `models.py` | Model versions/calibration status |
| `evaluations.py` | Dataset/holdout metrics and ablations |

## Dependencies and security
No route performs training, new association inference or untrusted raw file execution; localhost until RBAC tested.

## Test and completion gate
API contract validation, pagination/limit, authorization and offline smoke.

Review [complete project structure](../../../../docs/architecture/repository-structure.md) before implementing. Commit real code and its tests in the relevant phase PR; replace comment-only placeholders deliberately.
