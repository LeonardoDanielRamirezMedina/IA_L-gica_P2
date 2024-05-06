#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Otras Lógicas
#Tema: Lógica No Monotónica

# La lógica no monótona es un tipo de lógica en la que la adición de nuevas reglas o hechos puede llevar a la eliminación de conclusiones previamente derivadas.

# Definimos la clase EstadoAnimo con dos atributos: persona y emocion
class EstadoAnimo:
    def __init__(self, persona, emocion):
        self.persona = persona  # Inicializamos el atributo persona
        self.emocion = emocion

# Definimos la clase BaseConocimiento con un atributo: hechos
class BaseConocimiento:
    def __init__(self):
        self.hechos = []    # Inicializamos la lista de hechos

    # Método para agregar un hecho a la base de conocimiento
    def agregar_hecho(self, hecho):
        self.hechos.append(hecho)   #append() Agrega un elemento al final de la lista

    # Método para obtener la emoción de una persona
    def obtener_emocion(self, persona):
        for hecho in self.hechos:
            if hecho.persona == persona:    
                return hecho.emocion    # Si el hecho corresponde a la persona, retornamos la emoción
        return None # Si no se encuentra la persona, retornamos None

# Definimos la función principal que crea la base de conocimiento y realiza las consultas
def main():
    # Crear una base de conocimiento inicial
    base_conocimiento = BaseConocimiento()  # Creamos una base de conocimiento
    base_conocimiento.agregar_hecho(EstadoAnimo("Juan", "feliz"))   # Agregamos un hecho a la base de conocimiento
    base_conocimiento.agregar_hecho(EstadoAnimo("Pedro", "triste")) # Agregamos un hecho a la base de conocimiento

    # Observaciones adicionales
    base_conocimiento.agregar_hecho(EstadoAnimo("Juan", "desempleado"))

    # Reevaluar el estado de ánimo de Juan
    emocion_juan = base_conocimiento.obtener_emocion("Juan")
    if emocion_juan == "feliz" and "desempleado" in [hecho.emocion for hecho in base_conocimiento.hechos if hecho.persona == "Juan"]:   # Si Juan está desempleado
        emocion_juan = "triste" # Juan está triste

    print("El estado de ánimo de Juan es:", emocion_juan)

# Ejecutamos la función principal si el script se ejecuta directamente
if __name__ == "__main__":
    main()  # Llamamos a la función principal