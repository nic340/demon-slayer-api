from fastapi import FastAPI
import sqlite3

app = FastAPI()

def get_db():
    conn = sqlite3.connect("demon_slayer.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/")
def home():
    return {"message": "Demon Slayer Fanbase API"}

@app.get("/characters")
def get_characters():
    conn = get_db()
    data = conn.execute("SELECT * FROM characters").fetchall()
    return [dict(row) for row in data]

@app.get("/characters/{character_id}")
def get_character(character_id: int):
    conn = get_db()
    data = conn.execute(
        "SELECT * FROM characters WHERE id=?", (character_id,)
    ).fetchone()
    return dict(data) if data else {"error": "Character not found"}

@app.get("/actors")
def get_actors():
    conn = get_db()
    data = conn.execute("SELECT * FROM actors").fetchall()
    return [dict(row) for row in data]

@app.get("/characters/{character_id}/full")
def get_character_full(character_id: int):
    conn = get_db()
    data = conn.execute("""
        SELECT characters.name, breathing_style, rank, affiliation, actors.name as actor
        FROM characters
        JOIN actors ON characters.actor_id = actors.id
        WHERE characters.id=?
    """, (character_id,)).fetchone()

    return dict(data) if data else {"error": "Not found"}

@app.get("/search")
def search_character(name: str):
    conn = get_db()
    data = conn.execute(
        "SELECT * FROM characters WHERE name LIKE ?",
        (f"%{name}%",)
    ).fetchall()
    conn.close()
    return [dict(row) for row in data]

@app.get("/breathing/{style}")
def get_by_breathing(style: str):
    conn = get_db()
    data = conn.execute(
        "SELECT * FROM characters WHERE breathing_style=?",
        (style,)
    ).fetchall()
    conn.close()
    return [dict(row) for row in data]

from fastapi import Body

@app.post("/characters")
def add_character(data: dict = Body()):
    conn = get_db()
    conn.execute("""
        INSERT INTO characters (name, breathing_style, rank, affiliation, actor_id)
        VALUES (?, ?, ?, ?, ?)
    """, (
        data["name"],
        data["breathing_style"],
        data["rank"],
        data["affiliation"],
        data["actor_id"]
    ))
    conn.commit()
    conn.close()
    return {"message": "Character added successfully"}