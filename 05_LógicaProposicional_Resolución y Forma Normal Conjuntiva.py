#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Lógica Proposicional
# Tema: Resolución y Forma Normal Conjuntiva

# La resolución es un método de inferencia lógica que se utiliza para demostrar la validez de una fórmula proposicional. La forma normal conjuntiva (FNC) 
# es una forma normal en la que una fórmula proposicional se expresa como una conjunción de cláusulas, donde cada cláusula es una disyunción de literales.


from sympy import symbols
from sympy.logic.boolalg import Or, And, Not
from sympy.logic.inference import satisfiable

# Definimos algunas variables proposicionales
P, Q, R = symbols('P Q R')

# Creamos una fórmula en FNC
# (P AND Q) OR (NOT Q AND R)
formula = Or(And(P, Q), And(Not(Q), R))

# Creamos una cláusula para resolver contra la fórmula
# NOT P
clausula = Not(P)

# Aplicamos la resolución
# Si la fórmula y la negación de la cláusula son insatisfacibles juntas, entonces la cláusula se puede inferir de la fórmula
resultado = not satisfiable(And(formula, Not(clausula)))

print("La cláusula se puede inferir de la fórmula:", resultado) # La cláusula se puede inferir de la fórmula: True