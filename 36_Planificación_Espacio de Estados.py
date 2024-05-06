#---------------ENFOQUE: LÓGICA-----------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Planificación
# Tema: Espacio de Estados

# En el enfoque de planificación de espacio de estados, se busca un camino desde un nodo de inicio hasta un nodo meta en un grafo representado por conexiones entre nodos.

# Importamos deque de collections para usar una cola de doble extremo
from collections import deque

# Esta función busca un camino desde un nodo de inicio hasta un nodo meta en un grafo representado por conexiones
def buscar_camino(inicio, meta, conexiones):
    # Inicializamos una cola con el nodo de inicio y el camino inicial
    cola = deque([(inicio, [inicio])])
    # Mientras haya nodos en la cola
    while cola:
        # Obtenemos el primer nodo y el camino hasta ese nodo
        (nodo, camino) = cola.popleft()
        # Para cada nodo adyacente al nodo actual
        for siguiente in conexiones.get(nodo, []):
            # Si el nodo adyacente no está en el camino actual (para evitar ciclos)
            if siguiente not in camino:
                # Si el nodo adyacente es la meta, retornamos el camino hasta la meta
                if siguiente == meta:
                    return camino + [siguiente]
                # Si no, agregamos el nodo adyacente y el camino hasta él a la cola
                else:
                    cola.append((siguiente, camino + [siguiente]))
    # Si no encontramos un camino, retornamos None
    return None

# Definimos los nodos y las conexiones entre ellos
conexiones = {
    'casa': ['tienda', 'parque'],
    'tienda': ['escuela', 'trabajo'],
    'parque': ['trabajo'],
    'escuela': ['casa'],
    'trabajo': ['casa']
}

# Definimos el nodo de inicio y el nodo meta
inicio = 'casa'
meta = 'trabajo'

# Buscamos un camino desde el inicio hasta la meta
camino = buscar_camino(inicio, meta, conexiones)
# Imprimimos el camino encontrado
print("Camino encontrado:", camino)