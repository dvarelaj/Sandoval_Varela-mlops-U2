def predecir_estado(fiebre: bool, dolor: str, cambios_piel: bool):
    """
    Predice el estado de un paciente basado en tres síntomas.
   

    Argumentos:
    fiebre (bool): True si el paciente tiene fiebre, False si no.
    dolor (str): Nivel de dolor ('No', 'Leve', 'Agudo').
    cambios_piel (bool): True si hay cambios en la piel, False si no.

    Retorna:
    str: El estado predicho.
    """
    
    # --- Lógica de decisión ---

    # Lógica para ENFERMEDAD TERMINAL (Nueva)
    if fiebre and dolor == "Agudo" and cambios_piel:
        return "ENFERMEDAD TERMINAL"
    
  # Lógica existente (la ajustamos un poco para que no se pise)
    if dolor == "Agudo" and not cambios_piel:
        return "ENFERMEDAD AGUDA"
    if fiebre and not (dolor == "Agudo"):
        return "ENFERMEDAD LEVE"
    if cambios_piel and not (dolor == "Agudo"):
        return "ENFERMEDAD CRÓNICA"

    return "NO ENFERMO"

# --- Bloque para probar la función ---
# Esto solo se ejecuta si corres este archivo directamente
if __name__ == "__main__":
    
    # Caso 1: Sin síntomas
    paciente1 = predecir_estado(fiebre=False, dolor='No', cambios_piel=False)
    print(f"Paciente 1 (Sin síntomas): {paciente1}") # Esperado: NO ENFERMO

    # Caso 2: Resfriado común
    paciente2 = predecir_estado(fiebre=True, dolor='Leve', cambios_piel=False)
    print(f"Paciente 2 (Resfriado): {paciente2}") # Esperado: ENFERMEDAD LEVE

    # Caso 3: Apendicitis
    paciente3 = predecir_estado(fiebre=True, dolor='Agudo', cambios_piel=False)
    print(f"Paciente 3 (Apendicitis): {paciente3}") # Esperado: ENFERMEDAD AGUDA

    # Caso 4: Varicela
    paciente4 = predecir_estado(fiebre=True, dolor='Leve', cambios_piel=True)
    print(f"Paciente 4 (Varicela): {paciente4}") # Esperado: ENFERMEDAD AGUDA

    # Caso 5: Psoriasis
    paciente5 = predecir_estado(fiebre=False, dolor='Leve', cambios_piel=True)
    print(f"Paciente 5 (Psoriasis): {paciente5}") # Esperado: ENFERMEDAD CRÓNICA