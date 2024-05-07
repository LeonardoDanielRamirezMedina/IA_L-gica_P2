#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Aprendizaje Inductivo
# Tema: Árboles de Regresión: M5

# M5 es un algoritmo de aprendizaje inductivo que construye un árbol de regresión a partir de un conjunto de datos de entrenamiento utilizando un enfoque de división recursiva.
# El algoritmo M5 es un algoritmo de aprendizaje supervisado que se utiliza para la regresión de datos. En este ejemplo, utilizaremos el algoritmo M5 para construir un árbol de regresión para predecir los precios de las casas basándonos en el número de habitaciones, el tamaño del terreno y la distancia a los servicios.

# Importamos las bibliotecas necesarias
import numpy as np
import pandas as pd # se utiliza para trabajar con datos tabulares
from sklearn.model_selection import train_test_split    # se utiliza para dividir el conjunto de datos en un conjunto de entrenamiento y un conjunto de prueba
from sklearn.tree import DecisionTreeRegressor  # se utiliza para crear un árbol de regresión
from sklearn.metrics import mean_squared_error  # se utiliza para calcular el error cuadrático medio

# Establecemos una semilla para la generación de números aleatorios para que los resultados sean reproducibles
np.random.seed(42)

# Definimos el número de muestras que queremos generar
num_muestras = 1000

# Generamos características aleatorias para nuestras muestras
num_habitaciones = np.random.randint(1, 6, num_muestras)  # Número de habitaciones
tamanio_terreno = np.random.randint(500, 3000, num_muestras)  # Tamaño del terreno
distancia_servicios = np.random.randint(1, 11, num_muestras)  # Distancia a servicios

# Generamos los precios de las casas basándonos en nuestras características
precio = 50000 + 20000*num_habitaciones + 50*tamanio_terreno - 500*distancia_servicios + np.random.normal(0, 10000, num_muestras)

# Creamos un DataFrame de pandas con nuestros datos
datos = pd.DataFrame({
    'Num_Habitaciones': num_habitaciones,
    'Tamanio_Terreno': tamanio_terreno,
    'Distancia_Servicios': distancia_servicios,
    'Precio': precio
})

# Separamos nuestras características (X) de nuestra variable objetivo (y)
X = datos.drop('Precio', axis=1)
y = datos['Precio']

# Dividimos nuestros datos en un conjunto de entrenamiento y un conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creamos un árbol de regresión y lo entrenamos con nuestros datos de entrenamiento
arbol_regresion = DecisionTreeRegressor()
arbol_regresion.fit(X_train, y_train)

# Realizamos predicciones en nuestro conjunto de prueba
predicciones = arbol_regresion.predict(X_test)

# Calculamos el error cuadrático medio de nuestras predicciones
mse = mean_squared_error(y_test, predicciones)

# Imprimimos el error cuadrático medio
print("Error cuadrático medio:", mse)