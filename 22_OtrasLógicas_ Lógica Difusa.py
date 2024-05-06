#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Otras Lógicas
# Tema: Lógica Difusa

#la logica difusa es una tecnica de computo que se basa en la logica difusa, la cual es una extension de la logica booleana que permite trabajar con valores de verdad que pueden ser cualquier valor real entre 0 y 1, en lugar de solo 0 o 1. La logica difusa es util para modelar problemas que no son facilmente modelables con la logica booleana, como por ejemplo, el control de sistemas de climatizacion, el control de sistemas de frenado de automoviles, la toma de decisiones en sistemas expertos, etc.

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definición de las variables de entrada (antecedentes) y salida (consecuente)
edad = ctrl.Antecedent(np.arange(0, 101, 1), 'edad')
ingresos = ctrl.Antecedent(np.arange(0, 100001, 1), 'ingresos')
aprobacion_credito = ctrl.Consequent(np.arange(0, 101, 1), 'aprobacion_credito')

# Definición de las funciones de membresía para cada variable
edad['joven'] = fuzz.trimf(edad.universe, [0, 0, 30])
edad['mediana'] = fuzz.trimf(edad.universe, [20, 50, 80])
edad['mayor'] = fuzz.trimf(edad.universe, [60, 100, 100])

ingresos['bajo'] = fuzz.trimf(ingresos.universe, [0, 0, 50000])
ingresos['medio'] = fuzz.trimf(ingresos.universe, [20000, 50000, 80000])
ingresos['alto'] = fuzz.trimf(ingresos.universe, [60000, 100000, 100000])

aprobacion_credito['baja'] = fuzz.trimf(aprobacion_credito.universe, [0, 0, 50])
aprobacion_credito['media'] = fuzz.trimf(aprobacion_credito.universe, [0, 50, 100])
aprobacion_credito['alta'] = fuzz.trimf(aprobacion_credito.universe, [50, 100, 100])

# Definición de las reglas del sistema de control difuso
regla1 = ctrl.Rule(edad['joven'] & ingresos['bajo'], aprobacion_credito['baja'])
regla2 = ctrl.Rule(edad['mediana'] & ingresos['medio'], aprobacion_credito['media'])
regla3 = ctrl.Rule(edad['mayor'] & ingresos['alto'], aprobacion_credito['alta'])

# Creación del sistema de control difuso
sistema_ctrl = ctrl.ControlSystem([regla1, regla2, regla3])
sistema_aprobacion_credito = ctrl.ControlSystemSimulation(sistema_ctrl)

# Definición de las entradas para el sistema de control difuso
sistema_aprobacion_credito.input['edad'] = 35
sistema_aprobacion_credito.input['ingresos'] = 70000

# Cálculo de la salida del sistema de control difuso
sistema_aprobacion_credito.compute()

# Impresión de la salida del sistema de control difuso
print("El nivel de aprobación de crédito es:", sistema_aprobacion_credito.output['aprobacion_credito'])

# Visualización de la salida del sistema de control difuso
aprobacion_credito.view(sim=sistema_aprobacion_credito)