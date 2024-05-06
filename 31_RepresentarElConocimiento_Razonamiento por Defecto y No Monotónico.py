#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Representar el Conocimiento
# Tema: Razonamiento por Defecto y No Monotónico

# el razonamiento por defecto y no monotónico son enfoques que permiten realizar inferencias lógicas y tomar decisiones basadas en reglas y hechos

# Sistema de razonamiento por defecto
class Animal:# Se define una clase Animal, con un atributo nombre y tipo
    def __init__(self, nombre):     # Se define el constructor de la clase Animal
        self.nombre = nombre    # se asigna el nombre del animal
        self.tipo = "desconocido"   # se asigna el tipo de animal como "desconocido"

class Perro(Animal):    # Se define una subclase Perro que hereda de la clase Animal
    def __init__(self, nombre): # Se define el constructor de la clase Perro
        super().__init__(nombre)    # se llama al constructor de la clase padre
        self.tipo = "perro" # se asigna el tipo de animal como "perro"

def obtener_tipo_animal(animal):    # Se define una función que recibe un objeto de la clase Animal y retorna el tipo de animal
    if isinstance(animal, Perro):   
        return "perro"  # si el objeto es de la clase Perro, se retorna "perro"
    else:
        return "desconocido"    # en caso contrario, se retorna "desconocido"

animal_desconocido = Animal("Rex")  # Se crea un objeto de la clase Animal
print("El tipo de animal es:", obtener_tipo_animal(animal_desconocido)) # Se imprime el tipo de animal

