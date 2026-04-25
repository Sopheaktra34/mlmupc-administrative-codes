# Cambodia Administrative Codes Dataset

A structured dataset of Cambodian administrative divisions in **Khmer** and **English**, prepared from a public legal PDF and reorganized into reusable formats.

This repository contains three files:

*   `MLMUPC.csv` — structured CSV format
*   `MLMUPC.json` — JSON export converted from the CSV
*   `MLMUPC.txt` — plain-text hierarchical format

The dataset follows Cambodia’s official administrative hierarchy:

```text
Province / Capital (ខេត្ត/រាជធានី)
└── District / Municipality / Khan (ស្រុក/ក្រុង/ខណ្ឌ)
    └── Commune / Sangkat (ឃុំ/សង្កាត់)
        └── Village (ភូមិ)
```

***

## Dataset Size (Administrative Units)

This dataset contains the following number of administrative units:

| Level                              | Count      |
| ---------------------------------- | ---------- |
| Provinces / Capital                | **25**     |
| Districts / Municipalities / Khans | **210**    |
| Communes / Sangkats                | **1,653**  |
| Villages                           | **14,553 + 1** |

for the village except 1 cause the code not align with the parents code: 

* (05050201 ភូមិ យស់ជោ Yuos Chou) and this village is in (051002 ឃុំ ជើងរាស់ Cheung Roas)
> Note: Village counts are based on **unique administrative codes**.  
> The original source text contains a small number of duplicated village entries, which were deduplicated by code.

***

## Overview

This repository is a personal data‑preparation project created from a public source PDF.

I manually:

*   extracted text from the source PDF using OCR
*   cleaned and normalized the extracted text
*   reorganized the content into a hierarchical dataset
*   created CSV, JSON, and TXT versions for easier reuse

This project is intended to make the data easier to use for:

*   database import
*   GIS and mapping
*   lookup and search systems
*   address forms and cascading dropdowns
*   administrative reference
*   research and localization work

***

## Repository Contents

```text
.
├── MLMUPC.csv
├── MLMUPC.json
├── MLMUPC.txt
└── README.md
```

***

## File Details

### 1) `MLMUPC.csv`

A machine‑friendly structured dataset.

#### Columns

*   `code` — administrative code
*   `level` — administrative level (`province`, `district`, `commune`, `village`)
*   `name_kh` — name in Khmer
*   `name_en` — English / Latin transliteration
*   `parent_code` — parent administrative unit code

#### Example

```csv
code,level,name_kh,name_en,parent_code
01,province,បន្ទាយមានជ័យ,Banteay Meanchey,
0102,district,មង្គលបុរី,Mangkul Bourei,01
010201,commune,បន្ទាយនាង,Banteay Neang,0102
01020101,village,អូរធំ,Ou Thum,010201
```

***

### 2) `MLMUPC.json`

A JSON export converted from `MLMUPC.csv`.

This version preserves the same hierarchical structure and `parent_code` relationships in JSON format and is recommended for application use.

#### Fields

*   `code` — administrative code
*   `level` — administrative level (`province`, `district`, `commune`, `village`)
*   `name_kh` — name in Khmer
*   `name_en` — English / Latin transliteration
*   `parent_code` — parent administrative unit code

#### Example

```json
{
  "code": "01",
  "level": "province",
  "name_kh": "បន្ទាយមានជ័យ",
  "name_en": "Banteay Meanchey",
  "parent_code": ""
}
```

***

### 3) `MLMUPC.txt`

A human‑readable plain‑text hierarchy of the same data.

#### Example

```text
01 ខេត្ត បន្ទាយមានជ័យ Banteay Meanchey
0102 ស្រុក មង្គលបុរី Mangkul Bourei
010201 ឃុំ បន្ទាយនាង Banteay Neang
01020101 ភូមិ អូរធំ Ou Thum
```

This version is useful for:

*   manual checking
*   quick browsing
*   plain‑text search
*   comparing extracted text against the original PDF
*   lightweight reference without CSV tools

***

## Data Structure

This dataset follows Cambodia’s official administrative coding structure:

*   **Province / Capital**
*   **District / Municipality / Khan**
*   **Commune / Sangkat**
*   **Village**

The hierarchical code system supports:

*   parent‑child lookups
*   nested administrative trees
*   region filtering
*   address validation
*   province → district → commune → village dropdown selectors

***

## Suggested Use Cases

### Web & Application Development

*   address forms
*   location selectors
*   user profile location input
*   logistics and delivery systems

### Data Engineering

*   MySQL / PostgreSQL import
*   ETL pipelines
*   Pandas / Python analysis
*   lookup APIs
*   search indexing

### GIS, Government, and Research

*   administrative reference
*   mapping projects
*   census and demographic analysis
*   local governance systems
*   NGO and development work

***

## Source

The original public source document is hosted by **Open Development Cambodia (ODC)**:

**Inter‑ministerial Prakas No. 052 on the implementation of identification codes for the capital, provinces, municipalities, districts, Khans, communes, Sangkats, and villages of the Kingdom of Cambodia**

Source page:  
<https://data.opendevelopmentcambodia.net/laws_record/inter-ministerial-prakas-no-052-on-the-implementation-of-identification-codes-for-the-capital-provi/resource/30a2354d-8158-43a6-a1b2-e27bcc6f795b>

### Associated institutions

*   **ក្រសួងរៀបចំដែនដី នគរូបនីយកម្ម និងសំណង់**  
    Ministry of Land Management, Urban Planning and Construction

*   **ក្រសួងមហាផ្ទៃ**  
    Ministry of Interior

This repository is **not an official publication** of ODC or any government institution.  
It is a **personal OCR extraction, cleaning, and restructuring** of public source material.

***

## Data Quality Notes

Because this dataset was manually extracted and cleaned from a PDF source, there may still be:

*   OCR artifacts
*   transliteration inconsistencies
*   spacing or punctuation issues
*   formatting remnants from the original PDF
*   minor discrepancies that should be reviewed before production use

If issues are found, corrections and improvements are welcome.

***

## Attribution

If you reuse this dataset, please consider acknowledging:

*   the original public source document hosted by **Open Development Cambodia (ODC)**
*   the manual OCR extraction, cleaning, and restructuring performed by the repository maintainer

Suggested attribution:

> Based on a public ODC‑hosted PDF of Inter‑ministerial Prakas No. 052 on Cambodian administrative identification codes; dataset prepared through OCR extraction, cleaning, and restructuring by the repository maintainer.

***

## License

The original source page lists the license as:

**License not specified**

This repository does **not** claim ownership of the original legal content.  
Please review the original source and applicable reuse conditions before redistribution or commercial use.

***

## Contributing

Contributions are welcome, especially for:

*   OCR corrections
*   Khmer spelling fixes
*   transliteration cleanup
*   missing or duplicated entries
*   formatting improvements
*   schema and documentation enhancements

Please open an issue or submit a pull request.

***

## Disclaimer

This repository is a community‑prepared data extraction and structuring project based on a public legal source document.

It is provided for convenience and reuse and should **not be treated as a legally authoritative substitute** for the original official publication.
