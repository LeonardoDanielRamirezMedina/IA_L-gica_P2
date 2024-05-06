#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Lógica de 1er Orden
#Tema: Agentes Lógicos


class AgenteLogico:
    def __init__(self):
        # La base de conocimientos inicialmente está vacía
        self.base_de_conocimientos = []

    def percibir(self, percepciones):
        # Añadimos las percepciones a la base de conocimientos
        self.base_de_conocimientos.extend(percepciones)

    def inferir(self):
        # Inferimos nuevos hechos a partir de la base de conocimientos
        # (En este ejemplo simplificado, simplemente devolvemos la base de conocimientos tal cual)
        return self.base_de_conocimientos

    def decidir(self):
        # Tomamos una decisión basada en la base de conocimientos
        # (En este ejemplo simplificado, simplemente decidimos imprimir la base de conocimientos)
        print(self.base_de_conocimientos)

# Creamos un agente lógico
agente = AgenteLogico()

# El agente percibe algunos hechos
agente.percibir(["Es de día", "Está soleado"])

# El agente infiere nuevos hechos
agente.inferir()

# El agente toma una decisión
agente.decidir()  # Imprime: ['Es de día', 'Está soleado']