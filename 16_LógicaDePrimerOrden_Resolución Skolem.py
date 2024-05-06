#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Lógica de 1er Orden
# Tema: Resolución: Skolem


# Definimos una función de Skolem que simplemente devuelve su argumento incrementado en 1
def f(x):
    return x + 1

# Definimos una función que representa una fórmula lógica con un cuantificador existencial
def existe_x(func, n):  # La función recibe otra función y un número n
    for i in range(n):  # Iteramos sobre los valores de 0 a n-1
        if func(i): # Si la función func devuelve True para el valor i
            return True # Retornamos True
    return False   # Si la función func no devuelve True para ningún valor, retornamos False

# Definimos una función que representa la fórmula P(x) = "f(x) > x"
def P(x):   # La función recibe un número x
    return f(x) > x # Retorna True si f(x) es mayor que x, False en caso contrario

# Verificamos si existe un x tal que P(x) es verdadero
print(existe_x(P, 10))  # Imprime: True