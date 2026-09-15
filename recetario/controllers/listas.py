import web
import sqlite3

render = web.template.render('recetario/views/')

class Listas:
    def GET(self):
        conn = sqlite3.connect("recetario.db")
        recetas = conn.execute("SELECT nombre, ingredientes, categoria FROM recetas").fetchall()
        conn.close()
        return render.listas(recetas)
    