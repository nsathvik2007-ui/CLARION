# Offline Linux runtime and network-denial acceptance plan

**DESIGN ONLY — none of these tests have been executed in this repository.** SIH26146 requires a workable, complete offline Linux application. Internet use during development or dataset acquisition is not evidence of an offline release.

## 1. Air-gapped package manifest

Produce a reproducible \`release-manifest.json\`: Python runtime version/architecture, pinned dependency lock, local wheelhouse hashes, PyTorch/PyG CPU (or optional supported CUDA) wheels, frontend dist checksums, packaged FastAPI/static assets, approved model checkpoints and safe serializer, DuckDB/Parquet schema versions, optional legally distributable licensed GeoIP/ASN resources, CPU/GPU hardware constraints, model trained-on dataset/split manifest, and license notices.

**Offline assets must be provisioned before air-gap.** Network access for development CI/training is permitted only outside the final inference environment.

## 2. Air-gapped install test (future)

1. Start from documented supported Linux target/CPU architecture in a clean VM or container with outbound network denied.
2. Install all Python wheels from local wheelhouse only and initialize a read-only source-evidence store.
3. Load local model/feature registry with version/hash compatibility checks; no remote model download.
4. Start backend bound to localhost; serve React/TS bundle, fonts and icons locally with CSP and no CDN.
5. Import small synthetic CSV, JSON and XML sample; run chain-only and where valid cross-layer gating, graph, local model, fusion and dossier export.
6. Monitor network sockets/logs during installation, inference, dashboard exploration and PDF/CSV export. Unexpected egress or missing remote asset is failure.
7. Run unauthorized local access and malicious file upload tests; save exact install script, expected/actual outputs, hashes, CPU/RAM peak and elapsed times.
8. Repeat with optional GeoIP unavailable and without GPU; verify graceful PARTIAL/ABSTAIN rather than crash.

## 3. Product minimum resource profile (targets to benchmark, not guarantees)

**CPU minimum:** one local Linux workstation; classic ML and batched graph features if advanced GNN checkpoints cannot run. **Accelerated:** optional CUDA host with version-matched PyTorch/PyG; memory budgets, graph neighborhood sample size and maximum local query window enforceable. The project must measure wall time, max RAM/VRAM, output bytes, graph scale and dashboard latency before publishing supported hardware.

**Offline data:** raw public chain data may be very large; package finite approved block-range or user-supplied evidence rather than require synchronizing full Bitcoin node over the network during inference.

## 4. Security and completeness

No installer executes untrusted user paths/scripts; restrict file permissions; set upload caps and safe deserialization; record SBOM/licenses; treat IP/port captures as private. The API is loopback-only until authentication and remote-access policy are tested. Outgoing telemetry, font/CDN dependencies and inference-time API requests are forbidden.

## 5. Release gate

[ ] pin supported Linux OS/arch; [ ] generate offline wheelhouse; [ ] approve model/GeoIP licensing; [ ] no unresolved dynamic CDN imports; [ ] source evidence hash; [ ] CPU fallback; [ ] fully network-denied install + investigation; [ ] export and graph view load; [ ] model integrity checks; [ ] actual logs linked.

A README statement that software "supports offline" is not enough. Evidence required in Phase 5.
