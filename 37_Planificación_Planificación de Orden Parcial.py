#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Planificación
# Tema: Planificación de Orden Parcial

# La planificación de orden parcial es un enfoque de planificación que permite planificar acciones sin especificar un orden total entre ellas.

class Tarea:    #Se define la clase Tarea que contiene el nombre y la duración de la tarea.
    def __init__(self, nombre, duracion):
        self.nombre = nombre
        self.duracion = duracion

    def __str__(self):  #Método para imprimir la tarea de manera legible.
        return self.nombre  #Retorna el nombre de la tarea.

tarea1 = Tarea("Dormir", 8) #Se crean las tareas con sus respectivas duraciones.
tarea2 = Tarea("Trabajar", 8)
tarea3 = Tarea("Ejercicio", 1)
tarea4 = Tarea("Estudiar", 4)

tareas = [tarea1, tarea2, tarea3, tarea4]   #Se almacenan las tareas en una lista.

# Ordenar tareas por duración
tareas_ordenadas = sorted(tareas, key=lambda x: x.duracion) #Se ordenan las tareas de menor a mayor duración.

# Ejemplo de orden parcial
print("Orden de tareas (de menos a más tiempo):")   
for tarea in tareas_ordenadas:  #Se imprime el orden de las tareas.
    print(tarea)    
