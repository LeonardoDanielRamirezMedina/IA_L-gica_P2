#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Lógica de 1er Orden
# Tema: Encadenamiento: Hacia Delante y Atrás

# El encadenamiento hacia delante y hacia atrás son dos estrategias de inferencia utilizadas en sistemas expertos y lógica de primer orden para derivar nuevas conclusiones a partir de un conjunto de reglas y hechos.

# Base de conocimientos
conocimientos = {   # Definimos una base de conocimientos con reglas lógicas
    "llueve": ["el suelo está mojado"],  # Si llueve, entonces el suelo está mojado
    "el suelo está mojado": ["los zapatos se mojan"]    # Si el suelo está mojado, entonces los zapatos se mojan
}

# Encadenamiento hacia delante
def encadenamiento_hacia_delante(conocimientos, datos):  # Función que realiza un encadenamiento hacia delante
    while True:
        nueva_informacion = False   # Inicializamos una variable para verificar si se ha agregado nueva información
        for dato in datos:  # Iteramos sobre los datos
            if dato in conocimientos:   # Si el dato está en la base de conocimientos
                conclusiones = conocimientos[dato]  # Obtenemos las conclusiones asociadas al dato
                for conclusion in conclusiones:  # Iteramos sobre las conclusiones
                    if conclusion not in datos: # Si la conclusión no está en los datos
                        datos.append(conclusion)    # Agregamos la conclusión a los datos
                        nueva_informacion = True    # Indicamos que se ha agregado nueva información
        if not nueva_informacion:   # Si no se ha agregado nueva información
            break   
    return datos    # Retornamos los datos actualizados

# Encadenamiento hacia atrás
def encadenamiento_hacia_atras(conocimientos, meta):    
    for dato, conclusiones in conocimientos.items():    # Iteramos sobre los datos y las conclusiones en la base de conocimientos
        if meta in conclusiones:    # Si la meta está en las conclusiones
            return encadenamiento_hacia_atras(conocimientos, dato)  # Realizamos un encadenamiento hacia atrás con el dato
    return meta

datos = ["llueve"]  # Datos iniciales
print(encadenamiento_hacia_delante(conocimientos, datos))  # ['llueve', 'el suelo está mojado', 'los zapatos se mojan']

meta = "los zapatos se mojan"   # Meta a alcanzar
print(encadenamiento_hacia_atras(conocimientos, meta))  # 'llueve'