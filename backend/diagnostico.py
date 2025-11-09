def predecir_estado(fiebre, dolor, cambios_piel):
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
    
    # 1. ENFERMEDAD AGUDA (Prioridad más alta)
    # Dolor agudo O fiebre + rash 
    if dolor == 'Agudo' or (fiebre == True and cambios_piel == True):
        return 'ENFERMEDAD AGUDA'
    
    # 2. ENFERMEDAD CRÓNICA
    # Cambios en la piel sin fiebre 
    # (Ya sabemos que el dolor no es 'Agudo' por la regla anterior)
    elif cambios_piel == True and fiebre == False:
        return 'ENFERMEDAD CRÓNICA'
        
    # 3. ENFERMEDAD LEVE
    # Fiebre o dolor leve, pero sin las condiciones agudas/crónicas
    elif fiebre == True or dolor == 'Leve':
        return 'ENFERMEDAD LEVE'
        
    # 4. NO ENFERMO
    # Si no es Aguda, ni Crónica, ni Leve, es el caso base.
    else:
        # Esto solo ocurre si fiebre=False, dolor='No', cambios_piel=False
        return 'NO ENFERMO'

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