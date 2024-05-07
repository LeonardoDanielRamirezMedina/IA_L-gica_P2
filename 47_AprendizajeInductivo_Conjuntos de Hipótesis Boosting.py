#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Aprendizaje Inductivo
# Tema: Conjuntos de Hipótesis: Boosting

#El boosting es un enfoque de aprendizaje inductivo que combina múltiples clasificadores débiles para crear un clasificador fuerte. El algoritmo de boosting más común es AdaBoost, que ajusta secuencialmente los pesos de las instancias de entrenamiento para enfocarse en los ejemplos más difíciles de clasificar. 
#En este ejemplo, utilizaremos el algoritmo AdaBoost para clasificar las flores del conjunto de datos de iris.

from sklearn.datasets import load_iris  # se utiliza para cargar el conjunto de datos de iris
from sklearn.ensemble import AdaBoostClassifier # se utiliza para crear un clasificador de boosting
from sklearn.model_selection import train_test_split    # se utiliza para dividir el conjunto de datos en un conjunto de entrenamiento y un conjunto de prueba
from sklearn.metrics import accuracy_score  # se utiliza para calcular la precisión de las predicciones

# Cargar el conjunto de datos de ejemplo
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

# Entrenar un clasificador utilizando el algoritmo de boosting (AdaBoost)
clf = AdaBoostClassifier(n_estimators=100, random_state=42) #adaBoost es un algoritmo de boosting que ajusta secuencialmente los pesos de las instancias de entrenamiento para enfocarse en los ejemplos más difíciles de clasificar.
clf.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
predicciones = clf.predict(X_test)  # se utiliza para predecir las etiquetas de las instancias de prueba

# Calcular la precisión de las predicciones
precision = accuracy_score(y_test, predicciones)    #accuracy_score se utiliza para calcular la precisión de las predicciones
print("Precisión del clasificador:", precision) #se imprime la precisión del clasificador
