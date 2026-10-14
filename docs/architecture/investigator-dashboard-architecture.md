# Explainable Investigator Dashboard & Evidence Dossiers — Detailed Design

> **Status: proposed UI/API architecture only.** The uploaded v4 diagram's **§11** mandates an interactive multi-layer graph, timeline, multi-hop tracing, risk overlays, filters, attribution, explanations and offline case export. This page converts those into **screen contracts**. No frontend, screenshot, trained result or live report is claimed to exist.

## 1. Investigator experience and screen map

~~~mermaid
flowchart LR
   LOGIN["Local authorized analyst"] --> OVERVIEW["Workspace / readiness overview"]
   OVERVIEW --> LEADS["Ranked lead queue P1–P4"]
   LEADS --> CASE["Entity or transaction dossier"]
   CASE --> GRAPH["Temporal graph / path explorer"]
   CASE --> SCORES["Stack · Δ · Π · patterns · MLRP"]
   CASE --> TIMELINE["Transaction / relay timeline"]
   CASE --> EXPORT["CSV/PDF/JSON report"]
   OVERVIEW --> METHODS["Models, datasets and run audit"]
~~~

| Screen | Primary widgets | Source/uncertainty behavior |
|---|---|---|
| A. Dataset readiness | source files + checksums, schema fields, time precision, TXID join coverage, MI/dependence checks, labels, CHAIN_ONLY/CROSS_LAYER and calibration modes | show reason when wire evidence, fees, objectives or labels missing |
| B. Leads queue | sortable risk 0–100 **or** novelty rank, P1–P4, confidence state, entity/transaction, pattern, Δ/Π availability, verification state | never show unsupported 0–100 calibrated probability |
| C. Graph workspace | layered chain+wire graph; six typed nodes; time slider/day/week selector; evidence type visibility; selected-depth path, ASN/country context | host observed TXID relation explicitly labeled "relayed/observed", not "owns"; time cutoff always visible |
| D. Entity hypotheses | MCER group ID/version, proposed members, confidence, H1–H5 supporting/conflicting links, previous version, false-merge caution | candidate cluster ≠ confirmed real-world identity |
| E. Anomaly intelligence | base learner outputs, out-of-fold stack, calibration/interval, motifs, SHAP/meta-model contributions where supported | show score type; distinguish novelty/uncalibrated/calibrated |
| F. Δ/Π analysis | Δ1–Δ5, paired-view residual, Δ coverage; itemized Π_fee, Π_hop, Π_time, Π_frag, Π_infra; valid Π–Δ quadrant | explicit "ABSTAIN" and reason instead of invented zero/cost |
| G. Risk propagation | level selector Address/Transaction/Entity/Host/ASN (Country context), forward/backward toggle, heat overlay, provenance path, hop/time/value share, seed & cap | host/ASN non-emitting boundaries, service absorbing markers, seed freeze |
| H. Timeline | block time vs wire sensor observation, input/output flows, scripted pattern spans, fee/time changes | separate clock time types; no impossible broadcast-origin claims |
| I. Case dossier | summary reason, anomaly score, Δ contradiction, Π bill, selected minimal evidence subgraph, MLRP path, attribution card, references, report signature/hash | review annotations, redaction, limitations, no guilt language |
| J. Model/evaluation panel | dataset/model versions, OOF/holdout metrics, PR-AUC, ARI/NMI, false positives, ablations, drift, sample size | synthetic vs real benchmark badges; no inflated reliability claims |

## 2. Recommended layout (desktop, not a frontend implementation)

