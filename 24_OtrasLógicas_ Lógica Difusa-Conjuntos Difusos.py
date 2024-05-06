#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Otras Lógicas
#Tema: Lógica Difusa: Conjuntos Difusos

#En la lógica difusa, los conjuntos difusos son una extensión de los conjuntos clásicos, en los que los elementos pueden pertenecer a un conjunto con un grado de pertenencia que va de 0 a 1.

import numpy as np
import matplotlib.pyplot as plt #se importa la librería matplotlib para graficar

# Definimos el universo de discurso
x = np.arange(0, 11, 1)

# Función de membresía triangular
def trimf(x, params):   #se define la función trimf con dos parámetros, x y params.
    a, b, c = params    #se definen los parámetros de la función de membresía triangular.
    y = np.zeros_like(x)    #se crea un arreglo de ceros con las mismas dimensiones que x
    y[(a <= x) & (x <= b)] = (x[(a <= x) & (x <= b)] - a) / (b - a) #se define la función de membresía triangular.
    y[(b < x) & (x <= c)] = (c - x[(b < x) & (x <= c)]) / (c - b)   #se define la función de membresía triangular.
    return y

# Definimos las funciones de membresía triangular
membresia_baja = trimf(x, [0, 0, 5])    #se define la función de membresía baja.
membresia_media = trimf(x, [0, 5, 10])  #trimf es una función que se utiliza para definir una función de membresía triangular.
membresia_alta = trimf(x, [5, 10, 10])  #5, 10, 10 son los parámetros de la función de membresía triangular.

# Visualizamos las funciones de membresía
plt.figure()    #se crea una figura
plt.plot(x, membresia_baja, 'b', linewidth=1.5, label='Baja')   #se grafica la función de membresía baja
plt.plot(x, membresia_media, 'g', linewidth=1.5, label='Media') #se grafica la función de membresía media
plt.plot(x, membresia_alta, 'r', linewidth=1.5, label='Alta')   #se grafica la función de membresía alta
plt.title('Funciones de membresía')   #se coloca un título a la gráfica
plt.legend()    #se coloca la leyenda
plt.show()  #se muestra la gráfica