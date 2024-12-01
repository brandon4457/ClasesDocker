
#Se importa la clase Flask del módulo flask, que es la base para crear aplicaciones web.
from flask import Flask

##Aquí se crea una instancia de Flask, que representa la aplicación web.
##__name__ le dice a Flask dónde buscar recursos como plantillas y archivos estáticos.
app = Flask(__name__)

##La anotación @app.route("/") define la ruta principal de la aplicación, que se ejecuta al visitar http://localhost:5000/.
@app.route("/")

##La función hello() es el controlador que gestiona las solicitudes a esta ruta.
def hello():
    return 'Hola Mundo'

##Cuando un usuario accede a la ruta "/", Flask devuelve la respuesta Hola Mundo.

if __name__ =='__main__':
    app.run(host='0.0.0.0', port=5000)

###Si ejecutas este archivo directamente, Flask iniciará un servidor web de desarrollo.
##host='0.0.0.0': Hace que la aplicación esté disponible desde cualquier red local.
##port=5000: Especifica que el servidor escuchará en el puerto 5000.