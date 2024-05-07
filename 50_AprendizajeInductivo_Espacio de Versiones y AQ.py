#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Aprendizaje Inductivo
# Tema: Espacio de Versiones y AQ

# El espacio de versiones es un enfoque de aprendizaje inductivo que representa un conjunto de hipótesis consistentes con los datos de entrenamiento. En este ejemplo, utilizaremos el algoritmo AQ (Algoritmo de Quinlan) para generar el espacio de versiones y predecir si un estudiante aprobará o no un examen en función de las horas de sueño y de estudio.

class VersionSpace: # Clase para representar un ejemplo de datos de entrenamiento
    def __init__(self, h_sueño, h_estudio, aprobado):
        self.h_sueño = h_sueño
        self.h_estudio = h_estudio
        self.aprobado = aprobado

# horas de sueño, horas de estudio y si el estudiante aprobó (1) o no (0) el examen
datos_entrenamiento = [ # Datos de entrenamiento
    VersionSpace(7, 2, 0),  # 7 horas de sueño, 2 horas de estudio, no aprobado
    VersionSpace(8, 1, 0),
    VersionSpace(5, 3, 0),
    VersionSpace(10, 5, 1), # 10 horas de sueño, 5 horas de estudio, aprobado
    VersionSpace(6, 1, 0),
    VersionSpace(9, 4, 1),
    VersionSpace(4, 2, 0),
    VersionSpace(7, 3, 1),
    VersionSpace(8, 5, 1),
    VersionSpace(6, 3, 0)
]

# Implementación del algoritmo AQ para generar el espacio de versiones
def AQ(datos):
    version_space = []
    for dato in datos:
        if dato.aprobado == 1:
            version_space.append(dato)
    return version_space

#espacio de versiones generado con el algoritmo AQ
espacio_versiones = AQ(datos_entrenamiento) # Espacio de versiones generado con el algoritmo AQ

# Función para predecir si un estudiante aprueba o no el examen
def predecir_aprobacion(h_sueño, h_estudio, espacio_versiones): 
    for version in espacio_versiones:   # Recorre el espacio de versiones
        if version.h_sueño == h_sueño and version.h_estudio == h_estudio:   # Si las horas de sueño y de estudio coinciden con las del espacio de versiones
            return "El estudiante probablemente aprobará el examen."
    return "El estudiante probablemente no aprobará el examen."

# predicción para un estudiante con 7 horas de sueño y 3 horas de estudio
print(predecir_aprobacion(7, 3, espacio_versiones))
