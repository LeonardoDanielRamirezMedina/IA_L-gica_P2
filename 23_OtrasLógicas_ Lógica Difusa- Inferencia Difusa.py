#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Otras Lógicas
# Tema: Lógica Difusa: Inferencia Difusa

# En la lógica difusa, la inferencia difusa es el proceso de combinar las reglas difusas con las entradas difusas para obtener una salida difusa.

import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Definir entradas y salidas difusas
calidad = np.arange(0, 11, 1)   #se define el rango de la variable calidad
servicio = np.arange(0, 11, 1)  #se define el rango de la variable servicio
propina = np.arange(0, 26, 1)   #se define el rango de la variable propina

# Definir funciones de membresía
calidad_baja = fuzz.trimf(calidad, [0, 0, 5])   #se define la función de membresía baja para la variable calidad
calidad_media = fuzz.trimf(calidad, [0, 5, 10]) #se define la función de membresía media para la variable calidad
calidad_alta = fuzz.trimf(calidad, [5, 10, 10]) #se define la función de membresía alta para la variable calidad

servicio_bajo = fuzz.trimf(servicio, [0, 0, 5])  #se define la función de membresía baja para la variable servicio
servicio_medio = fuzz.trimf(servicio, [0, 5, 10])   #se define la función de membresía media para la variable servicio
servicio_alto = fuzz.trimf(servicio, [5, 10, 10])   #se define la función de membresía alta para la variable servicio

# Definir reglas difusas
regla1 = fuzz.relation_min(calidad_baja, servicio_bajo)  #se define la regla 1
regla2 = fuzz.relation_min(calidad_media, servicio_medio)   #se define la regla 2
regla3 = fuzz.relation_min(calidad_alta, servicio_alto) #se define la regla 3

# Inferencia difusa
activacion_regla1 = np.fmax(regla1, np.fmax(regla2, regla3))    #se realiza la inferencia difusa
propina_activada = fuzz.defuzz(propina, activacion_regla1, 'centroid')  #se desdifusa la inferencia difusa

# Visualizar el resultado
plt.figure()    #se crea una figura
plt.plot(propina, activacion_regla1, 'b', linewidth=0.5, linestyle='--')    #se grafica la activación de las reglas difusas
plt.title('Activación de reglas difusas')   #se coloca un título a la gráfica
plt.show()  #se muestra la gráfica
