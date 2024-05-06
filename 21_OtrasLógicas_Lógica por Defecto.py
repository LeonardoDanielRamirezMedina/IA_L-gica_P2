#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Otras Lógicas
# Tema: Lógica por Defecto

#La lógica por defecto es una extensión de la lógica clásica que permite razonar sobre proposiciones que no se conocen con certeza.

class Cafe:
    def __init__(self, tipo, disponible=True):  # Definimos la clase Cafe con dos atributos: tipo y disponible. disponible se inicializa en True por defecto
        self.tipo = tipo    # Inicializamos el atributo tipo
        self.disponible = disponible    # Inicializamos el atributo disponible

class Cafeteria:    # Definimos la clase Cafeteria con un atributo: menu. esta clase se utiliza para servir diferentes tipos de café
    def __init__(self): 
        self.menu = {   # Inicializamos el menú con diferentes tipos de café
            "espresso": Cafe("espresso"),   # Creamos un menú con diferentes tipos de café
            "latte": Cafe("latte"),     
            "cappuccino": Cafe("cappuccino")
        }

    def servir_cafe(self, tipo):    # Definimos la función servir_cafe que recibe un tipo de café y retorna el café correspondiente
        return self.menu.get(tipo, Cafe("cafe regular"))    # Retornamos el café correspondiente al tipo, si no se encuentra, retornamos un café regular

def main(): # Definimos la función principal
    cafeteria = Cafeteria()     # Creamos una cafetería

    # Simulación de pedido de café
    tipo_pedido = "mocha"   # Definimos el tipo de café que pide el cliente
    cafe_pedido = cafeteria.servir_cafe(tipo_pedido)    # Servimos el café correspondiente al tipo de pedido

    print(f"Cliente pidió un {tipo_pedido}, le servimos un {cafe_pedido.tipo}")   # Mostramos el café que se le sirvió al cliente

if __name__ == "__main__":  # Verificamos si el script se ejecuta directamente
    main()  # Llamamos a la función principal
