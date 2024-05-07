#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Planificación
# Tema: Vigilancia de Ejecución y Replanificación

#la vigilancia de ejecución y la replanificación son dos técnicas que permiten a un agente reaccionar a cambios en el entorno durante la ejecución de un plan. 
#La vigilancia de ejecución implica monitorear el entorno para detectar cambios que puedan afectar la ejecución del plan, mientras que la replanificación implica generar un nuevo plan si se detecta un cambio significativo.

# La clase Estado representa el estado actual del agente, incluyendo su posición y los obstáculos.
class Estado:
    # El constructor toma una posición y una lista de obstáculos.
    def __init__(self, posicion, obstaculos):
        self.posicion = posicion
        self.obstaculos = obstaculos

    # El método obstaculo verifica si una acción llevaría al agente a un obstáculo.
    def obstaculo(self, accion):
        return self.posicion + accion in self.obstaculos

    # El método ejecutar_accion actualiza la posición del agente según la acción dada.
    def ejecutar_accion(self, accion):
        return Estado(self.posicion + accion, self.obstaculos)

# La clase Planificador se encarga de generar un plan para el agente.
class Planificador:
    # El método planificar genera un plan para moverse desde el estado inicial hasta el objetivo.
    def planificar(self, estado_inicial, objetivo):
        return [1] * (objetivo - estado_inicial.posicion)  # Moverse hacia la derecha hasta alcanzar el objetivo

# La clase Agente representa al agente que se mueve en el entorno.
class Agente:
    # El constructor toma un planificador, un estado inicial y un objetivo.
    def __init__(self, planificador, estado_inicial, objetivo):
        self.planificador = planificador
        self.estado_actual = estado_inicial
        self.objetivo = objetivo
        self.plan = self.planificador.planificar(self.estado_actual, self.objetivo)

    # El método ejecutar lleva a cabo el plan del agente.
    def ejecutar(self):
        for accion in self.plan:
            if self.estado_actual.obstaculo(accion):
                print("Obstáculo detectado en la posición {}, replanificando...".format(self.estado_actual.posicion + accion))
                nuevo_plan = self.planificador.planificar(self.estado_actual, self.objetivo)
                if nuevo_plan is not None:
                    self.plan = nuevo_plan
                    self.ejecutar()
                else:
                    print("No se puede encontrar una ruta al objetivo.")
                break
            else:
                self.estado_actual = self.estado_actual.ejecutar_accion(accion)
                if self.estado_actual.posicion == self.objetivo:
                    print("Objetivo alcanzado en la posición {}!".format(self.objetivo))
                    break

# Creación del estado inicial, el planificador y el agente.
estado_inicial = Estado(0, [3, 7])  # El agente comienza en la posición 0 y hay obstáculos en las posiciones 3 y 7
planificador = Planificador()
agente = Agente(planificador, estado_inicial, 10)  # El objetivo está en la posición 10

# Ejecución del plan del agente.
agente.ejecutar()