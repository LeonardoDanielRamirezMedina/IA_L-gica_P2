#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Lógica de 1er Orden
# Tema: Ingeniería del Conocimiento

# En la ingeniería del conocimiento, se utilizan sistemas expertos para modelar y resolver problemas complejos.

class Paciente:
    def __init__(self, fiebre, tos, dificultad_respirar):   # Definimos la clase Paciente con los síntomas como atributos
        self.fiebre = fiebre   # Atributo fiebre  
        self.tos = tos  # Atributo tos  
        self.dificultad_respirar = dificultad_respirar  # Atributo dificultad_respirar

def diagnostico_covid(paciente):    # Función que realiza un diagnóstico de COVID-19 basado en los síntomas del paciente
    if paciente.fiebre and paciente.tos and paciente.dificultad_respirar:   # Si el paciente tiene fiebre, tos y dificultad para respirar
        return "El paciente puede tener COVID-19"   # Se devuelve un mensaje de diagnóstico
    else:
        return "El paciente probablemente no tiene COVID-19"    # Se devuelve un mensaje de diagnóstico

# Creamos un objeto Paciente con los síntomas del paciente
paciente = Paciente(fiebre=True, tos=True, dificultad_respirar=True)

# Realizamos el diagnóstico del paciente
print(diagnostico_covid(paciente))
