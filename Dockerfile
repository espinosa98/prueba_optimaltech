# Usa una imagen base de Python
FROM python:3.10-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios
COPY requirements.txt .

# Instala virtualenv
RUN pip install --no-cache-dir virtualenv

# Crea un entorno virtual
RUN virtualenv venv

# Activa el entorno virtual y luego instala los requisitos
RUN . venv/bin/activate && pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación
COPY . .

# Expone el puerto de la aplicación
EXPOSE 8000

# Ejecuta las migraciones y luego inicia el servidor
CMD ["sh", "-c", ". venv/bin/activate && python manage.py makemigrations &&  python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
