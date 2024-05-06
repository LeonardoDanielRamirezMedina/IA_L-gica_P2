#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Lógica de 1er Orden
# Tema: Reglas de Diagnóstico y Causales

# Las reglas de diagnóstico y causales son reglas lógicas que se utilizan en sistemas expertos y lógica de primer orden para inferir relaciones de causa y efecto entre eventos y condiciones.

class MotorFalla:   # la clase MotorFalla representa el estado de un motor y sus posibles fallas
    def __init__(self, enciende, funciona, hace_ruido):   # Método constructor de la clase MotorFalla
        self.enciende = enciende    # Atributos del motor
        self.funciona = funciona    # Atributos del motor
        self.hace_ruido = hace_ruido    # Atributos del motor

def diagnostico_motor(motor):   # Función que realiza un diagnóstico del motor basado en su estado
    if not motor.enciende:  # Si el motor no enciende
        print("La batería podría estar descargada o los cables de la batería podrían estar sueltos o corroídos.")   # Imprime un mensaje de diagnóstico
    elif motor.enciende and not motor.funciona:  # Si el motor enciende pero no funciona
        print("El combustible podría estar vacío o el filtro de combustible podría estar obstruido.")  # Imprime un mensaje de diagnóstico
    elif motor.hace_ruido:  # Si el motor hace ruido
        print("Podría haber un problema con el sistema de encendido.")  # Imprime un mensaje de diagnóstico

# Creamos un objeto MotorFalla con el estado del motor
motor = MotorFalla(enciende=False, funciona=False, hace_ruido=True) 

# Ejecutamos el diagnóstico del motor
diagnostico_motor(motor)