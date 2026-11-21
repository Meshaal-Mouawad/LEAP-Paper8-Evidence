# LEAP Paper 8 — Evidence and Replication (R29A)

**Paper:** When KPI Verification References Cross Evidence and Defect Boundaries: Two Archival Audits  
**Author:** Meshaal Mouawad  
**Harvard Dataverse DOI:** https://doi.org/10.7910/DVN/DC2FOK (dataset currently draft/in review according to account listing dated 2026-11-21)

This repository provides the curated derived replication evidence for **two distinct archival audits**. The audits have different units of analysis and are not pooled.

## Reproduce

```bash
python3 code/reproduce_curated.py
```

## Organization

- `analysis/`: item-level and alert-target audits, result summary, reference-applicability logic
- `code/`: reproduction script and twelve executable constructed witnesses
- `data/`: documentary readings, source pairs, reference certificates, and second-archive ledger
- `documentation/`: R29A manuscript PDF
- `metadata/`: attribution, provenance, Dataverse metadata

## Attribution and evidence boundaries

Meshaal Mouawad is the manuscript author. Hazem Alkhaiat is credited in dataset metadata as Data Collector. The first archive's proposed source-based key was not used in original grading. The primary raw event records remain in a controlled research archive and are not distributed here. See `metadata/Provenance.md` for source-origin details.

## Citation

Cite the Harvard Dataverse dataset DOI above after its publication. The repository is a companion for code and versioned evidence, not a replacement for the dataset DOI.

## Release state

R29A GitHub staging package. Check the final GitHub commit and the published Dataverse version before citing a specific release.
