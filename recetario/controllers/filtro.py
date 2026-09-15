import web
import sqlite3

render = web.template.render('recetario/views/')

class Filtro:
    def GET(self):
        categoria = web.input(categoria="").categoria
        recetas = []
        if categoria:
            conn = sqlite3.connect("recetario.db")
            recetas = conn.execute(
                "SELECT nombre, ingredientes FROM recetas WHERE categoria=?",
                (categoria,)
            ).fetchall()
            conn.close()
        return render.filtro(categoria, recetas)
    