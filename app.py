from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

from recetario.controllers import index, filtro, listas


class Manejador(BaseHTTPRequestHandler):

    def do_GET(self):
        partes = urlparse(self.path)
        ruta = partes.path
        parametros = parse_qs(partes.query)

        if ruta == "/filtro":
            categoria = parametros.get("categoria", ["todas"])[0]
            pagina = filtro.renderizar(categoria)
        elif ruta == "/listas":
            pagina = listas.renderizar_formulario()
        else:
            pagina = index.renderizar()

        self._responder_html(pagina)

    def do_POST(self):
        if self.path == "/listas":
            longitud = int(self.headers["Content-Length"])
            datos = self.rfile.read(longitud).decode("utf-8")
            campos = parse_qs(datos)

            nombre = campos.get("nombre", [""])[0].strip()
            categoria = campos.get("categoria", [""])[0]

            listas.agregar_receta(nombre, categoria)

            # Despues de agregar, regresa a la pagina principal
            self.send_response(303)
            self.send_header("Location", "/")
            self.end_headers()

    def _responder_html(self, contenido):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(contenido.encode("utf-8"))


if __name__ == "__main__":
    listas.inicializar_db()  # crea recetario.db la primera vez, usando sql/script.sql
    servidor = HTTPServer(("localhost", 8000), Manejador)
    print("Servidor corriendo en http://localhost:8000")
    servidor.serve_forever()
    