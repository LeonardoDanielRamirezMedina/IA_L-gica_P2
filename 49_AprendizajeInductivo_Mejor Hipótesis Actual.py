#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Aprendizaje Inductivo
# Tema: Mejor Hipótesis Actual

# La mejor hipótesis actual es la hipótesis que el modelo ha aprendido de los datos de entrenamiento. En este ejemplo, utilizaremos un modelo de regresión lineal para encontrar la mejor hipótesis actual para un conjunto de datos de regresión.

from sklearn.linear_model import LinearRegression   #se utiliza para crear un modelo de regresión lineal
from sklearn.model_selection import train_test_split    # se utiliza para dividir el conjunto de datos en un conjunto de entrenamiento y un conjunto de prueba
from sklearn.datasets import make_regression    # se utiliza para generar un conjunto de datos de regresión

# Generar un conjunto de datos de regresión
X, y = make_regression(n_samples=100, n_features=1, noise=0.1)

# Dividir el conjunto de datos en un conjunto de entrenamiento y un conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Crear un modelo de regresión lineal
model = LinearRegression()

# Entrenar el modelo en el conjunto de entrenamiento
model.fit(X_train, y_train)

# La mejor hipótesis actual es la que el modelo ha aprendido de los datos de entrenamiento
print("Mejor hipótesis actual:", model.coef_)