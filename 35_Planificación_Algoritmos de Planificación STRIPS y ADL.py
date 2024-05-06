#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Planificación
# Tema: Algoritmos de Planificación: STRIPS y ADL

# los algoritmos de planificación son una forma de automatizar la generación de planes para lograr un objetivo dado.

# La clase Estado representa el estado del mundo, en este caso las condiciones de las habitaciones.
class Estado:
    # El constructor inicializa el estado. Si no se proporciona un estado inicial, se usa un estado predeterminado.
    def __init__(self, habitaciones=None):
        self.habitaciones = habitaciones if habitaciones is not None else {"cocina": "limpia", "sala": "ordenada", "dormitorio": "desordenado"}
        #En la linea anterior se inicializan las habitaciones con sus respectivos estados, en este caso, la cocina está limpia, la sala ordenada y el dormitorio desordenado.
    # Este método permite imprimir el estado de manera legible.
    def __str__(self):
        return str(self.habitaciones)

# La clase Accion representa una acción que puede cambiar el estado del mundo.
class Accion:
    # El constructor inicializa la acción con un nombre, precondiciones y efectos.
    def __init__(self, nombre, precondiciones, efectos):
        self.nombre = nombre    #inicializa el nombre de la acción.
        self.precondiciones = precondiciones    #inicializa las precondiciones de la acción.
        self.efectos = efectos  #inicializa los efectos de la acción.

    # Este método permite imprimir la acción de manera legible.
    def __str__(self):
        return self.nombre

# Esta función ejecuta una acción en un estado dado.
def ejecutar_accion(estado, accion):
    # Verifica si las precondiciones de la acción se cumplen en el estado actual.
    for precondicion in accion.precondiciones:
        if precondicion not in estado.habitaciones:
            return "No se puede ejecutar la acción. Faltan precondiciones."
        elif estado.habitaciones[precondicion] != accion.precondiciones[precondicion]:
            return "No se puede ejecutar la acción. Precondiciones no cumplidas."
    # Si las precondiciones se cumplen, aplica los efectos de la acción al estado.
    for efecto in accion.efectos:
        estado.habitaciones[efecto] = accion.efectos[efecto]
    return "Acción ejecutada con éxito."

# Definir estados y acciones
estado_actual = Estado()
mover_sala_cocina = Accion("Moverse a la cocina", {"sala": "ordenada", "cocina": "limpia"}, {"sala": "desordenada"})
limpiar_cocina = Accion("Limpiar la cocina", {"cocina": "desordenada"}, {"cocina": "limpia"})

# Ejemplo de planificación
print("Estado actual:", estado_actual)
print(ejecutar_accion(estado_actual, mover_sala_cocina))
print(ejecutar_accion(estado_actual, limpiar_cocina))
print("Nuevo estado:", estado_actual)