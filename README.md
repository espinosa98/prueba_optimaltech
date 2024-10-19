# Prueba OptimalTech

Este proyecto es una aplicación Django que utiliza SQLite como base de datos y está diseñada para ejecutarse dentro de un contenedor Docker.



## Instalación Docker

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/espinosa98/prueba_optimaltech.git
   cd prueba_optimaltech
   ```

2. **Construye la imagen de Docker:**

   ```bash
   docker build -t optimaltech .
   ```

3. **Ejecuta el contenedor:**

   ```bash
   docker run --name optimaltech_container -p 8000:8000 optimaltech
   ```

4. **Accede a la aplicación:**

   Abre tu navegador y ve a `http://localhost:8000`.

## Instalación Local

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/espinosa98/prueba_optimaltech.git
   cd prueba_optimaltech
   ```

2. **Crea y activa un entorno virtual:**

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Instala las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Realiza las migraciones de la base de datos:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Ejecuta el servidor de desarrollo:**

   ```bash
   python manage.py runserver
   ```

6. **Accede a la aplicación:**

   Abre tu navegador y ve a `http://localhost:8000`.
```
