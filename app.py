import web

urls = (
    '/', 'controllers.index.Index',
    '/lista_contacto', 'controllers.lista_contacto.Lista_Contacto',
    '/ver_contacto/(.*)', 'controllers.ver_contacto.Ver_contacto',
)



app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
    