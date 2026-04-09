from fastapi import FastAPI, Depends
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

from db import get_db, fetch_all, fetch_one
import queries

app = FastAPI(title="MLMUPC Administrative API")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/")
def home():
    return FileResponse(os.path.join(STATIC_DIR, "index.html"))

# ---------------- CASCADING ----------------

@app.get("/provinces")
def provinces(db=Depends(get_db)):
    return fetch_all(db, queries.province_query)

@app.get("/districts")
def districts(province_code: int, db=Depends(get_db)):
    return fetch_all(db, queries.district_query, (province_code,))

@app.get("/communes")
def communes(district_code: int, db=Depends(get_db)):
    return fetch_all(db, queries.commune_query, (district_code,))

@app.get("/villages")
def villages(commune_code: int, db=Depends(get_db)):
    return fetch_all(db, queries.village_query, (commune_code,))

# ---------------- LOOKUP WITH FULL CONTEXT ----------------

@app.get("/lookup/code")
def lookup(code: str, db=Depends(get_db)):

    if len(code) == 2:
        r = fetch_one(db, queries.province_context_query, (code,))
        if not r:
            return {"error": "Not found"}
        return {"hierarchy": [
            {"level": "province", "code": r[0], "name_kh": r[1], "name_en": r[2]}
        ]}

    if len(code) == 4:
        r = fetch_one(db, queries.district_context_query, (code,))
        if not r:
            return {"error": "Not found"}
        return {"hierarchy": [
            {"level": "province", "code": r[0], "name_kh": r[1], "name_en": r[2]},
            {"level": "district", "code": r[3], "name_kh": r[4], "name_en": r[5]},
        ]}

    if len(code) == 6:
        r = fetch_one(db, queries.commune_context_query, (code,))
        if not r:
            return {"error": "Not found"}
        return {"hierarchy": [
            {"level": "province", "code": r[0], "name_kh": r[1], "name_en": r[2]},
            {"level": "district", "code": r[3], "name_kh": r[4], "name_en": r[5]},
            {"level": "commune", "code": r[6], "name_kh": r[7], "name_en": r[8]},
        ]}

    if len(code) == 8:
        r = fetch_one(db, queries.village_context_query, (code,))
        if not r:
            return {"error": "Not found"}
        return {"hierarchy": [
            {"level": "province", "code": r[0], "name_kh": r[1], "name_en": r[2]},
            {"level": "district", "code": r[3], "name_kh": r[4], "name_en": r[5]},
            {"level": "commune", "code": r[6], "name_kh": r[7], "name_en": r[8]},
            {"level": "village", "code": r[9], "name_kh": r[10], "name_en": r[11]},
        ]}

    return {"error": "Invalid code"}

# ---------------- SEARCH BY NAME ----------------

@app.get("/lookup/name")
def search_by_name(q: str, db=Depends(get_db)):
    key = f"%{q}%"
    rows = fetch_all(db, queries.name_search_query, (key, key) * 4)
    return [
        {"level": r[0], "code": r[1], "name_kh": r[2], "name_en": r[3]}
        for r in rows
    ]
    
@app.get("/counts/overall")
def overall_counts(db=Depends(get_db)):
    return {
        "provinces": fetch_one(db, queries.count_all_provinces)[0],
        "districts": fetch_one(db, queries.count_all_districts)[0],
        "communes":  fetch_one(db, queries.count_all_communes)[0],
        "villages":  fetch_one(db, queries.count_all_villages)[0],
    }
    
@app.get("/counts/context")
def context_counts(level: str, id: int, db=Depends(get_db)):

    if level == "province":
        return {
            "districts": fetch_one(db, queries.count_districts_by_province, (id,))[0],
            "communes":  fetch_one(db, queries.count_communes_by_province, (id,))[0],
            "villages":  fetch_one(db, queries.count_villages_by_province, (id,))[0],
        }

    if level == "district":
        return {
            "communes": fetch_one(db, queries.count_communes_by_district, (id,))[0],
            "villages": fetch_one(db, queries.count_villages_by_district, (id,))[0],
        }

    if level == "commune":
        return {
            "villages": fetch_one(db, queries.count_villages_by_commune, (id,))[0],
        }

    return {"error": "Invalid level"}