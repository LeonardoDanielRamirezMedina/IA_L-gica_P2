#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Tratamiento Lógico del Lenguaje
# Tema: Análisis Léxico

#El analisis léxico es el proceso de convertir una secuencia de caracteres en una secuencia de tokens. En este ejemplo, se implementa una función de análisis léxico que divide una expresión matemática en números y operadores.

import re   # Importa el módulo re para utilizar expresiones regulares

def analisis_lexico(expresion):
    tokens = re.findall(r'\d+|\+|\-|\*|\/|\(|\)', expresion)    # Encuentra todos los números y los operadores en la expresión
    return tokens                                        # Devuelve la lista de tokens

expresion = "3 + 5 * (2 - 4)"   # Define la expresión a analizar
tokens = analisis_lexico(expresion)  # Realiza el análisis léxico de la expresión
print(tokens)   # Imprime la lista de tokens      
