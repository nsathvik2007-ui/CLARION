# CLARION v4 — FILE BLUEPRINT ONLY. NOT FUNCTIONAL.
# Intended path: src/clarion/ingestion/readers.py
# Purpose: Stream bounded CSV, JSON and safe XML; DTD/XXE disabled.
# Phase: P1
# Contracts: Local authorized files and declared input schema. -> Versioned normalized records and row-level validation report.
# Acceptance: Fuzz dangerous XML, oversized arrays, mixed amount formats and duplicates.
# Implementation will be added in a dedicated phase PR with tests and security review.
