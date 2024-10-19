# Usamos una imagen base de Python 3.6
FROM python:3.6-slim

# Establecemos el directorio de trabajo
WORKDIR /app

# Copiamos el archivo de requisitos y lo instalamos
COPY requirements.txt .

# Instalamos las dependencias necesarias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiamos todo el código del proyecto
COPY . .

# Configuramos la variable de entorno para evitar errores de buffering
ENV PYTHONUNBUFFERED 1

# Copiamos el script de entrada
COPY entrypoint.sh .

# Hacemos que el script de entrada sea ejecutable
RUN chmod +x entrypoint.sh

# Exponemos el puerto 8000 para que el servidor de Django sea accesible
EXPOSE 8000

# Establecemos el script de entrada como el punto de entrada
ENTRYPOINT ["./entrypoint.sh"]

# Establecemos el comando para ejecutar el servidor de Django
CMD ["gunicorn", "project_optimaltech.wsgi:application", "--bind", "0.0.0.0:8000"]
