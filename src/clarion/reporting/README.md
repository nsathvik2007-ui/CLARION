# src/clarion/reporting — implementation blueprint

> Architecture-only: no functionality or test success is claimed.

**Phase:** P4
**Scope:** Safe CSV/JSON/PDF case export separate from scoring and explanation generation.

## Inputs and outputs
**Consumes:** Reviewed CaseDossier, permitted analyst identity  
**Provides:** Redacted, hashed offline exports

## Planned file responsibilities
| File | Required work |
|---|---|
| `__init__.py` | Reporting package |
| `csv_json.py` | Escaped CSV, canonical JSON and formula-injection checks |
| `pdf.py` | Static local PDF case dossier renderer |
| `manifest.py` | Case provenance, export hashes and audit chain |

## Dependencies and security
Never edit evidence, hide abstentions or use remote asset generation.

## Test and completion gate
Export determinism, redaction, tamper tests, sanitized input.

Review [complete project structure](../../../docs/architecture/repository-structure.md) before implementing. Commit real code and its tests in the relevant phase PR; replace comment-only placeholders deliberately.
