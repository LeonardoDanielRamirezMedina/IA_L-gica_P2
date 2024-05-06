#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Planificación
# Tema: Planificación Lógica Proposicional: SATPLAN

# La planificación lógica proposicional es un enfoque de planificación que utiliza la lógica proposicional para representar acciones y estados del mundo.

# Se definen las acciones posibles en el sistema, cada acción tiene precondiciones y efectos.
acciones = {'ir_trabajo': {'precondiciones': [], 'efectos': ['ir_trabajo']},
            'trabajar': {'precondiciones': ['ir_trabajo'], 'efectos': ['trabajar']},
            'descansar': {'precondiciones': [], 'efectos': ['descansar']},
            'estudiar': {'precondiciones': [], 'efectos': ['estudiar']},
            'ir_universidad': {'precondiciones': ['descansar'], 'efectos': ['ir_universidad']},
            'clases': {'precondiciones': ['ir_universidad'], 'efectos': ['clases']},
            'estudiar_ingles': {'precondiciones': ['clases'], 'efectos': ['estudiar_ingles']},
            'estudiar_ciencias': {'precondiciones': ['clases'], 'efectos': ['estudiar_ciencias']}}

# Se define el estado actual del sistema, inicialmente todas las acciones están en estado False.
estado_actual = {'ir_trabajo': False, 'trabajar': False, 'descansar': False, 'estudiar': False, 'ir_universidad': False, 'clases': False, 'estudiar_ingles': False, 'estudiar_ciencias': False}

# Se definen los objetivos a alcanzar, en este caso se desea ir al trabajo y trabajar.
objetivos = {'ir_trabajo': True, 'trabajar': True}

# Función para verificar si el estado actual cumple con las precondiciones de una acción.
def verificar_precondiciones(accion, estado):
    return all(estado[precondicion] for precondicion in acciones[accion]['precondiciones'])

# Función para aplicar los efectos de una acción al estado actual.
def aplicar_efectos(accion, estado):
    nuevo_estado = estado.copy()
    for efecto in acciones[accion]['efectos']:
        nuevo_estado[efecto] = True
    return nuevo_estado

# Función de planificación que genera un plan para alcanzar los objetivos a partir del estado actual.
def planificar(estado_actual, objetivos):
    plan = []
    estado = estado_actual.copy()
    while any(not estado[accion] for accion in objetivos):
        acciones_aplicables = [accion for accion in acciones if not estado[accion] and verificar_precondiciones(accion, estado)]
        if not acciones_aplicables:
            return None
        accion_elegida = acciones_aplicables[0]  # Enfoque ingenuo: elegir la primera acción aplicable
        plan.append(accion_elegida)
        estado = aplicar_efectos(accion_elegida, estado)
    return plan

# Se ejecuta la función de planificación y se imprime el plan resultante.
plan = planificar(estado_actual, objetivos)
if plan:
    print("Plan encontrado:", plan)
else:
    print("No se pudo encontrar un plan.")