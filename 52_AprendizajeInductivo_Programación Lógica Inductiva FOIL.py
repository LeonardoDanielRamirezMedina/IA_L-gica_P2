#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Aprendizaje Inductivo
# Tema: Programación Lógica Inductiva: FOIL

#La programación lógica inductiva es un enfoque de aprendizaje inductivo que utiliza la lógica de primer orden para inducir reglas a partir de datos de entrenamiento. En este ejemplo, utilizaremos el algoritmo FOIL (Primero en la Lista de Inducción de Cláusulas) para inducir reglas que clasifiquen a los clientes como buenos o malos en función de su historial crediticio, nivel de ingresos y estado civil.

# Importa las funciones necesarias de la biblioteca sympy para la manipulación simbólica
from sympy import symbols, Or, And, Not
# Importa la función para dividir los datos en conjuntos de entrenamiento y prueba
from sklearn.model_selection import train_test_split

# Define tres variables simbólicas: historial_crediticio, nivel_ingresos y estado_civil
historial_crediticio = symbols('historial_crediticio')
nivel_ingresos = symbols('nivel_ingresos')
estado_civil = symbols('estado_civil')

# Define los datos de entrenamiento. Cada cliente se representa como un diccionario con los valores de las tres variables
datos = [
    {historial_crediticio: 1, nivel_ingresos: 1000, estado_civil: 'soltero'},  # Buen cliente
    {historial_crediticio: 0, nivel_ingresos: 2000, estado_civil: 'casado'},   # Mal cliente
    {historial_crediticio: 1, nivel_ingresos: 1500, estado_civil: 'soltero'},  # Buen cliente
    {historial_crediticio: 0, nivel_ingresos: 3000, estado_civil: 'divorciado'},# Mal cliente
    {historial_crediticio: 1, nivel_ingresos: 1200, estado_civil: 'soltero'},  # Buen cliente
    {historial_crediticio: 0, nivel_ingresos: 2500, estado_civil: 'casado'}     # Mal cliente
]

# Divide los datos en conjuntos de entrenamiento y prueba utilizando la función train_test_split
datos_entrenamiento, datos_prueba = train_test_split(datos, test_size=0.2, random_state=42)

# Define la función foil, que implementa el algoritmo FOIL. Esta función genera una regla lógica que clasifica a los clientes en buenos y malos
def foil(datos_entrenamiento, target_variable):
    regla = Or()
    positivos = [dato for dato in datos_entrenamiento if dato[target_variable] == 1]
    negativos = [dato for dato in datos_entrenamiento if dato[target_variable] == 0]
    for atributo, valor in positivos[0].items():
        if atributo != target_variable:
            condiciones = Or()
            for dato in positivos:
                if dato[atributo] == valor:
                    condiciones = And(condiciones, atributo)
                else:
                    condiciones = And(condiciones, Not(atributo))
            regla = Or(regla, condiciones)
    for atributo, valor in negativos[0].items():
        if atributo != target_variable:
            condiciones = Or()
            for dato in negativos:
                if dato[atributo] == valor:
                    condiciones = And(condiciones, Not(atributo))
                else:
                    condiciones = And(condiciones, atributo)
            regla = Or(regla, condiciones)
    return regla

# Induce una regla utilizando la función foil y los datos de entrenamiento
regla = foil(datos_entrenamiento, historial_crediticio)

# Imprime la regla inducida
print("Regla inducida:", regla)

# Evalúa la regla en el conjunto de prueba. Para cada cliente en el conjunto de prueba, se sustituyen sus valores en la regla y se imprime la clasificación resultante
for dato in datos_prueba:
    if regla.subs(dato):
        print("Cliente:", dato, "Clasificación: Buen cliente")
    else:
        print("Cliente:", dato, "Clasificación: Mal cliente")