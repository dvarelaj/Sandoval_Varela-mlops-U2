Proyecto Taller: API de Diagnóstico (Full Stack)
Este proyecto es una solución "full stack" que utiliza Docker para desplegar dos servicios:

**Back-End (mi-servicio-api): Una API creada con FastAPI que recibe síntomas (fiebre, dolor, cambios de piel) y retorna una predicción de estado.

**Front-End (mi-servicio-front): Una interfaz web creada con Streamlit que permite al usuario interactuar con la API de forma visual.

Ambos servicios se comunican a través de una red interna de Docker (mi-taller-net).

Estructura del Proyecto
/Proyectos/

├── mi-taller-docker/ (Carpeta del Back-End - FastAPI)

└── mi-taller-front/ (Carpeta del Front-End - Streamlit)

Cómo Desplegar la Solución Completa (Desde Cero)
Sigue estos pasos desde tu terminal.

1. Inicia Docker Desktop
Asegúrate de que la aplicación Docker Desktop esté abierta y corriendo en tu Mac.

2. Crea la Red de Docker
Esta red permite que el front-end y el back-end se comuniquen. (Solo necesitas hacer esto una vez).
```bash
docker network create mi-taller-net
```
3. Construye el Back-End (API)

Navega a la carpeta del back-end:

```bash
    # Reemplaza la línea de abajo con la ruta a la carpeta en tu máquina
    cd backend
 ```
Construye la imagen de la API:
```bash
docker build -t api-diagnostico .
```
4. Construye el Front-End (Streamlit)
Navega a la carpeta del front-end:
```bash
    # Reemplaza la línea de abajo con la ruta a la carpeta en tu máquina
    cd frontend
```
Construye la imagen de la interfaz:
```bash
docker build -t front-diagnostico .
```
5. Inicia ambos servicios
Importante: Si reinicias tu Mac, solo necesitas repetir este paso 5.

Lanza el Back-End:
(Limpia por si acaso) 
```bash
docker rm -f mi-servicio-api
```

(Lanza el contenedor) 
```bash
docker run -d -p 8000:8000 --network mi-taller-net --name mi-servicio-api api-diagnostico
```
Lanza el Front-End:

(Limpia por si acaso) 
```bash
docker rm -f mi-servicio-front
```

(Lanza el contenedor) 
```bash
docker run -d -p 8501:8501 --network mi-taller-net --name mi-servicio-front front-diagnostico
```

6. ¡Usa la Aplicación!
Ahora tienes dos servicios corriendo:

Para usar la aplicación web (Front-End): Abre tu navegador y ve a: http://localhost:8501

Para probar la API directamente (Back-End): Abre tu navegador y ve a: http://localhost:8000/docs

(Opcional) Cómo detener todo
Para apagar ambos servicios, ejecuta:
```bash
docker stop mi-servicio-api mi-servicio-front
```

