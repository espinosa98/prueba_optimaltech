# Usamos una imagen base de Python 3.6
FROM python:3.6-slim

# Establecemos el directorio de trabajo
WORKDIR /app

# Configuramos la variable de entorno para evitar errores de buffering
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN pip install --upgrade pip
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

# Copiamos todo el código del proyecto
COPY . /app

ENTRYPOINT ["gunicorn", "project_optimaltech.wsgi"]
