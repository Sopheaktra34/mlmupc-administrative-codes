# ---------- CASCADING ----------
province_query = """
SELECT id, code, name_kh, name_en
FROM provinces ORDER BY code
"""

district_query = """
SELECT id, code, name_kh, name_en
FROM districts WHERE province_id = %s ORDER BY code
"""

commune_query = """
SELECT id, code, name_kh, name_en
FROM communes WHERE district_id = %s ORDER BY code
"""

village_query = """
SELECT id, code, name_kh, name_en
FROM villages WHERE commune_id = %s ORDER BY code
"""

# ---------- CONTEXT ----------
province_context_query = """
SELECT p.code, p.name_kh, p.name_en
FROM provinces p WHERE p.code = %s
"""

district_context_query = """
SELECT p.code, p.name_kh, p.name_en,
       d.code, d.name_kh, d.name_en
FROM districts d
JOIN provinces p ON d.province_id = p.id
WHERE d.code = %s
"""

commune_context_query = """
SELECT p.code, p.name_kh, p.name_en,
       d.code, d.name_kh, d.name_en,
       c.code, c.name_kh, c.name_en
FROM communes c
JOIN districts d ON c.district_id = d.id
JOIN provinces p ON d.province_id = p.id
WHERE c.code = %s
"""

village_context_query = """
SELECT p.code, p.name_kh, p.name_en,
       d.code, d.name_kh, d.name_en,
       c.code, c.name_kh, c.name_en,
       v.code, v.name_kh, v.name_en
FROM villages v
JOIN communes c ON v.commune_id = c.id
JOIN districts d ON c.district_id = d.id
JOIN provinces p ON d.province_id = p.id
WHERE v.code = %s
"""

# ---------- SEARCH ----------
name_search_query = """
SELECT 'province', code, name_kh, name_en FROM provinces
WHERE name_kh LIKE %s OR name_en LIKE %s
UNION ALL
SELECT 'district', code, name_kh, name_en FROM districts
WHERE name_kh LIKE %s OR name_en LIKE %s
UNION ALL
SELECT 'commune', code, name_kh, name_en FROM communes
WHERE name_kh LIKE %s OR name_en LIKE %s
UNION ALL
SELECT 'village', code, name_kh, name_en FROM villages
WHERE name_kh LIKE %s OR name_en LIKE %s
"""

# ---------- OVERALL COUNTS ----------
count_all_provinces = "SELECT COUNT(*) FROM provinces"
count_all_districts = "SELECT COUNT(*) FROM districts"
count_all_communes  = "SELECT COUNT(*) FROM communes"
count_all_villages  = "SELECT COUNT(*) FROM villages"

# ---------- CONTEXT COUNTS ----------
count_districts_by_province = """
SELECT COUNT(*) FROM districts WHERE province_id = %s
"""

count_communes_by_province = """
SELECT COUNT(*) 
FROM communes c
JOIN districts d ON c.district_id = d.id
WHERE d.province_id = %s
"""

count_villages_by_province = """
SELECT COUNT(*) 
FROM villages v
JOIN communes c ON v.commune_id = c.id
JOIN districts d ON c.district_id = d.id
WHERE d.province_id = %s
"""

count_communes_by_district = """
SELECT COUNT(*) FROM communes WHERE district_id = %s
"""

count_villages_by_district = """
SELECT COUNT(*) 
FROM villages v
JOIN communes c ON v.commune_id = c.id
WHERE c.district_id = %s
"""

count_villages_by_commune = """
SELECT COUNT(*) FROM villages WHERE commune_id = %s
"""