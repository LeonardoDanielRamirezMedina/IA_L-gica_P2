#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Otras Lógicas
# Tema: Logica modal

# Definimos la clase Mundo con dos atributos: nombre y proposiciones
class Mundo:
    def __init__(self, nombre, proposiciones):
        self.nombre = nombre
        self.proposiciones = proposiciones

# Definimos la clase Relacion con dos atributos: origen y destino
class Relacion:
    def __init__(self, origen, destino):
        self.origen = origen
        self.destino = destino

# Definimos la clase Modelo con dos atributos: mundos y relaciones
class Modelo:
    def __init__(self):
        self.mundos = []
        self.relaciones = []

# Definimos la función es_necesario que verifica si una proposición es necesariamente verdadera en un mundo dado
def es_necesario(modelo, proposicion, mundo):
    for relacion in modelo.relaciones:  # Recorremos las relaciones del modelo
        if relacion.origen == mundo:    # Si el origen de la relación es el mundo dado
            if proposicion not in relacion.destino.proposiciones:   # Si la proposición no está en el destino de la relación
                return False    # Retornamos False
    return True

# Definimos la función es_posible que verifica si una proposición es posiblemente verdadera en un mundo dado
def es_posible(modelo, proposicion, mundo): # Recorremos las relaciones del modelo
    for relacion in modelo.relaciones:  
        if relacion.origen == mundo:    
            if proposicion in relacion.destino.proposiciones:   # Si la proposición está en el destino de la relación
                return True   # Retornamos True
    return False

# Definimos la función principal que crea los mundos, las relaciones, el modelo y realiza las consultas
def main():
    # Crear mundos
    mundo1 = Mundo("M1", {"p", "q"})    # Creamos un mundo con nombre "M1" y proposiciones "p" y "q"
    mundo2 = Mundo("M2", {"p"})   # Creamos un mundo con nombre "M2" y proposición "p"
    mundo3 = Mundo("M3", {"q"})  # Creamos un mundo con nombre "M3" y proposición "q"

    # Crear relaciones
    relacion1 = Relacion(mundo1, mundo2)    # Creamos una relación del mundo1 al mundo2
    relacion2 = Relacion(mundo1, mundo3)

    # Crear modelo
    modelo = Modelo()   # Creamos un modelo
    modelo.mundos = [mundo1, mundo2, mundo3]    # Agregamos los mundos al modelo
    modelo.relaciones = [relacion1, relacion2]  # Agregamos las relaciones al modelo

    # Consultas
    proposicion = "p"
    mundo = mundo1

    print(f"¿'{proposicion}' es necesariamente verdadero en {mundo.nombre}? {es_necesario(modelo, proposicion, mundo)}")    # Realizamos la consulta
    print(f"¿'{proposicion}' es posiblemente verdadero en {mundo.nombre}? {es_posible(modelo, proposicion, mundo)}")    # Realizamos la consulta

# Ejecutamos la función principal si el script se ejecuta directamente
if __name__ == "__main__":  
    main()  # Llamamos a la función principal