#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Planificación
# Tema: Planificación Condicional

#La planificación condicional es un enfoque en el que se toman decisiones basadas en ciertas condiciones o criterios.

class SistemaNavegacionAutonoma:    #Se crea la clase SistemaNavegacionAutonoma que se utilizará para la planificación de rutas en un vehículo autónomo.   
    def __init__(self):
        self.ubicacion_actual = None    #Se inicializa la ubicación actual del vehículo como None.

    def actualizar_ubicacion(self, nueva_ubicacion):    #Se define el método actualizar_ubicacion que permite actualizar la ubicación actual del vehículo.
        self.ubicacion_actual = nueva_ubicacion   #Se actualiza la ubicación actual del vehículo con la nueva ubicación.

    def planificar_ruta(self, destino):   #Se define el método planificar_ruta que toma un destino como argumento y devuelve la ruta óptima al destino.
        if self.ubicacion_actual is None:   #Se verifica si la ubicación actual está establecida.
            raise ValueError("La ubicación actual no está establecida.")        #Si la ubicación actual no está establecida, se lanza un ValueError.
        ruta_optima = obtener_ruta_optima(self.ubicacion_actual, destino)   #Se llama a la función obtener_ruta_optima para obtener la ruta óptima al destino.
        return ruta_optima

def obtener_ruta_optima(origen, destino):
    # Lógica para encontrar la ruta óptima, por ejemplo, utilizando algoritmos de búsqueda de caminos como A* o Dijkstra
    pass

sistema_navegacion = SistemaNavegacionAutonoma()    #Se crea una instancia de la clase SistemaNavegacionAutonoma.
sistema_navegacion.actualizar_ubicacion((10, 20))  # Actualizar la ubicación actual del vehículo
ruta_optima = sistema_navegacion.planificar_ruta((30, 40))  # Planificar la ruta al destino
print("Ruta óptima:", ruta_optima)  #Imprimw la ruta óptima calculada por el sistema de navegación autónoma.
