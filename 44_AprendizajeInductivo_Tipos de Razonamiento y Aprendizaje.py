#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Aprendizaje Inductivo
# Tema: Tipos de Razonamiento y Aprendizaje

# Los tipos de razonamiento y aprendizaje son enfoques diferentes para la resolución de problemas y la toma de decisiones en inteligencia artificial.

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

#variables predictoras (clima, hora, eventos en la ciudad, etc.) y variable objetivo (tráfico)
datos = {
    'clima': [1, 2, 3, 1, 2, 3, 2, 3, 1, 2],  # Ejemplo de codificación de clima (1: soleado, 2: nublado, 3: lluvioso)
    'hora': [8, 9, 10, 11, 12, 13, 14, 15, 16, 17],  # Hora del día
    'eventos': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],  # Ejemplo de eventos en la ciudad (0: sin eventos, 1: con eventos)
    'trafico': [20, 25, 30, 35, 40, 45, 50, 55, 60, 65]  # Ejemplo de nivel de tráfico
}

# Convertir los datos en una matriz para el aprendizaje automático
X = np.array(list(zip(datos['clima'], datos['hora'], datos['eventos'])))    #variables predictoras
y = np.array(datos['trafico'])  #variable objetivo

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)   #80% de los datos para entrenamiento y 20% para prueba

# Entrenar diferentes modelos de aprendizaje automático para predecir el tráfico
# Modelo de regresión lineal
modelo_lr = LinearRegression()
modelo_lr.fit(X_train, y_train) #entrenamiento

# Modelo de SVM (Support Vector Machine) para regresión
modelo_svm = SVR(kernel='linear')   #kernel lineal
modelo_svm.fit(X_train, y_train)    #entrenamiento

# Modelo de Bosques Aleatorios
modelo_rf = RandomForestRegressor(n_estimators=100, random_state=42)    #100 árboles
modelo_rf.fit(X_train, y_train) #entrenamiento

# Función para evaluar los modelos
def evaluar_modelo(modelo, X_test, y_test): #evaluar el modelo
    predicciones = modelo.predict(X_test)   #predicciones
    error = mean_squared_error(y_test, predicciones)    #error cuadrático medio
    return error    #retornar el error

# Evaluar los modelos
error_lr = evaluar_modelo(modelo_lr, X_test, y_test)    #error de regresión lineal
error_svm = evaluar_modelo(modelo_svm, X_test, y_test)  #error de SVM
error_rf = evaluar_modelo(modelo_rf, X_test, y_test)    #error de Bosques Aleatorios

# Imprimir los errores de los modelos
print("Error de Regresión Lineal:", error_lr)   #imprimir el error de regresión lineal
print("Error de SVM:", error_svm)   #imprimir el error de SVM
print("Error de Bosques Aleatorios:", error_rf) #imprimir el error de Bosques Aleatorios
