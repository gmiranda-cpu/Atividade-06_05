import sqlite3

class FilmeRepository:

    def __init__(self):
        self.conn = sqlite3.connect("cinema.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS filme (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            genero TEXT,
            diretor TEXT
        )
        """)

    def salvar(self, filme):

        self.cursor.execute("""
        INSERT INTO filme (titulo, genero, diretor)
        VALUES (?, ?, ?)
        """, (filme.titulo, filme.genero, filme.diretor))

        self.conn.commit()
