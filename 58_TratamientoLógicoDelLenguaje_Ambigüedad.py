#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Tratamiento Lógico del Lenguaje
# Tema: Ambigüedad
#La ambigüedad es una característica de las gramáticas que permite que una oración pueda tener múltiples interpretaciones.

import nltk   #Se importa la librería Natural Language Toolkit que se utiliza para procesar texto en lenguaje natural

# Definimos una gramática que permite la ambigüedad
grammar = nltk.CFG.fromstring("""
    S -> NP VP
    PP -> P NP
    NP -> Det N | NP PP
    VP -> V NP | VP PP
    Det -> 'el'
    N -> 'hombre' | 'telescopio'
    V -> 'vio'
    P -> 'con'
""")

# Creamos un analizador sintáctico con la gramática
parser = nltk.ChartParser(grammar)  #nlkt.ChartParser se utiliza para analizar oraciones con una gramática dada

# Definimos una oración ambigua
sentence = "el hombre vio el telescopio con el hombre".split()

# Analizamos la oración
for tree in parser.parse(sentence):  #Se analiza la oración
    tree.pretty_print()  #Se imprime el árbol de análisis sintáctico

print("La oración es ambigua, ya que puede tener dos interpretaciones diferentes.") #Se imprime que la oración es ambigua, ya que puede tener dos interpretaciones diferentes.