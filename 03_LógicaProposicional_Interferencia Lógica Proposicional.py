#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Lógica Proposicional
#Tema: Inferencia Lógica Proposicional


# La inferencia lógica proposicional es un proceso mediante el cual se deducen nuevas sentencias a partir de reglas y sentencias existentes en una base de conocimientos.

class BaseConocimiento: # Clase que representa una base de conocimientos
    def __init__(self): 
        self.sentencias = []    # Lista de sentencias en la base de conocimientos

    def agregar_sentencia(self, sentencia): # Método para agregar una sentencia a la base de conocimientos
        self.sentencias.append(sentencia)   # Agrega la sentencia a la lista de sentencias

    def inferir(self, regla, sentencia):    # Método para inferir una nueva sentencia a partir de una regla
        if regla in self.sentencias:    # Verifica si la regla está en la base de conocimientos
            self.agregar_sentencia(sentencia)   # Agrega la nueva sentencia a la base de conocimientos

# Creamos una base de conocimientos
base = BaseConocimiento()

# Agregamos algunas sentencias a la base de conocimientos
base.agregar_sentencia('El cielo es azul')

# Inferimos una nueva sentencia a partir de una regla existente
base.inferir('El cielo es azul', 'Hoy es un día soleado')

# Verificamos si la nueva sentencia ha sido agregada a la base de conocimientos
print('Hoy es un día soleado' in base.sentencias)  # Devuelve True