# Usamos una imagen base de Python 3.6
FROM python:3.6-slim

# Configuramos la variable de entorno para evitar errores de buffering
ENV PYTHONUNBUFFERED 1

# Crear ambiente virtual
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Establecemos el directorio de trabajo
WORKDIR /app

# Copiamos el archivo de requisitos y lo instalamos
COPY requirements.txt .

# Instalamos las dependencias necesarias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiamos todo el código del proyecto
COPY . .

# Exponemos el puerto 8000 para que el servidor de Django sea accesible
EXPOSE 8000

# Ejecutamos las migraciones y luego corremos el servidor de Django
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

