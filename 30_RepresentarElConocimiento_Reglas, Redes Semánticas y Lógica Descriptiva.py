#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Representar el Conocimiento
# Tema: Reglas, Redes Semánticas y Lógica Descriptiva

# las reglas, redes semánticas y lógica descriptiva son enfoques que permiten representar el conocimiento de forma estructurada y lógica

# Sistema de recomendación de películas basado en reglas
usuario_preferencias = {    # se crea un diccionario con las preferencias del usuario
    "género": "acción",    
    "director": "Christopher Nolan",    # director de la película
    "año": 2000   # año de lanzamiento de la película
}

def recomendar_pelicula(preferencias):  # función que recomienda una película basada en las preferencias del usuario
    if preferencias["género"] == "acción" and preferencias["director"] == "Christopher Nolan":  # si el género es acción y el director es Christopher Nolan
        return "Memento"    # se recomienda la película "Memento"
    elif preferencias["género"] == "drama" and preferencias["año"] > 2010:  # si el género es drama y el año es mayor a 2010
        return "La La Land"   # se recomienda la película "La La Land"
    else:   
        return "No se encontró una recomendación adecuada"  # en caso contrario, no se puede determinar una recomendación

print("Recomendación de película:", recomendar_pelicula(usuario_preferencias))  # se imprime la recomendación de película
