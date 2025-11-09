import streamlit as st
import requests
import pandas as pd

# --- Configuración de la Página ---
st.set_page_config(page_title="Predicción de Pacientes", layout="wide")

# URL de la API (usa el nombre del servicio de Docker Compose)
API_URL = "http://backend:8000"

# --- Título ---
st.title('🩺 Predicción de Estado del Paciente')
st.write('Esta app consume la API de FastAPI para predecir el estado de un paciente.')

# --- Columnas Principales ---
col1, col2 = st.columns(2)

with col1:
    st.header("Realizar Predicción")

    # --- Entradas del Usuario ---
    fiebre = st.checkbox('¿Tiene fiebre?')
    cambios_piel = st.checkbox('¿Tiene cambios en la piel?')
    dolor = st.selectbox(
        'Nivel de dolor:',
        ('No', 'Leve', 'Agudo')
    )

    # --- Botón para enviar a la API ---
    if st.button('Predecir Estado'):
        payload = {
            "fiebre": fiebre,
            "dolor": dolor,
            "cambios_piel": cambios_piel
        }

        try:
            response = requests.post(f"{API_URL}/predecir/", json=payload)

            if response.status_code == 200:
                resultado = response.json()
                estado = resultado.get('estado_predicho', 'Error')

                if estado == 'ENFERMEDAD TERMINAL':
                    st.error(f'Resultado: {estado} 💀')
                elif estado == 'ENFERMEDAD AGUDA':
                    st.error(f'Resultado: {estado} 🚨')
                elif estado == 'ENFERMEDAD CRÓNICA':
                    st.warning(f'Resultado: {estado} ⚠️')
                elif estado == 'ENFERMEDAD LEVE':
                    st.info(f'Resultado: {estado} 🤧')
                else:
                    st.success(f'Resultado: {estado} ✅')
            else:
                st.error(f"Error al contactar la API: {response.status_code}")

        except requests.exceptions.ConnectionError:
            st.error("Error de Conexión: No se pudo conectar a la API.")

with col2:
    st.header("Estadísticas")

    # Botón para refrescar las estadísticas
    if st.button("Refrescar Estadísticas"):
        try:
            stats_response = requests.get(f"{API_URL}/estadisticas/")
            if stats_response.status_code == 200:
                stats = stats_response.json()

                st.subheader("Total por Categoría")
                st.bar_chart(stats["total_por_categoria"])

                st.subheader("Última Predicción")
                st.write(stats["fecha_ultima_prediccion"])

                st.subheader("Últimas 5 Predicciones")
                # Convertimos a DataFrame para mostrarlo bonito
                df = pd.DataFrame(stats["ultimas_5"])
                st.dataframe(df)

            else:
                st.error("No se pudieron cargar las estadísticas.")

        except requests.exceptions.ConnectionError:
            st.error("Error de Conexión: No se pudo conectar a la API.")