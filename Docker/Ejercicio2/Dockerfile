## vamos a descargar python y notebook de ubuntu
FROM ubuntu:20.04


## para que solamente manejemos este contenedor con terminal
ENV DEBIAN_FRONTEND=noninteractive


## actualizamos los paquetes del servidor y forzamos a yes siempre e instalar lo necesario para el contenedor

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \ 
    build-essential \ 
    wget \
    && apt-get clean


## pip actualizado e instalamos notebook
RUN pip3 install --upgrade pip && \
    pip3 install notebook

    ## creamos la carpeta dentro del contenedor 
WORKDIR /workspace


## directorio de configuracion de jupyter

RUN mkdir -p /root/.jupyter

# Añadir el archivo de configuración de Jupyter 
RUN echo "c.NotebookApp.token = ''" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.password = ''" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.open_browser = False" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.allow_root = True" >> /root/.jupyter/jupyter_notebook_config.py
  
    
    ##Al jupyternotebook ingresamos con el puerto:

EXPOSE 8888

## comando para iniciar el jupyiter notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]