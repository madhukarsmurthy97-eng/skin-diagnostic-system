import sqlite3
from datetime import datetime

DB_PATH = "patients.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            image_path TEXT,
            condition TEXT,
            confidence REAL,
            treatment TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_patient(name, image_path, condition, confidence, treatment):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO patients (name, image_path, condition, confidence, treatment, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, image_path, condition, confidence, treatment, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

def fetch_all_patients():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients ORDER BY timestamp DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows
