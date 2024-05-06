#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Otras Lógicas
#Tema: Lógicas de Orden Superior

# Las logicas de orden superior son aquellas que permiten que las funciones sean tratadas como objetos, es decir, que puedan ser pasadas como argumentos a otras funciones, retornadas por otras funciones, almacenadas en variables, etc.

def crear_operador(operacion):  # La función crear_operador recibe una función operacion
    def operador(x, y): # La función operador recibe dos argumentos x e y para realizar la operación
        return operacion(x, y)  # Retorna el resultado de aplicar la función operacion a los argumentos x e y
    return operador # Retorna la función operador

def suma(a, b): # función suma que recibe dos argumentos a y b
    return a + b    # Retorna la suma de a y b

def resta(a, b):    # función resta que recibe dos argumentos a y b
    return a - b    # Retorna la resta de a y b

operador_suma = crear_operador(suma)    # Creamos un operador de suma
operador_resta = crear_operador(resta)  # Creamos un operador de resta

resultado_suma = operador_suma(5, 3)    # Aplicamos el operador de suma a los argumentos 5 y 3
resultado_resta = operador_resta(5, 3)  # Aplicamos el operador de resta a los argumentos 5 y 3

print("Resultado de la suma:", resultado_suma)  # Imprimimos el resultado de la suma
print("Resultado de la resta:", resultado_resta)    # Imprimimos el resultado de la resta
