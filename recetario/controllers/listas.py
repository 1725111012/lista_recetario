import web
import sqlite3

render = web.template.render('views', base='layout')

class Lista_Contacto:

    def buscarContacto(self, id_contacto:int):
        conn = None
        try:
            # Conecta a la base de datos
            conn = sqlite3.connect('sql/agenda.db')
            cursor = conn.cursor()
            # Consulta los registros de la tabla contactos
            query = "SELECT * FROM contactos WHERE id_contacto= ?"
            cursor.execute(query, (id_contacto,))            
            # Crea un array vacio para almacenar los registros
            contactos = []
            # Almacena cada registro en un diccionario
            for row in cursor.fetchall():
                contacto = {
                    'id_contacto': row[0],
                    'nombre': row[1],
                    'primer_apellido': row[2],
                    'segundo_apellido': row[3],
                    'email': row[4],
                    'telefono': row[5]
                }
                # Agrega el diccionario creado al array
                contactos.append(contacto)
        
            return contactos
        except sqlite3.Error as error:
            print(f"ERROR 100: {error.args}")
            return []
        except Exception as error:
            print(f"ERROR 101: {error.args}")
            return []
        finally:
            if conn:
                conn.close()

    # Agregamos este método que le hacía falta a tu clase para que no marque error
    def obtenerContactos(self):
        conn = None
        try:
            conn = sqlite3.connect('sql/agenda.db')
            cursor = conn.cursor()
            query = "SELECT * FROM contactos"
            cursor.execute(query)            
            contactos = []
            for row in cursor.fetchall():
                contacto = {
                    'id_contacto': row[0],
                    'nombre': row[1],
                    'primer_apellido': row[2],
                    'segundo_apellido': row[3],
                    'email': row[4],
                    'telefono': row[5]
                }
                contactos.append(contacto)
            return contactos
        except sqlite3.Error as error:
            print(f"ERROR 102: {error.args}")
            return []
        finally:
            if conn:
                conn.close()

    def GET(self):
        # NOTA: Aquí agregamos los paréntesis () para que ejecute la consulta
        contactos = self.obtenerContactos()
        print(contactos)
        return render.lista_contacto(contactos)
    