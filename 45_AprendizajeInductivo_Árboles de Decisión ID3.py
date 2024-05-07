#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Aprendizaje Inductivo
# Tema: Árboles de Decisión: ID3

#El algoritmo ID3 es un algoritmo de aprendizaje inductivo que construye un árbol de decisión a partir de un conjunto de datos de entrenamiento utilizando un enfoque de división recursiva. El algoritmo ID3 es un algoritmo de aprendizaje supervisado que se utiliza para la clasificación de datos. 
#En este ejemplo, utilizaremos el algoritmo ID3 para construir un árbol de decisión para clasificar las flores del conjunto de datos de iris.

from sklearn.datasets import load_iris  # se utiliza para cargar el conjunto de datos de iris
from sklearn.model_selection import train_test_split    # se utiliza para dividir el conjunto de datos en un conjunto de entrenamiento y un conjunto de prueba
from sklearn.tree import DecisionTreeClassifier   # se utiliza para crear un clasificador de árbol de decisión
from sklearn.metrics import accuracy_score  # se utiliza para calcular la precisión de las predicciones

# Cargamos el conjunto de datos de iris
iris = load_iris()
X = iris.data
y = iris.target

# Dividimos el conjunto de datos en un conjunto de entrenamiento y un conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creamos un clasificador de árbol de decisión
clf = DecisionTreeClassifier(criterion='entropy')

# Entrenamos el clasificador en el conjunto de entrenamiento
clf.fit(X_train, y_train)

# Predecimos las etiquetas para el conjunto de prueba
y_pred = clf.predict(X_test)

# Calculamos la precisión de las predicciones
accuracy = accuracy_score(y_test, y_pred)

print(f'Accuracy: {accuracy}')