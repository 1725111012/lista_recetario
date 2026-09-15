import os
import sqlite3

RUTA_BASE = os.path.join(os.path.dirname(__file__), "..", "..")
RUTA_DB = os.path.join(RUTA_BASE, "recetario.db")
RUTA_SCRIPT_SQL = os.path.join(RUTA_BASE, "sql", "script.sql")
RUTA_VIEWS = os.path.join(os.path.dirname(__file__), "..", "views")

CATEGORIAS = ["salado", "dulce", "agridulce", "picoso", "pastas", "aderezos", "cortes", "mariscos"]


def _conectar():
    return sqlite3.connect(RUTA_DB)


def inicializar_db():
    """Si la base de datos no existe todavia, la crea corriendo sql/script.sql"""
    if os.path.exists(RUTA_DB):
        return
    conexion = _conectar()
    with open(RUTA_SCRIPT_SQL, encoding="utf-8") as archivo:
        conexion.executescript(archivo.read())
    conexion.commit()
    conexion.close()


def obtener_categorias():
    return CATEGORIAS


def obtener_recetas():
    """Trae todas las recetas guardadas en la base de datos."""
    conexion = _conectar()
    cursor = conexion.execute("SELECT nombre, categoria, descripcion FROM recetas")
    filas = cursor.fetchall()
    conexion.close()
    return [{"nombre": f[0], "categoria": f[1], "descripcion": f[2]} for f in filas]


def filtrar_por_categoria(categoria):
    """Trae solo las recetas de la categoria pedida (filtro hecho con SQL)."""
    conexion = _conectar()
    cursor = conexion.execute(
        "SELECT nombre, categoria, descripcion FROM recetas WHERE categoria = ?",
        (categoria,),
    )
    filas = cursor.fetchall()
    conexion.close()
    return [{"nombre": f[0], "categoria": f[1], "descripcion": f[2]} for f in filas]


def agregar_receta(nombre, categoria, descripcion=""):
    """Inserta una receta nueva en la base de datos."""
    if not nombre or categoria not in CATEGORIAS:
        return
    conexion = _conectar()
    conexion.execute(
        "INSERT INTO recetas(nombre, categoria, descripcion) VALUES (?, ?, ?)",
        (nombre, categoria, descripcion),
    )
    conexion.commit()
    conexion.close()


def _leer_view(nombre_archivo):
    ruta = os.path.join(RUTA_VIEWS, nombre_archivo)
    with open(ruta, encoding="utf-8") as archivo:
        return archivo.read()


def renderizar_formulario():
    """Arma la pagina con el formulario para agregar una receta nueva."""
    opciones = "".join(f'<option value="{c}">{c.capitalize()}</option>' for c in CATEGORIAS)
    html = _leer_view("listas.html")
    html = html.replace("{{OPCIONES_CATEGORIA}}", opciones)
    return html
