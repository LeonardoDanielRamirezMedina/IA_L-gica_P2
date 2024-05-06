#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Representar el Conocimiento
# Tema: Razonamiento por Defecto y No Monotónico

# el razonamiento por defecto y no monotónico son enfoques que permiten realizar inferencias lógicas y tomar decisiones basadas en reglas y hechos

# Sistema de diagnóstico médico con incertidumbre
def diagnosticar_enfermedad(síntomas):  # función que diagnostica una enfermedad basada en los síntomas del paciente
    if "fiebre" in síntomas and "dolor de cabeza" in síntomas:  
        return "Migraña", 0.8   # si el paciente tiene fiebre y dolor de cabeza, se diagnostica migraña con una certeza del 80%
    elif "fiebre" in síntomas:
        return "Gripe", 0.6 # si el paciente tiene fiebre, se diagnostica gripe con una certeza del 60%
    elif "dolor de cabeza" in síntomas:
        return "Cefalea", 0.4   # si el paciente tiene dolor de cabeza, se diagnostica cefalea con una certeza del 40%
    else:
        return "No se pudo determinar la enfermedad", 0.0   # en caso contrario, no se puede determinar la enfermedad con certeza

síntomas_paciente = ["fiebre", "dolor de cabeza"]   # síntomas del paciente
enfermedad, certeza = diagnosticar_enfermedad(síntomas_paciente)    # se diagnostica la enfermedad y se obtiene la certeza
print("El paciente tiene:", enfermedad)  # se imprime la enfermedad diagnosticada
print("Certeza:", certeza)  # se imprime la certeza del diagnóstico
