# Imagen de sistema operativo para el servidor que permitira la instalacion de Python y Jupyter Notebook
FROM ubuntu:20.04

# Se configua el sistema operativo para que no tenga la forma grafica
ENV DEBIAN_FRONTEND=noninteractive

# Actualizar el sistema operativo
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    build-essential \
    wget \
    postgresql postgresql-contrib \
    gnupg \
    && apt-get clean

RUN mkdir -p /etc/apt/keyrings && \
    wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | gpg --dearmor | tee /etc/apt/keyrings/mongodb.gpg > /dev/null && \
    echo "deb [ arch=amd64,arm64 signed-by=/etc/apt/keyrings/mongodb.gpg ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/6.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-6.0.list

RUN apt-get update && apt-get install -y mongodb-org && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip && \
    pip3 install notebook mysql-connector-python psycopg2-binary pymongo

# Crear el Workspace de trabajo
WORKDIR /workspace

# Crear directorio de configuracion de Jupyter
RUN mkdir -p /root/.jupyter

# Añadir el archivo de configuración de Jupyter 
RUN echo "c.NotebookApp.token = ''" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.password = ''" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.open_browser = False" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.allow_root = True" >> /root/.jupyter/jupyter_notebook_config.py

# Habilitar los puertos a utilizar
EXPOSE 8888 3306 5432 27017

CMD ["bash", "-c", "service mysql start && service postgresql start && mongo --fork --logpath /var/log/mongodb.log && jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow_root"]
