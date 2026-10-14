# Investigator screen modules

> DESIGN ONLY — planned files are comments, not functioning application code.

**Scope:** One folder per end-user workflow, each with its own README and comment-only TSX files.

## File and folder responsibilities

| Folder | Screen |
|---|---|
| readiness | schema, capture/label gates |
| leads | ranked priorities, filters and uncertainty |
| graph | six-type temporal graph and path tracing |
| entities | MCER versions, H1–H5 constraints |
| patterns | peel/mixing-like/layering witness paths |
| signals | OOF model, Δ and Π evidence |
| propagation | frozen seed, value/context risk channels and 25-point cap |
| timeline | separate block vs P2P observed time |
| cases | authorized local case PDF/CSV/JSON export |
| models | model cards, temporal holdout, ablations |
| audit | source/run hashes and review history |

## Contracts, dependencies and safeguards

One shared typed localhost client, bounded/time-scoped endpoints; no duplicate risk arithmetic in UI.

## Exit criteria

Functional UI/e2e and accessibility tests after Phase 4 implementation.

For system-level dependency direction and migration rationale, consult the [production structure blueprint](../../../docs/architecture/repository-structure.md).