~~~text
+----------------------------------------------------------------------------------------+
| CLARION v4       Run: R...  Cutoff: ...  Mode: CHAIN_ONLY / CROSS_LAYER  [Export]     |
+----------------------------------------------------------------------------------------+
| Left navigation     | Global filters: time, country, ASN, motif, level, P1..P4        |
| - Readiness         +-----------------------------------------------------------------+
| - Leads             | Selected lead [Entity E...]   Risk or rank | Confidence + mode |
| - Graph             +-----------------------------------------+-----------------------+
| - Entities          | Graph/time visualization               | Why flagged?         |
| - Patterns          | typed nodes and selected path          | Stack, Δ, Π, motif   |
| - Models            | chain edges != observed relay edges    | MLRP contributions   |
| - Cases             | layers/timeline + hop slider           | abstentions/benign   |
| - Audit             +-----------------------------------------+-----------------------+
|                     | Minimal evidence path + timestamp + source + export hash         |
+----------------------------------------------------------------------------------------+
~~~

Use responsive browser layout, keyboard navigation, accessible contrast, downloadable reports, clear loading/empty/error/offline states, and pagination/top-k graph expansion. No remote CDN, remote map, telemetry, analytics or browser font download.

## 3. Data/API contracts (planned and versioned later)

**Do not implement endpoint names as promises yet.** These are candidate v1 routes to freeze in a reviewed OpenAPI contract in Phase 4.

| Proposed REST path | Method | Returns |
|---|---|---|
| /api/v1/runs | GET | local dataset/investigation run manifests and status |
| /api/v1/runs/{id}/readiness | GET | schema/time/join/gating and abstention audit |
| /api/v1/leads | GET | paginated and filtered lead summary with score_type, priority and source |
| /api/v1/leads/{id} | GET | one lead's versions, local stack, Δ, Π, pattern and MLRP |
| /api/v1/graph/neighborhood | GET | time-cutoff-limited typed nodes/edges + relation provenance |
| /api/v1/graph/paths | GET | bounded contributing paths with channel and evidence refs |
| /api/v1/entities/{id}/versions | GET | MCER candidate history, confidence and constraints |
| /api/v1/subjects/{id}/signals | GET | selected model/Δ/Π/motif signals and abstentions |
| /api/v1/cases/{id} | GET | dossier assembly snapshot + audit/version data |
| /api/v1/cases/{id}/export | POST | authorized PDF/CSV/JSON rendering with redaction and hash |
| /api/v1/models | GET | model registry; split and calibration status |
| /api/v1/evaluations | GET | per-holdout and ablation reports, synthetic disclaimer |

**Filtering:** run_id, snapshot cutoff/range, subject_type, risk band, pattern type, ASN/country, service boundary, score availability. **Pagination:** page size limits server-side; graph queries restrict max hops/nodes/edges and a time cutoff. **Authorization:** loopback-only baseline; approved analyst roles and audit if LAN access is later enabled. Avoid exposing raw file paths in API responses.

### 3.1 Canonical UI view models (design, not code)

~~~text
LeadSummary: id, run_id, subject_type, local_score?, final_score?,
             score_type, priority?, uncertainty?, model_id,
             top_reasons[], valid_signal_flags, review_state
GraphNode:   id, kind, label, valid_from/to, level_risk?,
             confidence?, source_refs[], redaction_state
GraphEdge:   id, relation, source, target, amount_sats?,
             event_time, evidence_refs[], association_confidence?,
             ownership_claim=false
SignalPanel: base_predictions[], stack?, calibration?, Δ?,
             Π_components[], motifs[], abstain_reasons[]
PropagationPath: channel, frozen_seed_id, hops, elapsed_time,
                 value_shares[], level_score, boundary_flags, evidence_refs[]
Dossier:     run_hash, model_hash, snapshot_hash, reviewer_actions,
             explanation, witness_edges[], report_hash, disclaimers[]
~~~

Field values may be **missing/abstained**; never coerce missing cross-layer evidence into a zero score.

## 4. Explainability and the per-entity dossier

The uploaded diagram explicitly calls for:
- one-line Π–Δ quadrant verdict;
- itemized Π bill: observed expenditure vs justified minimum;
- chain/wire contradiction described in ordinary language;
- minimal sufficient subgraph with time-ordered evidence path;
- frozen-seed MLRP path and value share;
- ASN/country/host type and inferred time-zone (with uncertainty);
- SHAP explanation over supported stacking meta-models and per-signal contribution bars;
- chain-only counterfactual re-score (same model-valid test path and cutoff);
- confidence/priority P1–P4 and local CSV/PDF export.

