#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Representar el Conocimiento
# Tema: Ingeniería del Conocimiento: Ontologías

#La ontología es una representación formal y explícita de los conceptos, propiedades y relaciones entre los conceptos de un dominio específico.

# Definición de la clase Proyecto
class Proyecto:
    # Constructor de la clase Proyecto
    def __init__(self, nombre, descripcion, fecha_inicio, fecha_fin, responsables):
        self.nombre = nombre  # Nombre del proyecto
        self.descripcion = descripcion  # Descripción del proyecto
        self.fecha_inicio = fecha_inicio  # Fecha de inicio del proyecto
        self.fecha_fin = fecha_fin  # Fecha de finalización del proyecto
        self.responsables = responsables  # Lista de responsables del proyecto

# Definición de la clase Empleado
class Empleado:
    # Constructor de la clase Empleado
    def __init__(self, nombre, cargo, proyecto_asignado):
        self.nombre = nombre  # Nombre del empleado
        self.cargo = cargo  # Cargo del empleado
        self.proyecto_asignado = proyecto_asignado  # Proyecto asignado al empleado

# Creación de instancias de proyectos
proyecto_1 = Proyecto("Desarrollo de Software", "Desarrollo de una nueva aplicación móvil", "2024-01-01", "2024-06-30", ["Juan", "María"])
proyecto_2 = Proyecto("Implementación de CRM", "Implementación de un sistema CRM para la gestión de clientes", "2024-02-15", "2024-08-31", ["Pedro", "Ana"])

# Creación de instancias de empleados
empleado_1 = Empleado("Juan", "Desarrollador", proyecto_1)
empleado_2 = Empleado("María", "Diseñadora UI/UX", proyecto_1)
empleado_3 = Empleado("Pedro", "Gerente de Proyecto", proyecto_2)
empleado_4 = Empleado("Ana", "Analista de Negocios", proyecto_2)

# Asignación de responsables a los proyectos
proyecto_1.responsables = [empleado_1, empleado_2]
proyecto_2.responsables = [empleado_3, empleado_4]

# Impresión de los detalles del proyecto 1
print("Proyecto:", proyecto_1.nombre)
print("Descripción:", proyecto_1.descripcion)
print("Fecha de inicio:", proyecto_1.fecha_inicio)
print("Fecha de finalización:", proyecto_1.fecha_fin)
print("Responsables:")
for responsable in proyecto_1.responsables:
    print("- Nombre:", responsable.nombre)
    print("  Cargo:", responsable.cargo)

# Impresión de los detalles del proyecto 2
print("\nProyecto:", proyecto_2.nombre)
print("Descripción:", proyecto_2.descripcion)
print("Fecha de inicio:", proyecto_2.fecha_inicio)
print("Fecha de finalización:", proyecto_2.fecha_fin)
print("Responsables:")
for responsable in proyecto_2.responsables:
    print("- Nombre:", responsable.nombre)
    print("  Cargo:", responsable.cargo)