#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Planificación
# Tema: Planificación Continua y Multiagente

# La planificación continua y multiagente es un enfoque de la planificación en el que los agentes pueden ejecutar sus planes de forma continua y en paralelo.

class Agente:
    def __init__(self, nombre, planificador, estado_inicial, objetivo):
        self.nombre = nombre  # Nombre del agente
        self.planificador = planificador  # Planificador que se utilizará para generar el plan
        self.estado_actual = estado_inicial  # Estado inicial del agente
        self.objetivo = objetivo  # Objetivo que el agente intenta alcanzar
        self.plan = self.planificador.planificar(self.estado_actual, self.objetivo)  # Plan inicial

    def ejecutar(self):
        for accion in self.plan:  # Para cada acción en el plan
            if self.estado_actual.obstaculo(accion):  # Si hay un obstáculo
                print(f"Agente {self.nombre}: Obstáculo detectado, replanificando...")
                self.plan = self.planificador.planificar(self.estado_actual, self.objetivo)  # Replanificar
                self.ejecutar()  # Ejecutar el nuevo plan
                break
            else:  # Si no hay un obstáculo
                self.estado_actual = self.estado_actual.ejecutar_accion(accion)  # Ejecutar la acción
                if self.estado_actual == self.objetivo:  # Si el estado actual es el objetivo
                    print(f"Agente {self.nombre}: Objetivo alcanzado!")  # El objetivo ha sido alcanzado
                    break

class Estado:
    def __init__(self, posicion, obstaculos):
        self.posicion = posicion  # Posición actual
        self.obstaculos = obstaculos  # Lista de posiciones de los obstáculos

    def obstaculo(self, accion):
        return (self.posicion + accion) in self.obstaculos  # Verificar si la acción lleva a un obstáculo

    def ejecutar_accion(self, accion):
        if not self.obstaculo(accion):  # Si la acción no lleva a un obstáculo
            self.posicion += accion  # Actualizar la posición
        return self

class Planificador:
    def planificar(self, estado_inicial, objetivo):
        plan = []  # Inicializar el plan
        while estado_inicial.posicion != objetivo:  # Mientras no se haya alcanzado el objetivo
            if estado_inicial.posicion < objetivo:  # Si el objetivo está a la derecha
                plan.append(1)  # Moverse a la derecha
            else:  # Si el objetivo está a la izquierda
                plan.append(-1)  # Moverse a la izquierda
            estado_inicial = estado_inicial.ejecutar_accion(plan[-1])  # Actualizar el estado inicial
        return plan  # Devolver el plan

# Crear los estados iniciales y los agentes
estado_inicial1 = Estado(0, [3, 7])  # El agente 1 comienza en la posición 0 y hay obstáculos en las posiciones 3 y 7
estado_inicial2 = Estado(10, [3, 7])  # El agente 2 comienza en la posición 10 y hay obstáculos en las posiciones 3 y 7
planificador = Planificador()  # Crear el planificador
agente1 = Agente("1", planificador, estado_inicial1, 10)  # El objetivo del agente 1 está en la posición 10
agente2 = Agente("2", planificador, estado_inicial2, 0)  # El objetivo del agente 2 está en la posición 0

# Los agentes ejecutan sus planes de forma continua
while True:
    agente1.ejecutar()
    agente2.ejecutar()

    # Si ambos agentes han alcanzado sus objetivos, terminamos el bucle
    if agente1.estado_actual == agente1.objetivo and agente2.estado_actual == agente2.objetivo:
        break