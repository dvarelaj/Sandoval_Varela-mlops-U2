import streamlit as st
import requests

st.title('🩺 Predicción de Estado del Paciente')
st.write('Esta app consume la API de FastAPI para predecir el estado de un paciente.')

# --- Entradas del Usuario ---
st.subheader('Por favor, ingrese los síntomas:')

# Usamos st.checkbox para valores True/False
fiebre = st.checkbox('¿Tiene fiebre?')
cambios_piel = st.checkbox('¿Tiene cambios en la piel?')

# Usamos st.selectbox para opciones definidas
dolor = st.selectbox(
    'Nivel de dolor:',
    ('No', 'Leve', 'Agudo')
)

# --- Botón para enviar a la API ---
if st.button('Predecir Estado'):
    # 1. Prepara los datos para enviar
    payload = {
        "fiebre": fiebre,
        "dolor": dolor,
        "cambios_piel": cambios_piel
    }

    # 2. Llama a la API de FastAPI
    # Usamos el nombre del contenedor 'mi-servicio-api' como el host
    # Esto solo funciona porque están en la misma red Docker.
    try:
        response = requests.post(
            "http://mi-servicio-api:8000/predecir/",
            json=payload
        )

        # 3. Muestra el resultado
        if response.status_code == 200:
            resultado = response.json()
            estado = resultado.get('estado_predicho', 'Error')

            # Nueva Lógica de display
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
        st.error("Error de Conexión: No se pudo conectar a la API. ¿Está corriendo el contenedor 'mi-servicio-api'?")