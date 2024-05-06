#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Otras Lógicas
#Tema: Lógica Temporal

#La logica temporal es una extension de la logica modal que permite razonar sobre proposiciones que cambian en el tiempo.

class IntervaloTiempo:  # Definimos la clase IntervaloTiempo con dos atributos: inicio y fin. se utiliza para representar un intervalo de tiempo
    def __init__(self, inicio, fin):
        self.inicio = inicio    # Inicializamos el atributo inicio
        self.fin = fin  # Inicializamos el atributo fin

class MundoTemporal:    # Definimos la clase MundoTemporal con tres atributos: nombre, proposiciones e intervalo. 
    def __init__(self, nombre, proposiciones, intervalo):
        self.nombre = nombre    # Inicializamos el atributo nombre
        self.proposiciones = proposiciones  # Inicializamos el atributo proposiciones
        self.intervalo = intervalo  # Inicializamos el atributo intervalo

class ModeloTemporal:   # Definimos la clase ModeloTemporal con un atributo: mundos.
    def __init__(self): 
        self.mundos = []    # Inicializamos la lista de mundos

def es_verdadera_en_tiempo(modelo, proposicion, tiempo):    # Definimos la función es_verdadera_en_tiempo que verifica si una proposición es verdadera en un tiempo dado
    for mundo in modelo.mundos: # Recorremos los mundos del modelo
        if mundo.intervalo.inicio <= tiempo <= mundo.intervalo.fin:   # Si el tiempo está dentro del intervalo del mundo
            if proposicion in mundo.proposiciones:  # Si la proposición está en las proposiciones del mundo
                return True # Retornamos True
    return False    # Retornamos False

def main():
    # Crear intervalos de tiempo
    intervalo1 = IntervaloTiempo(0, 5)  # Creamos un intervalo de tiempo de 0 a 5
    intervalo2 = IntervaloTiempo(6, 10)     # Creamos un intervalo de tiempo de 6 a 10

    # Crear mundos temporales
    mundo1 = MundoTemporal("M1", {"p", "q"}, intervalo1)    # Creamos un mundo con nombre "M1", proposiciones "p" y "q" y intervalo de tiempo 0 a 5   
    mundo2 = MundoTemporal("M2", {"p"}, intervalo2)    # Creamos un mundo con nombre "M2", proposición "p" e intervalo de tiempo 6 a 10

    # Crear modelo temporal
    modelo = ModeloTemporal()   
    modelo.mundos = [mundo1, mundo2]    # Agregamos los mundos al modelo

    # Consultas
    tiempo = 3  # Definimos el tiempo
    proposicion = "p"   # Definimos la proposición

    print(f"¿'{proposicion}' es verdadero en el tiempo {tiempo}? {es_verdadera_en_tiempo(modelo, proposicion, tiempo)}")    # Realizamos la consulta

if __name__ == "__main__":  # Verificamos si el script se ejecuta directamente
    main()  # Llamamos a la función principal
