#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Tratamiento Lógico del Lenguaje
# Tema: Análisis Sintáctico

#El analisis sintáctico es el proceso de analizar una secuencia de tokens para determinar su estructura gramatical con respecto a una gramática formal dada.

import nltk #Se importa la librería Natural Language Toolkit que se utiliza para procesar texto en lenguaje natural

# Definimos una gramática para analizar las instrucciones de una receta
grammar = nltk.CFG.fromstring("""
    S -> VP
    VP -> V NP | V NP PP
    PP -> P NP
    V -> "corta" | "mezcla" | "cocina"
    NP -> "tomate" | "cebolla" | "pimiento" | Det N | Det N PP
    Det -> "un" | "una" | "dos" | "las" | "los"
    N -> "tomates" | "cebollas" | "pimientos"
    P -> "en" | "con"
""")

# Creamos un analizador sintáctico con la gramática
parser = nltk.ChartParser(grammar)  #nlkt.ChartParser se utiliza para analizar oraciones con una gramática dada

# Definimos una instrucción de la receta    
sentence = "corta un tomate".split()    #Se define una instrucción de la receta

# Analizamos la instrucción
for tree in parser.parse(sentence): #Se analiza la instrucción
    tree.pretty_print() #Se imprime el árbol de análisis sintáctico

print("La instrucción es válida y se puede analizar sintácticamente.")