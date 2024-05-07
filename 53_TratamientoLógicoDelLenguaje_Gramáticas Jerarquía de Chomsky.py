#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Tratamiento Lógico del Lenguaje
# Tema: Gramáticas: Jerarquía de Chomsky

# Gramática para generar paréntesis balanceados
# S -> (S)S | ε

# Define la función generar_parentesis_balanceados que genera todas las posibles cadenas de paréntesis balanceados
def generar_parentesis_balanceados(n):
    # Si n es 0, la única cadena posible es la cadena vacía
    if n == 0:
        return ['']
    # Si n es 1, la única cadena posible es "()"
    if n == 1:
        return ['()']
    # Inicializa un conjunto para almacenar los resultados
    resultados = set()
    # Itera sobre todos los números desde 0 hasta n-1
    for i in range(n):
        # Para cada número i, genera todas las posibles cadenas de paréntesis balanceados de longitud i
        for left in generar_parentesis_balanceados(i):
            # Para cada número n-1-i, genera todas las posibles cadenas de paréntesis balanceados de longitud n-1-i
            for right in generar_parentesis_balanceados(n - 1 - i):
                # Añade la cadena "(" + left + ")" + right al conjunto de resultados
                resultados.add('(' + left + ')' + right)
    # Convierte el conjunto de resultados en una lista y la devuelve
    return list(resultados)

# Define n como 3
n = 3
# Genera todas las posibles cadenas de paréntesis balanceados de longitud n
cadenas = generar_parentesis_balanceados(n)
# Imprime cada cadena generada
for cadena in cadenas:
    print(cadena)