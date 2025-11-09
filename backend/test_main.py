import pytest
from fastapi.testclient import TestClient
import os
import json

# Importamos la app de FastAPI desde nuestro archivo main.py
from main import app, DB_FILE

# Creamos un cliente de prueba
client = TestClient(app)

# --- Fixture de Pytest ---
@pytest.fixture(autouse=True)
def setup_and_teardown():
    """
    Esta función se ejecuta antes de CADA prueba.
    Limpia el archivo de estadísticas para que cada prueba
    empiece desde cero.
    """
    db_data = {
        "total_por_categoria": {},
        "ultimas_5": [],
        "fecha_ultima_prediccion": None
    }
    with open(DB_FILE, 'w') as f:
        json.dump(db_data, f)

    yield # Esto es donde se ejecuta la prueba

    # Opcional: Limpiar después, aunque ya lo hacemos antes
    os.remove(DB_FILE)

# --- PRUEBA UNITARIA 1 ---
def test_prediccion_terminal():
    """
    Prueba que, dados los parámetros correctos, la respuesta
    del modelo es ENFERMEDAD TERMINAL.
    """
    response = client.post(
        "/predecir/",
        json={"fiebre": True, "dolor": "Agudo", "cambios_piel": True}
    )
    assert response.status_code == 200
    assert response.json() == {"estado_predicho": "ENFERMEDAD TERMINAL"}

# --- PRUEBA UNITARIA 2 ---
def test_estadisticas_actualizadas():
    """
    Prueba que, después de hacer una predicción, el endpoint
    de estadísticas retorna los datos actualizados.
    """
    # 1. Hacemos una predicción
    client.post(
        "/predecir/",
        json={"fiebre": False, "dolor": "No", "cambios_piel": False}
    )

    # 2. Pedimos las estadísticas
    response = client.get("/estadisticas/")

    # 3. Verificamos que todo esté correcto
    assert response.status_code == 200
    stats = response.json()

    assert stats["total_por_categoria"]["NO ENFERMO"] == 1
    assert len(stats["ultimas_5"]) == 1
    assert stats["ultimas_5"][0]["prediccion"] == "NO ENFERMO"