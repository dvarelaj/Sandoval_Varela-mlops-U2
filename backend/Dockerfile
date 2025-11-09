# 1. Imagen base: Usamos una imagen oficial de Python ligera
FROM python:3.10-slim

# 2. Directorio de trabajo: Creamos un directorio dentro del contenedor
WORKDIR /app

# 3. Instalar dependencias:
# Copiamos SOLO el archivo de requisitos primero
COPY requirements.txt .
# Instalamos las librerías (FastAPI y Uvicorn)
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar el código de la aplicación:
# Copiamos todos los archivos de nuestro proyecto (main.py y diagnostico.py)
COPY . .

# 5. Exponer el puerto:
# Le decimos a Docker que la app se ejecutará en el puerto 8000
EXPOSE 8000

# 6. Comando de ejecución:
# El comando para iniciar el servidor Uvicorn cuando el contenedor arranque
# --host 0.0.0.0 es crucial para que sea accesible desde fuera del contenedor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]