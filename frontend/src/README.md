# Offline TypeScript investigator UI

> DESIGN ONLY — planned files are comments, not functioning application code.

**Scope:** React frontend composed from independent screen modules, shared view models and local assets.

## File and folder responsibilities

- app: routes, selected run/time and auth context.
- components: observed/inferred/abstained indicators, score legends.
- features: vertical folders for readiness, leads, graph, entities, patterns, signals, propagation, timeline, cases, models, audit.
- lib: local API client and versioned data types.
- styles: local CSS, accessible print and no CDN.
- main.tsx: future browser bootstrap (currently comment-only).

## Contracts, dependencies and safeguards

UI never reads source captures or fits ML; always preserve time cutoff, source evidence and score type.

## Exit criteria

Accessible offline browser, bounded graph, correct redactions and role-aware exports.

For system-level dependency direction and migration rationale, consult the [production structure blueprint](../../docs/architecture/repository-structure.md).
