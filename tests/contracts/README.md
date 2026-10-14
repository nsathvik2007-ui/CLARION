# tests/contracts — implementation blueprint

> Architecture-only: no functionality or test success is claimed.

**Phase:** P1/P4
**Scope:** Versioned schema and API/domain compatibility tests.

## Inputs and outputs
**Consumes:** Canonical schemas, generated OpenAPI, independent fixtures  
**Provides:** Schema migration and type compatibility results

## Planned file responsibilities
| File | Required work |
|---|---|
| `test_domain_schemas.py` | Sats, graph relations, missingness and score-kind contracts |
| `test_api_contracts.py` | Versioning, pagination, abstention and role check DTOs |

## Dependencies and security
Reject incompatible schema silently treated as old.

## Test and completion gate
Negative control and old/new version acceptance.

Review [complete project structure](../../docs/architecture/repository-structure.md) before implementing. Commit real code and its tests in the relevant phase PR; replace comment-only placeholders deliberately.
