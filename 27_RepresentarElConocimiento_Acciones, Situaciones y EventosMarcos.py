#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Representar el Conocimiento
# Tema: Acciones, Situaciones y Eventos: Marcos

# Los marcos son estructuras que representan situaciones, eventos o acciones, y contienen información sobre los elementos que los componen.

# Definición de la clase Persona
class Persona:
    # Constructor de la clase Persona
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre de la persona
        self.creencias = []  # Lista de creencias de la persona

    # Método para agregar una creencia a la lista de creencias de la persona
    def agregar_creencia(self, creencia):
        self.creencias.append(creencia)

# Definición de la clase Creencia
class Creencia:
    # Constructor de la clase Creencia
    def __init__(self, contenido):
        self.contenido = contenido  # Contenido de la creencia

# Creación de una instancia de Persona
persona1 = Persona("Juan")
# Creación de instancias de Creencia
creencia1 = Creencia("El trabajo duro lleva al éxito")
creencia2 = Creencia("La honestidad es importante")

# Agregar las creencias a la persona
persona1.agregar_creencia(creencia1)
persona1.agregar_creencia(creencia2)

# Impresión de las creencias de la persona
print("Creencias de", persona1.nombre + ":")
for i, creencia in enumerate(persona1.creencias, 1):
    print(f"{i}. {creencia.contenido}")