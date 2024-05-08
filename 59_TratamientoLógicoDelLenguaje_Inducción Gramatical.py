#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Tratamiento Lógico del Lenguaje
# Tema: Inducción Gramatical
#La inducción gramatical es un proceso mediante el cual se infiere una gramática a partir de un conjunto de ejemplos de cadenas válidas en un lenguaje.

from nltk import CFG    #Se utiliza para definir gramáticas
from nltk.parse.generate import generate    #Se utiliza para generar cadenas a partir de una gramática

# Definimos un conjunto de cadenas de entrada
input_strings = ["el gato come", "el perro come", "el gato duerme", "el perro duerme"]

# Inicializamos una gramática con algunas reglas básicas
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> 'el' N
    N -> 'gato' | 'perro'
    VP -> V
    V -> 'come' | 'duerme'
""")

# Generamos todas las cadenas que puede producir la gramática
generated_strings = [' '.join(sentence) for sentence in generate(grammar)]

# Comprobamos si todas las cadenas de entrada están en las cadenas generadas
if all(input_string in generated_strings for input_string in input_strings):    #Se verifica si todas las cadenas de entrada están en las cadenas generadas
    print("La gramática puede generar todas las cadenas de entrada.")   #Se imprime si la gramática puede generar todas las cadenas de entrada
else:
    print("La gramática no puede generar todas las cadenas de entrada.")    #Se imprime si la gramática no puede generar todas las cadenas de entrada