**Dossier sections in display order:** case and run IDs; data/sensor completeness; subject and cluster hypothesis; why flagged; local anomaly score *type*; Δ panel; Π bill; motifs; propagation channels and top contributors; counterevidence/benign confounders; graph/timeline witness; model/calibration/threshold versions; reviewer decisions; redaction/export manifest.

If the only basis for a claim is a model attention weight or a network relay, explain it as an **association hypothesis**, not a firm attribution.

## 5. Frontend modular architecture and responsibility map

| Folder/file | Planned view responsibility |
|---|---|
| frontend/src/app/App.tsx | root navigation, authorization context, global run/time mode |
| frontend/src/app/routes.tsx | readiness, leads, graph, entity, signals, cases and models route map |
| frontend/src/features/leads/LeadsPage.tsx | paginated lead queue, risk bands and clear score types |
| frontend/src/features/graph/GraphPage.tsx | Cytoscape.js temporal six-type graph, risk overlay, path tracing |
| frontend/src/features/cases/CaseDossier.tsx | evidence summaries and local case export |
| frontend/src/components/EvidenceChip.tsx | observed vs inferred vs abstained evidence indicators |
| frontend/src/components/RiskScale.tsx | local/final score and propagation ≤25 distinction |
| frontend/src/lib/types.ts | view models and versioned OpenAPI-derived types |
| frontend/src/lib/api.ts | bounded local API, stale-data errors, offline response |
| frontend/src/styles | local CSS tokens, accessible/print layout, no CDNs |
| src/clarion/api | validated FastAPI routers, paginated graph queries, local auth |
| src/clarion/explanations | SHAP/meta-feature contributions, case report evidence assembly |

## 6. Investigator threat and privacy model

- Malicious case text, labels and IP strings must be escaped/sanitized (XSS and CSV formula injection).
- All graph and case queries are limited by user authorization, run scope, time cutoff and max response size.
- Show redacted IP details to unauthorized viewers; never export real-world attribution inferred from a relay.
- Immutable source hashes and report hashes, provenance references, reviewer action log, allowed export roles.
- Restrict local UI default binding to 127.0.0.1. Do not expose a development server publicly.
- Check offline operation with network denied after all static assets, software wheels, models and licensed GeoIP files have been provisioned.
- Do not pass raw private evidence to external LLMs or remote telemetry.

## 7. Acceptance tests

- [ ] Dashboard loads when Internet egress is blocked and all static assets are local.
- [ ] Missing Δ/Π/labels produces visible abstention, never an invented probability.
- [ ] Entity, address, transaction, host, ASN and country render with correct risk semantics; Country **not scored**.
- [ ] Clicking any leading risk evidence resolves to correct immutable source ID and graph snapshot/time.
- [ ] Analyst can compare stack/Δ/Π/motif/MLRP contributions without double counting propagation.
- [ ] Time slider cannot reveal post-cutoff facts while inspecting an earlier lead.
- [ ] Risk heat overlay preserves service boundaries and inbound/outbound channel distinction.
- [ ] PDFs/CSVs/JSONs are hash-verified, sanitized, redacted according to role and locally reproducible.
- [ ] UI paths and semantic labels are accessible by keyboard and screen reader.
- [ ] Huge graphs are bounded/paginated and don't crash the browser; source graph remains available for local queries.
- [ ] All reported accuracy belongs to a named dataset, split and model version.

**Source:** uploaded CLARION v4 architecture, §11 and §12, with dependency on §4–§10. Screens, endpoint names, data types and UI layout are implementation proposals.

**Implementation folder map:** [production module structure](repository-structure.md) and the per-screen READMEs under frontend/src/features. UI routes are planned; no screens are implemented yet.
