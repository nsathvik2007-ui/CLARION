# src/clarion/ingestion/adapters — implementation blueprint

> Architecture-only: no functionality or test success is claimed.

**Phase:** P1
**Scope:** Per-dataset versioned adapter registry instead of monolithic adapters.py.

## Inputs and outputs
**Consumes:** Authorized local CSV/JSON/XML or benchmark source + usage manifest  
**Provides:** Typed canonical records, source mapping and unsupported-field declarations

## Planned file responsibilities
| File | Required work |
|---|---|
| `__init__.py` | Adapter registration and supported capability interface |
| `sih.py` | SIH transactions and optional network metadata adapter |
| `bitcoin_core.py` | Bitcoin Core local block/UTXO export adapter |
| `elliptic_pp.py` | Elliptic++ graph and feature benchmark import; preserve granularity |
| `bitcoinheist.py` | Address-level labeled benchmark import; uncertain negative labels |

## Dependencies and security
Never fabricate raw transactions or cross-layer IP ownership from benchmark graph features.

## Test and completion gate
Schema versions, sampling bias, missing fields, exact monetary conversion.

Review [complete project structure](../../../../docs/architecture/repository-structure.md) before implementing. Commit real code and its tests in the relevant phase PR; replace comment-only placeholders deliberately.
