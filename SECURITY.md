# CLARION security and responsible analysis (architecture only)

The repository currently contains design documentation and **comment-only file stubs**. Do not expose a future API publicly until tested access controls and audit logs exist.

- Report security issues privately through GitHub's repository security reporting when enabled, rather than sharing sensitive findings publicly.
- Never upload confidential Bitcoin monitoring captures, personal IP datasets, keys or credentials.
- All future ingestion must be bounded, reject XML external entities, escape CSV exports and attach provenance hashes.
- Treat every network observation as supporting evidence **not** proof of wallet ownership or identity.
- Ensure the deployed application and every bundled UI/model/GeoIP asset operates offline.
- See docs/security/README.md and the complete CLARION architecture specification.
