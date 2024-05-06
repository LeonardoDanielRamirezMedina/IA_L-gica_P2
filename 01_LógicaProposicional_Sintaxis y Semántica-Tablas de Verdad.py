#------------ENFOQUE: LÓGICA--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Lógica Proposicional
#Tema: Sintaxis y Semántica: Tablas de Verdad

# En lógica proposicional, una tabla de verdad es una representación de todas las posibles combinaciones de valores de verdad para un conjunto de proposiciones.

# Definimos las proposiciones
proposiciones = [False, True]   #definimos las proposiciones como una lista de valores booleanos

print("Tabla de verdad AND:")
print("P\tQ\tP AND Q")
for P in proposiciones:     #iteramos sobre las proposiciones
    for Q in proposiciones:         #iteramos sobre las proposiciones
        print(f"{P}\t{Q}\t{P and Q}")       #mostramos los valores de verdad de P, Q y P AND Q

print("\nTabla de verdad OR:")
print("P\tQ\tP OR Q")
for P in proposiciones:     #iteramos sobre las proposiciones
    for Q in proposiciones:     #iteramos sobre las proposiciones
        print(f"{P}\t{Q}\t{P or Q}")    #mostramos los valores de verdad de P, Q y P OR Q

print("\nTabla de verdad NOT:")
print("P\tNOT P")
for P in proposiciones:    #iteramos sobre las proposiciones
    print(f"{P}\t{not P}")  #mostramos los valores de verdad de P y NOT P