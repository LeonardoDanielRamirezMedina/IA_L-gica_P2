#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Lógica Proposicional
# Tema: Algoritmos de Búsqueda Local

# Los algoritmos de búsqueda local son métodos heurísticos para resolver problemas de optimización que buscan mejorar iterativamente una solución inicial mediante movimientos locales.

# La función objetivo es la función que queremos maximizar o minimizar.
# En este caso, queremos encontrar el valor de x que minimiza -x^2.
def funcion_objetivo(x):
    return -x**2

# El algoritmo de Hill Climbing es un algoritmo de búsqueda local que comienza con una solución arbitraria a un problema,
# luego intenta encontrar una mejor solución variando incrementalmente un solo elemento de la solución.
def hill_climbing(funcion_objetivo, x_inicial, paso, iteraciones_maximas):
    # Comenzamos con un valor inicial de x.
    x_actual = x_inicial

    # Realizamos un número máximo de iteraciones.
    for _ in range(iteraciones_maximas):
        # Calculamos los valores de x a la izquierda y a la derecha del valor actual, con un cierto paso.
        x_izquierda = x_actual - paso
        x_derecha = x_actual + paso

        # Si la función objetivo en x_actual es mayor o igual que en los puntos a su alrededor,
        # entonces hemos encontrado un máximo local y retornamos x_actual.
        if funcion_objetivo(x_izquierda) <= funcion_objetivo(x_actual) >= funcion_objetivo(x_derecha):
            return x_actual
        # Si la función objetivo es mayor en x_izquierda, entonces movemos x_actual a x_izquierda.
        elif funcion_objetivo(x_izquierda) > funcion_objetivo(x_actual):
            x_actual = x_izquierda
        # Si la función objetivo es mayor en x_derecha, entonces movemos x_actual a x_derecha.
        else:
            x_actual = x_derecha

    # Si no encontramos un máximo después del número máximo de iteraciones, retornamos el último valor calculado de x.
    return x_actual

# Ejecutamos el algoritmo de Hill Climbing con un valor inicial de x de 0, un paso de 0.01 y un máximo de 1000 iteraciones.
x_inicial = 10
paso = 0.01
iteraciones_maximas = 1000
print(hill_climbing(funcion_objetivo, x_inicial, paso, iteraciones_maximas))
