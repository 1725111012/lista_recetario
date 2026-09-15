import os
from . import listas

RUTA_VIEWS = os.path.join(os.path.dirname(__file__), "..", "views")


def _leer_view(nombre_archivo):
    ruta = os.path.join(RUTA_VIEWS, nombre_archivo)
    with open(ruta, encoding="utf-8") as archivo:
        return archivo.read()


def _armar_enlaces_categorias():
    enlaces = '<a href="/">Todas</a> | '
    enlaces += " | ".join(
        f'<a href="/filtro?categoria={c}">{c.capitalize()}</a>' for c in listas.obtener_categorias()
    )
    return enlaces


def _armar_lista_recetas(recetas):
    if not recetas:
        return "<p>No hay recetas en esta categoria.</p>"
    filas = "".join(f"<li><b>{r['nombre']}</b> - {r['categoria'].capitalize()}</li>" for r in recetas)
    return f"<ul>{filas}</ul>"


def renderizar(categoria):
    """Arma la pagina mostrando solo las recetas de esa categoria (filtro via SQL)."""
    html = _leer_view("filtro.html")
    html = html.replace("{{ENLACES_CATEGORIAS}}", _armar_enlaces_categorias())
    html = html.replace("{{CATEGORIA_ACTUAL}}", categoria.capitalize())
    html = html.replace("{{LISTA_RECETAS}}", _armar_lista_recetas(listas.filtrar_por_categoria(categoria)))
    return html
