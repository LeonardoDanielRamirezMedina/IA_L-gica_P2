#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Representar el Conocimiento
# Tema: Modelo Probabilista Racional

# el modelo probabilista racional es un enfoque que se basa en la probabilidad para realizar predicciones

# Sistema de predicción de precios de acciones basado en modelo probabilista

import random

def predecir_precio_acción(día_actual): # función que predice el precio de una acción en un día específico
    precio_actual = 100 # precio inicial de la acción
    if día_actual < 10: # si el día actual es menor a 10
        return precio_actual + random.uniform(-5, 5)    # se le suma un valor aleatorio entre -5 y 5 al precio actual
    elif día_actual < 20:   # si el día actual es menor a 20
        return precio_actual + random.uniform(-10, 10)  # se le suma un valor aleatorio entre -10 y 10 al precio actual
    else:   
        return precio_actual + random.uniform(-15, 15)  # se le suma un valor aleatorio entre -15 y 15 al precio actual

for día in range(30):   # se simulan 30 días
    print(f"Día {día+1}: Precio predicho = {predecir_precio_acción(día)}")  # se imprime el día y el precio predicho de la acción
