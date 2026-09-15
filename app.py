import web
import sqlite3
import recetario.controllers.index
import recetario.controllers.listas
import recetario.controllers.filtro

urls = (
    '/', 'recetario.controllers.index.Index',
    '/listas', 'recetario.controllers.listas.Listas',
    '/filtro', 'recetario.controllers.filtro.Filtro',
)

app = web.application(urls, globals())

def crear_bd():
    conn = sqlite3.connect("recetario.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS recetas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            ingredientes TEXT,
            categoria TEXT
        )
    """)
    conn.close()

if __name__ == "__main__":
    crear_bd()
    app.run()

    