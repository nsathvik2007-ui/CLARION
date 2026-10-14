# CLARION v4 — FILE BLUEPRINT ONLY. NOT FUNCTIONAL.
# Intended path: src/clarion/storage/catalog.py
# Purpose: DuckDB table registration, reader validation and schema migrations.
# Phase: P1
# Contracts: Typed canonical records + run IDs. -> Read-only verifiable snapshots and queryable local catalog.
# Acceptance: Reject mutation of raw evidence; test crash atomicity and migrations.
# Implementation will be added in a dedicated phase PR with tests and security review.
