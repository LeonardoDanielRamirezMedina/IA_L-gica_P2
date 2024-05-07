#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Aprendizaje Inductivo
# Tema: Explicaciones e Información Relevante

# En el aprendizaje automático, a menudo queremos entender qué características son las más importantes para nuestras predicciones.

from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris

# Cargar el conjunto de datos de iris
iris = load_iris()  # se utiliza para cargar el conjunto de datos de iris
X = iris.data   # características
y = iris.target # etiquetas

# Crear un modelo de árbol de decisión
model = DecisionTreeClassifier()

# Entrenar el modelo en el conjunto de datos
model.fit(X, y)

# Imprimir la importancia de las características
print("Importancia de las características:", model.feature_importances_)