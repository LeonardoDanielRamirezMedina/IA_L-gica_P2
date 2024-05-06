#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Representar el Conocimiento
# Tema: Sistemas Expertos

# los sistemas expertos son enfoques que permiten representar el conocimiento de expertos en un dominio específico para realizar tareas de razonamiento y toma de decisiones

# Sistema experto para recomendación de carreras
def recomendar_carrera(aptitudes):  # función que recomienda una carrera basada en las aptitudes del estudiante
    if aptitudes["matemáticas"] > 8 and aptitudes["ciencias"] > 7:  
        return "Ingeniería" # si el estudiante tiene aptitudes en matemáticas y ciencias, se recomienda Ingeniería
    elif aptitudes["creatividad"] > 8 and aptitudes["arte"] > 7:
        return "Arquitectura"   # si el estudiante tiene aptitudes en creatividad y arte, se recomienda Arquitectura
    else:
        return "No se pudo determinar una carrera recomendada"  # en caso contrario, no se puede determinar una carrera recomendada

aptitudes_estudiante = {    # se crea un diccionario con las aptitudes del estudiante
    "matemáticas": 9,   
    "ciencias": 8,
    "creatividad": 7,
    "arte": 9
}

print("Carrera recomendada:", recomendar_carrera(aptitudes_estudiante)) # se imprime la carrera recomendada
