# MLMUPC Administrative Codes (Cambodia)

This repository contains administrative boundary codes published by the Ministry of Land Management, Urban Planning and Construction (MLMUPC) of Cambodia.

The dataset is provided as a **faithful text extraction** from the original official PDF and a **mechanical CSV conversion** of that text. No data cleaning, correction, enrichment, or normalization has been applied.

---

## Contents

### `MLMUPC.txt`
- Raw text extracted directly from the official MLMUPC PDF document
- Preserves original ordering, structure, and line breaks as much as possible
- Represents the closest machine‑readable form of the source document

### `MLMUPC.csv`
- CSV file converted mechanically from `MLMUPC.txt`
- Columns:
  - `code` — administrative code as it appears in the text
  - `level` — province, district, commune, or village
  - `name_kh` — Khmer name
  - `name_en` — Latin name (when present)
  - `parent_code` — inferred hierarchical parent code
- No external references or corrections were introduced during conversion

---

## Important Notes on Data Quality

- This dataset reflects **only what can be extracted from the source PDF**.
- Some administrative units may appear visually in the original document but not as structured rows in the extracted text due to document layout or OCR limitations.
- No assumptions, imputations, or manual patches were added.
- Users requiring a fully validated or normalized gazetteer should treat this repository as **source material**, not a final canonical list.

---

## Source

Original source publication:
> Ministry of Land Management, Urban Planning and Construction (MLMUPC), Cambodia

All administrative names and codes originate from the official MLMUPC document.

---

## Intended Use

- Transparency and reproducibility
- Research and documentation reference
- OCR and document‑structure analysis
- Downstream transformation, validation, or normalization by users if required

---

## Disclaimer

This repository is **not an official publication** of the Royal Government of Cambodia.

It is a best‑effort, faithful extraction of publicly available information for research and open‑data purposes.
