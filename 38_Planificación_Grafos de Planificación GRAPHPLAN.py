#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Planificación
# Tema: Grafos de Planificación: GRAPHPLAN

#los grafos de planificación graphlan son una forma de planificación que utiliza un grafo dirigido acíclico para representar las acciones y estados del mundo.

# Definir acciones y estados iniciales y objetivos
acciones = {    #Se definen las acciones con sus precondiciones y efectos.
    'calentar_agua': {'precondiciones': [], 'efectos': ['agua_caliente']},
    'agregar_te': {'precondiciones': ['agua_caliente'], 'efectos': ['te_agregado']},
    'agregar_azucar': {'precondiciones': ['te_agregado'], 'efectos': ['te_con_azucar']}
}

estado_inicial = {'agua_caliente': False, 'te_agregado': False}   #Se define el estado inicial.
objetivos = {'te_con_azucar': True}  #Se definen los objetivos.

# Funciones para verificar precondiciones y aplicar efectos
def verificar_precondiciones(accion, estado):   #Función para verificar si las precondiciones de una acción se cumplen en un estado dado.
    return all(estado[precondicion] for precondicion in acciones[accion]['precondiciones']) #Retorna True si todas las precondiciones se cumplen.

def aplicar_efectos(accion, estado):    #Función para aplicar los efectos de una acción a un estado dado.
    nuevo_estado = estado.copy()
    for efecto in acciones[accion]['efectos']:
        nuevo_estado[efecto] = True   #Aplica los efectos de la acción al estado.
    return nuevo_estado

# Función para obtener niveles en el grafo de planificación
def obtener_niveles(estado_actual, objetivos, acciones):
    niveles = [[objetivos]]  # El nivel más bajo contiene los objetivos
    while True:
        nivel_actual = []
        for accion, info_accion in acciones.items():
            if all(verificar_precondiciones(accion, estado) for estado in niveles[-1][0]):
                nivel_actual.append(accion)
        if not nivel_actual:  # Si no hay acciones aplicables, detenerse
            return None
        niveles.append([nivel_actual])
        for accion in nivel_actual:  # Aplicar las acciones del nivel actual a un nuevo estado
            nuevo_estado = aplicar_efectos(accion, estado_actual)
            estado_actual.update(nuevo_estado)
        if all(estado_actual[obj] for obj in objetivos):  # Si todos los objetivos están satisfechos, terminar
            return niveles
    return None

# Función para extraer un plan a partir de los niveles del grafo de planificación
def extraer_plan(niveles, acciones):
    plan = []   #se inicializa una lista vacía para almacenar el plan.
    for nivel in reversed(niveles): # Recorre los niveles en orden inverso
        for accion in nivel[0]:
            if not any(accion in acciones[precondicion]['efectos'] for precondicion in acciones[accion]['precondiciones']): # Verificar que la acción no sea redundante
                plan.insert(0, accion)  # Insertar la acción en el plan
    return plan

niveles_planificacion = obtener_niveles(estado_inicial, objetivos, acciones)    #Obtener los niveles del grafo de planificación
if niveles_planificacion:
    plan = extraer_plan(niveles_planificacion, acciones)        #Extraer el plan a partir de los niveles del grafo de planificación.
    print("Plan encontrado:", plan)   #Imprimir el plan encontrado.
else:
    print("No se pudo encontrar un plan.")  #Mensaje si no se encuentra un plan.
