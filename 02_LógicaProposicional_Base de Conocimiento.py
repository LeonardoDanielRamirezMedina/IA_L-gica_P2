#------------ENFOQUE: LÓGICA--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Lógica Proposicional
#Tema: Base de Conocimiento

# base de conocimientos es un repositorio de información que se puede utilizar para tomar decisiones o responder preguntas.

class BaseConocimiento: # esta clase representa una base de conocimientos
    def __init__(self): # inicializa la base de conocimientos con una lista vacía de sentencias
        self.sentencias = []    # lista de sentencias

    def agregar_sentencia(self, sentencia): # agrega una sentencia a la base de conocimientos
        self.sentencias.append(sentencia)   # agrega la sentencia a la lista de sentencias

    def verificar(self, sentencia): # verifica si una sentencia está en la base de conocimientos
        return sentencia in self.sentencias # devuelve True si la sentencia está en la lista de sentencias, False en caso contrario

# Creamos una base de conocimientos
base = BaseConocimiento()

# Agregamos algunas sentencias a la base de conocimientos
base.agregar_sentencia('El cielo es azul')
base.agregar_sentencia('La hierba es verde')

# Verificamos si una sentencia está en la base de conocimientos
print(base.verificar('El cielo es azul'))  # Devuelve True
print(base.verificar('El sol es verde'))  # Devuelve False