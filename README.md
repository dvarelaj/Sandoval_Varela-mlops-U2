Proyecto Taller: API de Diagnóstico (Full Stack)
Este proyecto es una solución "full stack" que utiliza Docker para desplegar dos servicios:

**Back-End (mi-servicio-api): Una API creada con FastAPI que recibe síntomas (fiebre, dolor, cambios de piel) y retorna una predicción de estado.

**Front-End (mi-servicio-front): Una interfaz web creada con Streamlit que permite al usuario interactuar con la API de forma visual.

Ambos servicios se comunican a través de una red interna de Docker (mi-taller-net).

Estructura del Proyecto
/Proyectos/

├── mi-taller-docker/ (Carpeta del Back-End - FastAPI)

└── mi-taller-front/ (Carpeta del Front-End - Streamlit)

---

## Cómo Desplegar la Solución Completa (Desde Cero)

Sigue estos pasos desde tu terminal.

### 1. Requisitos
* Tener **Docker Desktop** instalado y en ejecución.
* Haber clonado este repositorio.

### 2. Construir y Ejecutar

Este proyecto usa **Docker Compose v2** para gestionar ambos servicios (backend y frontend).

**Nota:** Docker Desktop usa `docker compose` (con espacio) en lugar de `docker-compose` (con guion).

1.  Navega a la raíz de este proyecto (donde está el archivo `docker-compose.yml`).
2.  Ejecuta el siguiente comando:

    ```bash
    docker compose up -d --build
    ```
* `up`: Crea y levanta los contenedores.
* `-d`: Los ejecuta en segundo plano (detached).
* `--build`: Fuerza a Docker a reconstruir las imágenes con cualquier cambio que hayas hecho.

### 3. ¡Usa la Aplicación!

Ahora tienes dos servicios corriendo:

* **Para usar la aplicación web (Front-End):**
    Abre tu navegador y ve a: **`http://localhost:8501`**

* **Para probar la API directamente (Back-End):**
    Abre tu navegador y ve a: **`http://localhost:8000/docs`**

---

## (Opcional) Cómo detener todo

Para apagar ambos servicios, ejecuta:

```bash
docker compose down
```

