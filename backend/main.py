from fastapi import FastAPI
from pydantic import BaseModel
from diagnostico import predecir_estado
import json
import datetime
import threading

# --- Configuración de la App ---
app = FastAPI()

# Ruta al archivo de "base de datos"
DB_FILE = "predicciones.json"

# Un "candado" para evitar que dos peticiones escriban en el archivo al mismo tiempo
db_lock = threading.Lock()

# --- Modelos de Datos ---
class SintomasPaciente(BaseModel):
    fiebre: bool
    dolor: str
    cambios_piel: bool

class StatsResponse(BaseModel):
    total_por_categoria: dict
    ultimas_5: list
    fecha_ultima_prediccion: str | None

# --- Funciones de Ayuda ---
def leer_db():
    with db_lock:
        try:
            with open(DB_FILE, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            # Si el archivo no existe, lo crea
            return {"total_por_categoria": {}, "ultimas_5": [], "fecha_ultima_prediccion": None}

def escribir_db(data):
    with db_lock:
        with open(DB_FILE, 'w') as f:
            json.dump(data, f, indent=4)

# --- Endpoints de la API ---
@app.get("/")
def leer_raiz():
    return {"mensaje": "API de predicción de estado de paciente"}

@app.post("/predecir/")
def api_predecir(sintomas: SintomasPaciente):
    """
    Recibe los síntomas, retorna la predicción Y
    ACTUALIZA las estadísticas.
    """

    # 1. Obtener la predicción
    resultado = predecir_estado(
        fiebre=sintomas.fiebre,
        dolor=sintomas.dolor,
        cambios_piel=sintomas.cambios_piel
    )

    # 2. Actualizar la "base de datos"
    db_data = leer_db()

    # Actualiza el total por categoría
    db_data["total_por_categoria"][resultado] = db_data["total_por_categoria"].get(resultado, 0) + 1

    # Actualiza la fecha
    now = datetime.datetime.now().isoformat()
    db_data["fecha_ultima_prediccion"] = now

    # Actualiza las últimas 5 predicciones
    db_data["ultimas_5"].insert(0, {
        "fecha": now,
        "prediccion": resultado,
        "input": sintomas.model_dump()
    })
    db_data["ultimas_5"] = db_data["ultimas_5"][:5] # Mantiene solo las últimas 5

    escribir_db(db_data)

    # 3. Retornar el resultado al usuario
    return {"estado_predicho": resultado}

# --- NUEVO ENDPOINT DE ESTADÍSTICAS ---
@app.get("/estadisticas/", response_model=StatsResponse)
def api_estadisticas():
    """
    Retorna las estadísticas de predicciones.
    """
    db_data = leer_db()
    return db_data