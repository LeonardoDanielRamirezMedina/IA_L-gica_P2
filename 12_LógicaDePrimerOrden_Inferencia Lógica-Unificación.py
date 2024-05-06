#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Lógica de 1er Orden
#Tema: Inferencia Lógica: Unificación

# La unificación es un proceso en lógica de primer orden que busca encontrar una sustitución que haga que dos expresiones lógicas sean iguales.

def unificar(expr1, expr2, sustituciones={}):   # Función que unifica dos expresiones lógicas
    if sustituciones is None:   # Si las sustituciones son nulas
        return None  # Retorna nulo
    elif expr1 == expr2:    # Si las expresiones son iguales
        return sustituciones    # Retorna las sustituciones
    elif isinstance(expr1, str) and expr1.islower():    # Si la expresión 1 es una cadena y es minúscula
        return unificar_var(expr1, expr2, sustituciones)    # Retorna la unificación de la variable
    elif isinstance(expr2, str) and expr2.islower():    # Si la expresión 2 es una cadena y es minúscula
        return unificar_var(expr2, expr1, sustituciones)    # Retorna la unificación de la variable
    elif isinstance(expr1, list) and isinstance(expr2, list):   # Si la expresión 1 y la expresión 2 son listas
        return unificar(expr1[1:], expr2[1:], unificar(expr1[0], expr2[0], sustituciones))  # Retorna la unificación de las listas
    else:   
        return None   # Retorna nulo

def unificar_var(var, expr, sustituciones):  # Función que unifica una variable con una expresión
    if var in sustituciones:    # Si la variable está en las sustituciones
        return unificar(sustituciones[var], expr, sustituciones)    # Retorna la unificación de las sustituciones
    elif isinstance(expr, str) and expr in sustituciones:   # Si la expresión es una cadena y está en las sustituciones
        return unificar(var, sustituciones[expr], sustituciones)    # Retorna la unificación de la variable con las sustituciones
    else:
        return {**sustituciones, var: expr}   # Retorna las sustituciones

# Ejemplo de uso
print(unificar(["p", "x", "y"], ["p", "John", "y"]))  # {'x': 'John'}
print(unificar(["p", "x", "y"], ["p", "John", "z"]))  # {'x': 'John', 'y': 'z'} # {'x': 'y'}