#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Planificación
# Tema: Redes Jerárquicas de Tareas

# Las redes jerárquicas de tareas son una forma de planificación que organiza las tareas en una estructura jerárquica, donde las tareas principales pueden dividirse en subtareas más pequeñas.

class Tarea:    #Se define la clase Tarea para representar una tarea con un nombre y una lista de sub-tareas.
    def __init__(self, nombre, sub_tareas=None):    #Constructor de la clase Tarea. 
        self.nombre = nombre    #Se asigna el nombre de la tarea.
        self.sub_tareas = sub_tareas if sub_tareas is not None else []  #Se asignan las sub-tareas, si no se proporcionan, se inicializa como una lista vacía.

# Definir la jerarquía de tareas para construir una casa
preparar_terreno = Tarea("Preparar Terreno")    #Se crean las tareas principales.
construir_estructura = Tarea("Construir Estructura")    
instalar_sistemas = Tarea("Instalar Sistemas", [Tarea("Instalar Electricidad"), Tarea("Instalar Plomería")])    #Se crean las sub-tareas de la tarea principal.
acabar_interiores = Tarea("Acabar Interiores")      
finalizar = Tarea("Finalizar", [acabar_interiores])   #Se crea la tarea principal con una sub-tarea.

# Visualizar la estructura jerárquica de tareas
print("Tareas para construir una casa:")    #Se imprime la estructura jerárquica de tareas.
print("- ", preparar_terreno.nombre)    #Se imprime el nombre de la tarea principal.
print("- ", construir_estructura.nombre)    #Se imprime el nombre de la tarea principal.
print("- ", instalar_sistemas.nombre)   
for sub_tarea in instalar_sistemas.sub_tareas:  #Se imprimen las sub-tareas de la tarea principal.
    print("    - ", sub_tarea.nombre)
print("- ", finalizar.nombre)
