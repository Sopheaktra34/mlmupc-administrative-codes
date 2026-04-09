import mysql.connector

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Jenifer12",
        database="mlmupc"
    )

def fetch_all(db, query, params=None):
    cursor = db.cursor()
    cursor.execute(query, params or ())
    rows = cursor.fetchall()
    cursor.close()
    return rows

def fetch_one(db, query, params=None):
    cursor = db.cursor()
    cursor.execute(query, params or ())
    row = cursor.fetchone()
    cursor.close()
    return row