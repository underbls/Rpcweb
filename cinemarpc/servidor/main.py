from spyne import Application, rpc, ServiceBase, Iterable, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import create_engine, select, MetaData, Table
import pymysql


class serviciosRPC(ServiceBase):
#Clase principal, donde se inician los servicios
    """docstring fo RPCService."""

    #Servicio Login, recibe datos del cl va a db y entrega respuesta:
    @rpc(Unicode, Unicode, _returns=Unicode)
    def log_user(ctx,name,passs):
        #recibir datos:
        print(name)
        print(passs)
        #conectar a db:
        engine = create_engine("mysql://root@localhost/prueba")
        metadata = MetaData(bind=None)
        table = Table('usuarios', metadata, autoload = True, autoload_with = engine)
        #query:
        #stmt = select([table]).where(table.columns.column_name == 'filter')
        stmt = select([table])
        #.where(table.columns.nombre == 'name' and table.columns.contrasena == 'passs')
        connection = engine.connect()
        results = connection.execute(stmt).fetchall()
        #print(results)
        #for result in results:
        for result in results:
            print('resultado de la consulta',result[1])

            if  result[1] == name:

                return ('Login correcto')
            else:
                return ('Login incorrecto')

        #revisar resultados
        #usar resultados
        #respuesta del servidor


    #Listar peliculas
    @rpc(Unicode, Unicode, _returns = Unicode)
    def list_hello(ctx, name_movie, date_p):

        peliculas = []
        #recibir datos:
        print(name_movie)
        print(date_p)
        #conectar a db:
        engine = create_engine("mysql://root@localhost/prueba")
        metadata = MetaData(bind=None)
        table = Table('peliculas', metadata, autoload = True, autoload_with = engine)
        #query:
        stmt = select([table])
        connection = engine.connect()
        results = connection.execute(stmt).fetchall()
        #for result in results:
        for result in results:
            print('resultado de la consulta',result)

        while result.next():
            peliculas.add(
                result.getInt("id"),
                peliculas.GetString("nombre_p"),
                peliculas.getString("fecha_e")

                )


            return('fui a db, obtuve:',peliculas)








application = Application([serviciosRPC],'spyne.examples.hello.soap',
                                            in_protocol=Soap11(validator='lxml'),
                                            out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

#codigo para iniciar el servidor
if __name__ == '__main__':
    import logging
    from wsgiref.simple_server import make_server

    logging.basicConfig(level=logging.DEBUG)

    server = make_server('127.0.0.1',8000,wsgi_application)
    server.serve_forever()
