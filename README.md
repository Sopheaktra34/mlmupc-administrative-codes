# MLMUPC Administrative API

This project provides a small FastAPI service and static browser interface for exploring Cambodia administrative boundaries stored in a MySQL database.

## Overview

The `mlmupc` service exposes hierarchical geographic data for:
- Provinces
- Districts
- Communes
- Villages

It supports cascading selection, lookup by administrative code, name search, and count summaries.

## Contents

- `main.py` - FastAPI application with endpoints for lookup, search, counts, and static UI delivery
- `db.py` - MySQL connection helper and query execution wrappers
- `queries.py` - SQL statements for provinces, districts, communes, villages, lookup, search, and counts
- `Database.sql` - MySQL schema for the `mlmupc` database
- `static/index.html` - Browser interface for the API
- `static/app.js` - Frontend logic for cascading selection and searches

## Requirements

- Python 3.10+ (or compatible)
- MySQL server
- Python packages:
  - `fastapi`
  - `uvicorn`
  - `mysql-connector-python`

## Installation

1. Create and activate a Python virtual environment.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies.

```powershell
pip install fastapi uvicorn mysql-connector-python
```

3. Create the MySQL database and schema.

```powershell
mysql -u root -p < Database.sql
```

4. Load administrative data into the database.

> The repository does not include import scripts for source data. Use your own data import workflow to populate `provinces`, `districts`, `communes`, and `villages`.

## Configuration

The default database connection is defined in `db.py`:

```python
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Jenifer12",
        database="mlmupc"
    )
```

Update the host, user, password, or database name as needed for your local environment.

## Running the API

Start the app with Uvicorn:

```powershell
uvicorn main:app --reload
```

Then open the UI in your browser:

```text
http://127.0.0.1:8000/
```

## API Endpoints

- `GET /` - Opens the static browser application
- `GET /provinces` - Returns all provinces
- `GET /districts?province_code=<id>` - Returns districts for the selected province
- `GET /communes?district_code=<id>` - Returns communes for the selected district
- `GET /villages?commune_code=<id>` - Returns villages for the selected commune
- `GET /lookup/code?code=<code>` - Returns full context for a province/district/commune/village code
- `GET /lookup/name?q=<query>` - Search administrative names in Khmer or English
- `GET /counts/overall` - Returns counts for provinces, districts, communes, and villages
- `GET /counts/context?level=<province|district|commune>&id=<id>` - Returns child counts by selected level

## Notes

- The front-end uses the static folder mounted at `/static`.
- The UI supports both code-based lookup and keyword search.
- If your MySQL database uses a different port or credentials, update `db.py` accordingly.

## License

No license specified. Add one if you want to publish this repository publicly.
