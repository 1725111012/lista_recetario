import web
import sqlite3

render = web.template.render('views', base='layout') # Agregamos base='layout' para usar tu layout.html

class Ver_contacto:

    def buscarContacto(self, id_contacto:int):
        try:
            # Conecta a la base de datos
            conn = sqlite3.connect('sql/agenda.db')
            cursor = conn.cursor()
            # Consulta los registros de la tabla contactos
            query = "SELECT * FROM contactos WHERE id_contacto= ?"
            cursor.execute(query, (id_contacto,))            
            
            # Obtenemos la única fila resultante
            row = cursor.fetchone()
            
            # Crea un array vacio para almacenar los registros
            contactos = []
            
            if row:
                # Almacena cada registro en un diccionario
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

            # Cierra la conexion a la base de datos
            conn.close()     
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

    def GET(self,id_contacto):
        print(f"ID_CONTACTO: {id_contacto}")
        contacto = self.buscarContacto(id_contacto)
        print(contacto)

        # Como tu función devuelve una lista, mandamos el primer elemento contacto[0] si existe
        if contacto:
            return render.ver_contacto(contacto[0])
        else:
            return "Contacto no encontrado"