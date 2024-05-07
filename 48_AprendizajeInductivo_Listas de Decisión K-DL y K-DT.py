#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Aprendizaje Inductivo
# Tema: Listas de Decisión: K-DL y K-DT

# Las listas de decisión son un enfoque de aprendizaje inductivo que utiliza una lista de reglas de decisión para clasificar instancias. En este ejemplo, utilizaremos el algoritmo de listas de decisión K-DL (K-Decision Lists) para clasificar las flores del conjunto de datos de iris.

from sklearn.datasets import load_diabetes  # se utiliza para cargar el conjunto de datos de diabetes
from sklearn.model_selection import train_test_split    # se utiliza para dividir el conjunto de datos en un conjunto de entrenamiento y un conjunto de prueba
from sklearn.linear_model import LogisticRegression   # se utiliza para crear un modelo de regresión logística
from sklearn.metrics import accuracy_score  # se utiliza para calcular la precisión de las predicciones

# Cargar el conjunto de datos de diabetes
diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target

# Dividir el conjunto de datos en un conjunto de entrenamiento y un conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear un modelo de regresión logística
model = LogisticRegression()

# Entrenar el modelo en el conjunto de entrenamiento
model.fit(X_train, y_train)

# Predecir las etiquetas para el conjunto de prueba
y_pred = model.predict(X_test)

# Calcular la precisión de las predicciones
accuracy = accuracy_score(y_test, y_pred)

print(f'Accuracy: {accuracy}')