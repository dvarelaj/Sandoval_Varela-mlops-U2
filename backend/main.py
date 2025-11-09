from fastapi import FastAPI
from pydantic import BaseModel
from diagnostico import predecir_estado  # <-- ¡Importamos tu función!

# 1. Crea la aplicación de FastAPI
# ¡ESTA ES LA LÍNEA QUE FALTABA O ESTABA INCORRECTA!
app = FastAPI()

# 2. Define el formato de los datos de entrada
class SintomasPaciente(BaseModel):
    fiebre: bool
    dolor: str  # Esperará 'No', 'Leve' o 'Agudo'
    cambios_piel: bool

# 3. Define el punto final (endpoint) de la API
@app.post("/predecir/")
def api_predecir(sintomas: SintomasPaciente):
    """
    Recibe los síntomas en formato JSON y retorna
    el estado predicho del paciente.
    """

    # Llama a tu función original con los datos recibidos
    resultado = predecir_estado(
        fiebre=sintomas.fiebre,
        dolor=sintomas.dolor,
        cambios_piel=sintomas.cambios_piel
    )

    # Retorna el resultado en un JSON
    return {"estado_predicho": resultado}

# (Opcional) Un endpoint de bienvenida para probar
@app.get("/")
def leer_raiz():
    return {"mensaje": "API de predicción de estado de paciente"}