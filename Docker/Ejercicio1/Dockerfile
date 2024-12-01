##Utiliza la imagen oficial de Python basada en la versión 3.9-slim,
## una versión ligera que contiene lo mínimo necesario para ejecutar Python.
FROM python:3.9-slim

##Define el directorio /app como el lugar donde se ejecutarán los comandos dentro del contenedor.
##Este directorio actúa como el espacio de trabajo.
WORKDIR /app

##Copia el archivo requirements.txt (que contiene las dependencias de Python) al directorio /app.
COPY requirements.txt ./

##Ejecuta pip install para instalar las dependencias listadas en requirements.txt.
##La opción --no-cache-dir evita guardar archivos temporales, reduciendo el tamaño de la imagen.
RUN pip install --no-cache-dir -r requirements.txt

##Copia todo el contenido del directorio actual (el proyecto) al directorio /app dentro del contenedor.
COPY . .

##Indica que la aplicación utiliza el puerto 5000, que será accesible fuera del contenedor.

EXPOSE 5000

##Define el comando para iniciar la aplicación Flask: ejecuta el archivo app.py utilizando Python.
CMD ["python", "app.py"]



## en el terminal ejecutamos desde la carpeta actual (docker build -t app-back .) y verificamos que está instalado
## la imagen

## para ejecutar el contenedor (docker run -d -p 5000:5000 --name app-back-container app-back)
## Para visualizar si el contenedor fue creado, en extensiones buscamos docker
## nos damos cuenta que se tenía que actualizar el Flask==3.1.0 cuand ejecutamos pip freeze
##El comando pip freeze se utiliza en Python para listar todas las dependencias instaladas en el entorno actual junto con sus versiones específicas
## eliminamos el docker imagen y el contenedor y volvemos a contruir
##....
## Para explorar más el container le damos anticlick en el container y elegimos
## execute in bash y ejecutamos ls, es como un servidor de linux