# frontend/src/features/timeline — implementation blueprint

> Architecture-only: no functionality or test success is claimed.

**Phase:** P4
**Scope:** Block vs observed relay time and amount paths

## Inputs and outputs
**Consumes:** Typed localhost API, cutoff-filtered score/evidence view models  
**Provides:** Accessible screen and safe graph/query interactions

## Planned file responsibilities
| File | Required work |
|---|---|
| `TimelinePage.tsx` | Block vs observed relay time and amount paths |

## Dependencies and security
UI never claims TXID host is wallet owner, never uses CDNs/remote telemetry; score type and evidence provenance visible.

## Test and completion gate
Keyboard navigation, offline assets, bounded rendering, correct warnings and source drill-down.

Review [complete project structure](../../../../docs/architecture/repository-structure.md) before implementing. Commit real code and its tests in the relevant phase PR; replace comment-only placeholders deliberately.
