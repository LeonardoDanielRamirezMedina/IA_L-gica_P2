#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Otras Lógicas
#Tema: Lógica Difusa: Fuzzy CLIPS

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Antecedentes y consecuentes
calidad = ctrl.Antecedent(np.arange(0, 11, 1), 'calidad')   #np.arange(0, 11, 1) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
servicio = ctrl.Antecedent(np.arange(0, 11, 1), 'servicio') 
propina = ctrl.Consequent(np.arange(0, 26, 1), 'propina')

# Funciones de membresía
calidad['baja'] = fuzz.trimf(calidad.universe, [0, 0, 5])   #trimf = triangular
calidad['media'] = fuzz.trimf(calidad.universe, [0, 5, 10]) #.trimf es una función de membresía triangular
calidad['alta'] = fuzz.trimf(calidad.universe, [5, 10, 10])

servicio['bajo'] = fuzz.trimf(servicio.universe, [0, 0, 5])
servicio['medio'] = fuzz.trimf(servicio.universe, [0, 5, 10])   #trimf = triangular
servicio['alto'] = fuzz.trimf(servicio.universe, [5, 10, 10])

propina['baja'] = fuzz.trimf(propina.universe, [0, 0, 13])
propina['media'] = fuzz.trimf(propina.universe, [0, 13, 25])
propina['alta'] = fuzz.trimf(propina.universe, [13, 25, 25])    #trimf = triangular

# Reglas
regla1 = ctrl.Rule(calidad['baja'] | servicio['bajo'], propina['baja'])  #ctrl.Rule = regla
regla2 = ctrl.Rule(servicio['medio'], propina['media']) 
regla3 = ctrl.Rule(servicio['alto'] | calidad['alta'], propina['alta'])

# Sistema de control
sistema_ctrl = ctrl.ControlSystem([regla1, regla2, regla3]) #ctrl.ControlSystem = sistema de control
sistema_propina = ctrl.ControlSystemSimulation(sistema_ctrl)

# Entradas
sistema_propina.input['calidad'] = 6.5  # la calidad d  e la comida es 6.5
sistema_propina.input['servicio'] = 9.8 # el servicio es 9.8

# Computar la salida
sistema_propina.compute()   #compute = computar

print("El valor de la propina es:", sistema_propina.output['propina'])  # se obtiene el valor de la propina
propina.view(sim=sistema_propina)                               # se muestra la gráfica de la propina
