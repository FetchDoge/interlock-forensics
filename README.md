# interlock-forensics

**Pre-registers the AEGIS Day-30 provenance gate as one SHA-256-checkable file at a public tag.**

[![Claims integrity](https://github.com/FetchDoge/interlock-forensics/actions/workflows/claims.yml/badge.svg)](https://github.com/FetchDoge/interlock-forensics/actions/workflows/claims.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

This is a public witness repo for the AEGIS Day-30 gate (cutoff 2026-10-27 23:59 America/Edmonton). Its scope is this SDK, the pre-registered benchmark, and the smallest AEGIS slice the benchmark can score, not the full agent OS. It contains a pre-registration, a draft attestation schema and a claims check. It has no SDK code yet.

## What it guarantees

- **One hash input.** The witness is `prereg/day30.md` at tag `aegis-day30`. The hash is the SHA-256 of the raw file bytes (UTF-8, LF, no BOM, exactly one trailing newline). The hash line is not in the file.
- **A stranger can recompute it.** One clone and one command, with no account needed.
- **A one-bit metric with a written falsifier.** The pre-registration defines M_fc. The gate passes only if a forged-signature attestation (TC-SIG-FORGE) is rejected, gets no partial trust, and returns no success status. The falsifier is stated in the file.

## Quickstart

```
git clone --depth 1 --branch aegis-day30 https://github.com/FetchDoge/interlock-forensics.git
cd interlock-forensics
sha256sum prereg/day30.md
```

## How it fails

- **A changed file means a changed hash.** Any edit to `prereg/day30.md` changes the SHA-256, so a mismatch against the published hash shows the witness was altered.
- **A forged attestation accepted means M_fc = 0.** If TC-SIG-FORGE gets acceptance, partial trust or a silent pass, Day-30 fails. The pre-registration says so before the run.
- **The unknowns below stay unknown until they are written into the tagged file.** No hash should be quoted as the record before then.

## Evidence

Checked 2026-10-07:

- Tag `aegis-day30` **exists**. It is annotated, by "Ektar", dated 2026-10-02 04:55 MDT, and points at commit `c24e2e5`.
- At that tag, `sha256sum prereg/day30.md` gives `ad1938c74d7ea7a4bd25632837803cfa4f9f14994c49928ae32842b49525f48b`, identical to `main`.
- The tagged file still reads "Status: DRAFT on main. Not the frozen hash. Tag aegis-day30 is not cut." Its "Still UNKNOWN" section lists the verify key and signature algorithm, the verify invocation, and the URL where M_fc is recorded. The witness rule requires all of these in the tagged file before a hash counts, so **this tag does not yet satisfy the repo's own freeze rule.**
- `python3 scripts/check_claims.py` passes. CI runs it on every push.

## Still unknown

- **Attestation schema:** DRAFT at `schemas/provenance-attestation.v1.schema.json` (ProvenanceAttestation v1), not frozen.
- **Verify key and signature algorithm.** The schema's draft default is Ed25519, to be fixed in the frozen file.
- **Verify invocation.**
- **Where the gate records M_fc.**

## Status

Pre-registration in progress. The freeze needs the unknowns above resolved inside the tagged file. How to reconcile the existing tag with that rule is the maintainer's decision, due before the 2026-10-27 cutoff. No graded SDK diff merges before the freeze.

## License

MIT. See [LICENSE](LICENSE).
