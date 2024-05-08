#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Tratamiento Lógico del Lenguaje
# Tema: Gramática Causal Definida

import nltk

# Definimos una gramática que puede analizar oraciones que expresan relaciones causales
grammar = nltk.CFG.fromstring("""
    S -> NP VP
    VP -> V NP | V NP 'porque' S
    NP -> 'Yo' | 'el' | 'perro' | 'mi' | 'tarea' | NP NP
    V -> 'hice' | 'corrió'
""")

# Creamos un analizador sintáctico con la gramática
parser = nltk.ChartParser(grammar)

# Definimos una oración que expresa una relación causal
sentence = "Yo hice mi tarea porque el perro corrió".split()

# Analizamos la oración
for tree in parser.parse(sentence):
    tree.pretty_print()

print("La oración expresa una relación causal y se puede analizar sintácticamente.")
