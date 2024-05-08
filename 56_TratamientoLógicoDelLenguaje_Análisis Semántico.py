#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Tratamiento Lógico del Lenguaje
# Tema: Análisis Semántico

#El análisis semántico es el proceso de analizar el significado de una secuencia de tokens en un lenguaje de programación.

import ast  #Se importa el módulo ast que se utiliza para analizar código fuente de Python

class SemanticAnalyzer(ast.NodeVisitor):    #Se define la clase SemanticAnalyzer que hereda de ast.NodeVisitor
    def __init__(self):
        self.variables = set()  #Se inicializa el conjunto de variables

    def visit_Assign(self, node):
        # Cuando se asigna a una variable, la añadimos al conjunto de variables definidas
        for target in node.targets:
            if isinstance(target, ast.Name):
                self.variables.add(target.id)   #Se añade la variable al conjunto de variables definidas
        self.generic_visit(node)    #Se visita el nodo

    def visit_Name(self, node):
        # Cuando se usa una variable, comprobamos si ha sido definida
        if isinstance(node.ctx, ast.Load) and node.id not in self.variables:
            raise NameError(f"Variable '{node.id}' not defined")    #Se genera un error si la variable no ha sido definida
        self.generic_visit(node)    #Se visita el nodo

# Definimos un código de prueba
code = """
x = 1
y = x + 2
w = 5
z = w + 3
"""

# Parseamos el código a un AST
tree = ast.parse(code)

# Creamos un analizador semántico y lo ejecutamos en el AST
analyzer = SemanticAnalyzer()   #Se crea un analizador semántico
analyzer.visit(tree)    #Se visita el árbol

print("El análisis semántico ha sido exitoso, todas las variables están definidas correctamente.")
