#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Lógica Proposicional
# Tema: Encadenamiento: Hacia Delante y Atrás


# El encadenamiento hacia adelante y hacia atrás son dos estrategias de inferencia utilizadas en sistemas expertos
# y lógica de primer orden para deducir nuevas conclusiones a partir de reglas y hechos en una base de conocimientos.

# La clase Regla representa una regla lógica con antecedentes y un consecuente.
class Regla:
    def __init__(self, antecedentes, consecuente):
        # Los antecedentes son un conjunto de proposiciones que, si todas son verdaderas, implican el consecuente.
        self.antecedentes = antecedentes
        # El consecuente es una proposición que es implicada por los antecedentes.
        self.consecuente = consecuente

# La clase SistemaBasadoEnReglas representa un sistema basado en reglas que puede realizar encadenamiento hacia delante y hacia atrás.
class SistemaBasadoEnReglas:
    def __init__(self, reglas):
        # Las reglas son una lista de objetos de la clase Regla que definen la lógica del sistema.
        self.reglas = reglas

    # El método encadenamiento_hacia_delante realiza encadenamiento hacia delante.
    def encadenamiento_hacia_delante(self, datos):
        # Se repite el proceso hasta que no se pueda agregar más información a los datos.
        while True:
            # Se asume que no se agregará nueva información a los datos.
            nueva_informacion = False
            # Se itera sobre cada regla en el sistema.
            for regla in self.reglas:
                # Si los antecedentes de la regla son un subconjunto de los datos y el consecuente de la regla no está en los datos,
                if regla.antecedentes.issubset(datos) and regla.consecuente not in datos:
                    # entonces se agrega el consecuente de la regla a los datos y se marca que se agregó nueva información.
                    datos.add(regla.consecuente)
                    nueva_informacion = True
            # Si no se agregó nueva información, se termina el proceso.
            if not nueva_informacion:
                break
        # Se devuelven los datos después de realizar el encadenamiento hacia delante.
        return datos

    # El método encadenamiento_hacia_atras realiza encadenamiento hacia atrás.
    def encadenamiento_hacia_atras(self, meta):
        # Se itera sobre cada regla en el sistema.
        for regla in self.reglas:
            # Si el consecuente de la regla es la meta,
            if regla.consecuente == meta:
                # y si todos los antecedentes de la regla pueden ser inferidos mediante encadenamiento hacia atrás,
                if all(self.encadenamiento_hacia_atras(antecedente) for antecedente in regla.antecedentes):
                    # entonces se devuelve True para indicar que la meta puede ser inferida.
                    return True
        # Si ninguna regla permite inferir la meta, se devuelve False.
        return False

# Se definen algunas reglas.
reglas = [Regla({'A'}, 'B'), Regla({'B'}, 'C'), Regla({'C'}, 'D')]

# Se crea un sistema basado en reglas con las reglas definidas.
sistema = SistemaBasadoEnReglas(reglas)

# Se realizan encadenamiento hacia delante con los datos iniciales {'A'}.
print(sistema.encadenamiento_hacia_delante({'A'}))  # Devuelve {'A', 'B', 'C', 'D'}

# Se realiza encadenamiento hacia atrás con la meta 'D'.
print(sistema.encadenamiento_hacia_atras('D'))  # Devuelve True