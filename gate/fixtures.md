# Structural gate fixture

The gate rehearsal may use a deterministic synthetic judgement fixture to test
CI wiring. The fixture labels every returned product as exactly relevant, so
judged coverage is complete and nDCG@10 ties at 1.0 across variants. These
numbers have no relevance-quality meaning.

The fixture report is evaluated from a frozen public API capture of the exact
source build image. Its signed attestation names that image's immutable Nexus
build receipt. The live KServe-abstention report remains separate and blocked.
