#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Lógica Proposicional
# Tema: Equivalencia, Validez y Satisfacibilidad

# La equivalencia, validez y satisfacibilidad son conceptos importantes en lógica proposicional que nos permiten evaluar la relación entre sentencias y fórmulas lógicas.

# Equivalencia: Dos fórmulas son equivalentes si tienen el mismo valor de verdad para todas las asignaciones de verdad posibles.
# Validez: Una fórmula es válida si es verdadera para todas las asignaciones de verdad posibles.
# Satisfacibilidad: Una fórmula es satisfacible si es verdadera para al menos una asignación de verdad.

from sympy import symbols   #se utiliza para definir variables simbólicas
from sympy.logic.boolalg import Or, And, Not, Implies, Equivalent   #se utilizan para definir operaciones lógicas
from sympy.logic.inference import satisfiable, valid    #se utiliza para verificar la satisfacibilidad y validez de una fórmula

# Definimos algunas variables proposicionales
P, Q = symbols('P Q')

# Verificamos la equivalencia de dos fórmulas   
formula1 = And(P, Q)        #and se utiliza para la conjunción lógica
formula2 = Not(Or(Not(P), Not(Q))) #and se utiliza para la conjunción lógica, not se utiliza para la negación lógica
print("Las fórmulas son equivalentes:", Equivalent(formula1, formula2)) #Equivalent se utiliza para verificar si dos fórmulas son equivalentes

# Verificamos la validez de una fórmula
formula = Implies(P, P) #implies se utiliza para la implicación lógica
print("La fórmula es válida:", valid(formula))  #valid se utiliza para verificar si una fórmula es válida

# Verificamos la satisfacibilidad de una fórmula
formula = Or(P, Not(P)) #or se utiliza para la disyunción lógica
print("La fórmula es satisfacible:", satisfiable(formula))  #satisfiable se utiliza para verificar si una fórmula es satisfacible
