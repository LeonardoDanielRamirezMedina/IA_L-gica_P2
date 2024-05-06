#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Representar el Conocimiento
# Tema: Eventos y Objetos Mentales: Creencias

# Los eventos y objetos mentales son elementos que forman parte de la representación del conocimiento en sistemas inteligentes.

# Definición de la clase Emocion
class Emocion:
    # Constructor de la clase Emocion
    def __init__(self, nombre, intensidad):
        self.nombre = nombre  # Nombre de la emoción
        self.intensidad = intensidad  # Intensidad de la emoción

# Definición de la clase Persona
class Persona:
    # Constructor de la clase Persona
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre de la persona
        self.emociones = []  # Lista de emociones de la persona

    # Método para agregar una emoción a la lista de emociones de la persona
    def agregar_emocion(self, emocion):
        self.emociones.append(emocion)

# Creación de una instancia de Persona
persona1 = Persona("María")
# Creación de instancias de Emocion
emocion1 = Emocion("Felicidad", 0.8)
emocion2 = Emocion("Tristeza", 0.6)

# Agregar las emociones a la persona
persona1.agregar_emocion(emocion1)
persona1.agregar_emocion(emocion2)

# Impresión de las emociones de la persona
print("Emociones de", persona1.nombre + ":")
for i, emocion in enumerate(persona1.emociones, 1):
    print(f"{i}. {emocion.nombre} - Intensidad: {emocion.intensidad}")