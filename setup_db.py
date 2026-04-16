import sqlite3

conn = sqlite3.connect("demon_slayer.db")
cur = conn.cursor()

# CREATE TABLES
cur.execute("""
CREATE TABLE actors (
    id INTEGER PRIMARY KEY,
    name TEXT
)
""")

cur.execute("""
CREATE TABLE characters (
    id INTEGER PRIMARY KEY,
    name TEXT,
    breathing_style TEXT,
    rank TEXT,
    affiliation TEXT,
    actor_id INTEGER
)
""")

# INSERT DATA
cur.executemany("INSERT INTO actors VALUES (?, ?)", [
    (1, 'Natsuki Hanae'),
    (2, 'Akari Kito'),
    (3, 'Hiro Shimono'),
    (4, 'Yoshitsugu Matsuoka')
])

cur.executemany("INSERT INTO characters VALUES (?, ?, ?, ?, ?, ?)", [
    (1, 'Tanjiro Kamado', 'Water', 'Slayer', 'Demon Slayer Corps', 1),
    (2, 'Nezuko Kamado', 'Demon', 'Demon', 'None', 2),
    (3, 'Zenitsu Agatsuma', 'Thunder', 'Slayer', 'Demon Slayer Corps', 3),
    (4, 'Inosuke Hashibira', 'Beast', 'Slayer', 'Demon Slayer Corps', 4)
])

conn.commit()
conn.close()

print("DB FIXED SUCCESSFULLY")