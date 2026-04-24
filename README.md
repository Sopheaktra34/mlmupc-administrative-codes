# Cambodia Administrative Codes Dataset

A structured dataset of Cambodian administrative divisions in **Khmer** and **English**, prepared from a public legal PDF and reorganized into reusable formats.

This repository contains three files:

- `MLMUPC.csv` — structured CSV format
- `MLMUPC.json` — JSON export converted from the CSV
- `MLMUPC.txt` — plain-text hierarchical format

The dataset is organized in Cambodia's administrative hierarchy:

```text
Province / Capital (ខេត្ត/រាជធានី)
└── District / Municipality / Khan (ស្រុក/ក្រុង/ខណ្ឌ)
    └── Commune / Sangkat (ឃុំ/សង្កាត់)
        └── Village (ភូមិ)
```

***

## Overview

This repository is a personal data-preparation project created from a public source PDF.

I manually:

*   extracted text from the source PDF using OCR
*   cleaned and normalized the extracted text
*   reorganized the content into a hierarchical dataset
*   created both CSV and TXT versions for easier reuse

This project is intended to make the data easier to use for:

*   database import
*   GIS and mapping
*   lookup/search systems
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

A machine-friendly structured dataset.

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

This file is recommended for application use because it preserves the same hierarchical structure and `parent_code` relationships in JSON format.

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

A human-readable plain-text hierarchy of the same data.

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
*   plain-text search
*   comparing extracted text against the original PDF
*   lightweight reference without CSV tools

***

## Data Structure

This dataset follows Cambodia's administrative hierarchy:

*   **Province / Capital**
*   **District / Municipality / Khan**
*   **Commune / Sangkat**
*   **Village**

The coding system is hierarchical, which makes the dataset suitable for:

*   parent-child lookups
*   nested administrative trees
*   region filtering
*   search and validation
*   province → district → commune → village dropdown selectors

***

## Suggested Use Cases

This dataset may be useful for:

### Web & Application Development

*   location selectors
*   address forms
*   profile location input
*   logistics and delivery systems

### Data Engineering

*   MySQL / PostgreSQL import
*   ETL pipelines
*   Pandas / Python analysis
*   lookup APIs
*   search indexing

### GIS, Government, and Research

*   administrative reference
*   geospatial projects
*   census or demographic work
*   local governance systems
*   NGO / development projects

***

## Source

The original public source document is hosted by **Open Development Cambodia (ODC)**:

**Inter-ministerial Prakas no. 052 on the implementation of identification codes for the capital, provinces, municipalities, districts, Khans, communes, Sangkats, and villages of the Kingdom of Cambodia**

Source page:  
<https://data.opendevelopmentcambodia.net/laws_record/inter-ministerial-prakas-no-052-on-the-implementation-of-identification-codes-for-the-capital-provi/resource/30a2354d-8158-43a6-a1b2-e27bcc6f795b>

### Associated institutions

*   **ក្រសួងរៀបចំដែនដី នគរូបនីយកម្ម និងសំណង់**  
    **Ministry of Land Management, Urban Planning and Construction**
*   **ក្រសួងមហាផ្ទៃ**  
    **Ministry of Interior**

This repository is **not an official publication** of ODC or of any government institution.  
It is a **personal OCR extraction, cleaning, and restructuring** of public source material for easier reuse.

***

## Data Quality Notes

Because this dataset was manually extracted and cleaned from a PDF source, there may still be:

*   OCR errors
*   transliteration inconsistencies
*   spacing / punctuation issues
*   formatting artifacts from the original PDF
*   occasional discrepancies that should be reviewed before production use

If you find any issues, contributions and corrections are welcome.

***

## Attribution

If you reuse this repository, please consider acknowledging:

*   the original public source document hosted by **Open Development Cambodia (ODC)**
*   the fact that this repository is a **manually prepared OCR/text extraction and restructuring** of that source

Suggested attribution:

> Based on a public ODC-hosted PDF of Inter-ministerial Prakas no. 052 on Cambodian administrative identification codes; repository version prepared through OCR extraction, cleaning, and restructuring by the repository maintainer.

***

## License

The original ODC resource page lists the source document license as:

**License not specified**

This repository does **not** claim ownership of the original legal/public source content.  
Please review the original source and applicable reuse conditions before redistribution or commercial use.

If desired, you may add a separate note for the repository formatting / structuring work only.

***

## Contributing

Contributions are welcome, especially for:

*   OCR corrections
*   Khmer spelling fixes
*   transliteration cleanup
*   missing or duplicated entries
*   formatting improvements
*   schema or documentation enhancements

Please open an issue or submit a pull request if you would like to help improve the dataset.

***

## Disclaimer

This repository is a community-prepared data extraction and structuring project based on a public source document.

It is provided for convenience and practical reuse, but it should **not** be treated as a legally authoritative replacement for the original official publication.