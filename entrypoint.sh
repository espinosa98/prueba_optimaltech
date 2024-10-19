#!/bin/sh

# Ejecuta las migraciones
python manage.py makemigrations
python manage.py migrate

# Inicia la aplicación
exec "$@"
