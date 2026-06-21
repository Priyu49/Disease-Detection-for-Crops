import sqlite3

def init_db():
    conn = sqlite3.connect("farm.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        disease TEXT,
        confidence REAL
    )
    """)

    conn.commit()
    conn.close()

def insert_data(disease, confidence):
    conn = sqlite3.connect("farm.db")
    c = conn.cursor()

    c.execute("INSERT INTO history (disease, confidence) VALUES (?, ?)", 
              (disease, confidence))

    conn.commit()
    conn.close()