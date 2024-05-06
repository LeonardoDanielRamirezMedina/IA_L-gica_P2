#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Representar el Conocimiento
# Tema: Taxonomías: Categorías y Objetos

# Las taxonomías son estructuras jerárquicas que organizan conceptos en categorías y subcategorías.

# Definición de la clase Situacion
class Situacion:
    # Constructor de la clase Situacion
    def __init__(self, nombre, ubicacion, participantes):
        self.nombre = nombre  # Nombre de la situación
        self.ubicacion = ubicacion  # Ubicación de la situación
        self.participantes = participantes  # Participantes en la situación

# Definición de la clase Compra, que hereda de Situacion
class Compra(Situacion):
    # Constructor de la clase Compra
    def __init__(self, ubicacion, participantes, productos):
        super().__init__("Compra", ubicacion, participantes)  # Llamada al constructor de la clase padre
        self.productos = productos  # Productos comprados

# Definición de la clase Reunion, que hereda de Situacion
class Reunion(Situacion):
    # Constructor de la clase Reunion
    def __init__(self, ubicacion, participantes, tema):
        super().__init__("Reunión", ubicacion, participantes)  # Llamada al constructor de la clase padre
        self.tema = tema  # Tema de la reunión

# Creación de una instancia de Compra
compra1 = Compra("Supermercado", ["Juan", "María"], ["Leche", "Pan"])
# Creación de una instancia de Reunion
reunion1 = Reunion("Oficina", ["Equipo de Proyecto"], "Planificación")

# Impresión de los detalles de la compra
print("Situación:", compra1.nombre)
print("Ubicación:", compra1.ubicacion)
print("Participantes:", compra1.participantes)
print("Productos:", compra1.productos)

# Impresión de los detalles de la reunión
print("\nSituación:", reunion1.nombre)
print("Ubicación:", reunion1.ubicacion)
print("Participantes:", reunion1.participantes)
print("Tema:", reunion1.tema)