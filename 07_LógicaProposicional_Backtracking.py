#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Lógica Proposicional
# Tema: Backtracking

# El backtracking es una estrategia para encontrar soluciones a algunos problemas computacionales, notablemente en búsqueda y problemas de restricción, por probar sistemáticamente todas las soluciones posibles de un problema.
# Si la solución candidata propuesta no es válida, se descarta y se retrocede a la anterior.

# El problema de las N reinas consiste en colocar N reinas en un tablero de ajedrez NxN de tal manera que ninguna reina amenace a otra.

def es_seguro(tablero, fila, col, n):
    # Verificar la fila en el lado izquierdo
    for i in range(col):
        if tablero[fila][i] == 1:
            return False

    # Verificar la diagonal superior izquierda
    for i, j in zip(range(fila, -1, -1), range(col, -1, -1)):
        if tablero[i][j] == 1:
            return False

    # Verificar la diagonal inferior izquierda
    for i, j in zip(range(fila, n, 1), range(col, -1, -1)):
        if tablero[i][j] == 1:
            return False

    return True

def resolver_n_reinas(tablero, col, n):
    # Si todas las reinas están colocadas, retornar verdadero
    if col >= n:
        return True

    # Colocar esta reina en todas las filas una por una
    for i in range(n):
        if es_seguro(tablero, i, col, n):
            # Colocar esta reina en la celda del tablero[i][col]
            tablero[i][col] = 1

            # Recursión para colocar el resto de las reinas
            if resolver_n_reinas(tablero, col + 1, n):
                return True

            # Si colocar la reina en la celda del tablero[i][col] no conduce a una solución, entonces quitar la reina de la celda del tablero[i][col]
            tablero[i][col] = 0

    # Si la reina no puede ser colocada en ninguna fila en esta columna col, retornar falso
    return False

def n_reinas(n):
    tablero = [[0]*n for _ in range(n)]

    if not resolver_n_reinas(tablero, 0, n):
        print("No existe solución")
        return

    for i in range(n):
        for j in range(n):
            print(tablero[i][j], end=" ")
        print()

# Ejecutamos el algoritmo con un tablero de 4x4
n_reinas(4)