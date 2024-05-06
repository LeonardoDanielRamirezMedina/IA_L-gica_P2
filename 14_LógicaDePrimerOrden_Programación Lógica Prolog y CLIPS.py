#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Lógica de 1er Orden
# Tema: Programación Lógica: Prolog y CLIPS

# prolog y clips son lenguajes de programación lógica que se utilizan para definir reglas y relaciones lógicas entre diferentes entidades.

from pyswip import Prolog

# Creamos una instancia de la clase Prolog
prolog = Prolog()
# hechos a la base de conocimientos de Prolog
# hechos representan las relaciones de parentesco entre diferentes personas
prolog.assertz("padre(juan, maria)")  # Juan es padre de Maria
prolog.assertz("padre(juan, pedro)")  # Juan es padre de Pedro
prolog.assertz("madre(ana, maria)")  # Ana es madre de Maria
prolog.assertz("madre(ana, pedro)")  # Ana es madre de Pedro

# Añadimos una regla a la base de conocimientos de Prolog
# Esta regla define la relación de hermandad: dos personas son hermanas si comparten el mismo padre y no son la misma persona
prolog.assertz("hermano(X, Y) :- padre(Z, X), padre(Z, Y), X \= Y")

# Realizamos una consulta a la base de conocimientos de Prolog
# Esta consulta busca todos los pares de hermanos según la regla que hemos definido
# La función list convierte el resultado (que es un generador) en una lista para que podamos ver todos los resultados a la vez
list(prolog.query("hermano(X, Y)"))

resultados = list(prolog.query("hermano(X, Y)"))
if len(resultados) > 0:
    print(resultados[0])  # Imprime el primer resultado
else:
    print("No se encontraron resultados")