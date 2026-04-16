import sqlite3

conn = sqlite3.connect("demon_slayer.db")
cur = conn.cursor()

cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cur.fetchall()

print("TABLES:", tables)

if tables:
    for t in tables:
        print(f"\nDATA FROM {t[0]}:")
        rows = cur.execute(f"SELECT * FROM {t[0]}").fetchall()
        print(rows)

conn.close()