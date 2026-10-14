# Ingestion and source adapters

> DESIGN ONLY — planned files are comments, not functioning application code.

**Scope:** Secure bulk CSV/JSON/XML normalized into source-provenance records.

## File and folder responsibilities

| Location | Planned work |
|---|---|
| readers.py | bounded CSV/JSON/XML and XXE refusal |
| validation.py | integer sats, UTC/time semantics, duplicates, row diagnostics |
| adapters/__init__.py | source capability and version registry |
| adapters/sih.py | official SIH-format input |
| adapters/bitcoin_core.py | authentic local UTXO export, not historical relay IP |
| adapters/elliptic_pp.py | Elliptic++ transaction/actor feature benchmark |
| adapters/bitcoinheist.py | address behavior labels with uncertain negatives |

## Contracts, dependencies and safeguards

Source-specific adapters declare absent fields; no synthetic cross-layer joins from benchmark feature graphs.

## Exit criteria

Exact formats, source rights/hashes, no inferred ownership, malformed-input and unit tests.

For system-level dependency direction and migration rationale, consult the [production structure blueprint](../../../docs/architecture/repository-structure.md).
