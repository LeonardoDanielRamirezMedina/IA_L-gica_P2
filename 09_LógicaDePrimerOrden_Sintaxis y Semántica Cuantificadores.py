#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Lógica de 1er Orden
#Tema: Sintaxis y Semántica: Cuantificadores

# Los cuantificadores son operadores lógicos que expresan la cantidad de elementos en un conjunto que satisfacen una propiedad.

from sympy import symbols, Implies, And, Or, Not
from sympy.logic.inference import satisfiable

# Definimos algunas variables proposicionales
P, Q, R = symbols('P Q R')

# Creamos una fórmula que dice "si P entonces Q"
formula = Implies(P, Q)

# Creamos una interpretación donde P es verdadero y Q es falso
interpretacion = {P: True, Q: False}

# Verificamos si la fórmula es satisfacible con esta interpretación
print(satisfiable(And(formula, Not(Q))))

# Creamos una fórmula que dice "P o no P"
formula = Or(P, Not(P))

# Verificamos si la fórmula es satisfacible
print(satisfiable(formula))

#creas una fórmula que dice "Para todo P, si P entonces Q". Luego, verificas si esta fórmula es satisfacible con una interpretación donde P es verdadero y Q es falso.
# Después, creas una fórmula que dice "Para todo P, P o no P" y verificas si esta fórmula es una tautología (siempre verdadera).