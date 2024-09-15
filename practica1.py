# -*- coding: utf-8 -*-
"""
Created on Tue May 14 17:05:06 2024

@author: User
"""

import pandas as pd
import random
import heapq  # Usaremos un min-heap para la implementación de Dijkstra

# Representación de los centros de distribución como nodos del grafo
V = list('ABCDEFGH')  # Centros de distribución

# Creación del grafo, representando las conexiones directas entre los centros
grafo = pd.DataFrame(index=V, columns=V)

# Asignar conexiones con pesos aleatorios entre los nodos
grafo.loc['A', ['B', 'C', 'G']] = [random.randint(1, 10) for _ in range(3)] 
grafo.loc['B', ['A', 'D', 'G']] = [random.randint(1, 10) for _ in range(3)] 
grafo.loc['C', ['A', 'D', 'E']] = [random.randint(1, 10) for _ in range(3)] 
grafo.loc['D', ['B', 'C', 'F']] = [random.randint(1, 10) for _ in range(3)] 
grafo.loc['E', ['C', 'F', 'G']] = [random.randint(1, 10) for _ in range(3)] 
grafo.loc['F', ['D', 'E', 'H']] = [random.randint(1, 10) for _ in range(3)] 
grafo.loc['G', ['A', 'B', 'E']] = [random.randint(1, 10) for _ in range(3)]
grafo.loc['H', ['F']] = [random.randint(1, 10)]

# Guardar el grafo en formato JSON para poder usar los datos externamente
grafo.to_json("grafo_con_pesos.json", orient='split')

# Nodo inicial (centro de distribución inicial) para Dijkstra
v1 = 'A'  # Se puede cambiar este nodo para que inicie desde otro centro

# Función para aplicar el algoritmo de Dijkstra
def dijkstra(grafo, start):
    # Diccionario de distancias desde el nodo inicial a todos los demás
    distancias = {nodo: float('inf') for nodo in grafo.index}
    distancias[start] = 0
    
    # Cola de prioridad para seleccionar el nodo con menor distancia
    pq = [(0, start)]  # (distancia, nodo)
    visitados = set()
    padres = {start: None}  # Para reconstruir el camino más corto

    while pq:
        (dist_actual, nodo_actual) = heapq.heappop(pq)
        
        if nodo_actual in visitados:
            continue
        
        visitados.add(nodo_actual)
        
        # Explorar los vecinos del nodo actual
        for vecino in grafo.columns:
            if pd.notna(grafo.loc[nodo_actual, vecino]):  # Si hay una conexión válida
                peso = grafo.loc[nodo_actual, vecino]
                nueva_dist = dist_actual + peso
                
                # Si encontramos un camino más corto hacia el vecino
                if nueva_dist < distancias[vecino]:
                    distancias[vecino] = nueva_dist
                    padres[vecino] = nodo_actual
                    heapq.heappush(pq, (nueva_dist, vecino))

    return distancias, padres

# Ejecutar Dijkstra desde el nodo inicial
distancias, padres = dijkstra(grafo, v1)

# Mostrar los resultados: distancia más corta desde el nodo inicial 'v1' a todos los demás nodos
print(f"Distancias más cortas desde el nodo {v1}:")
for nodo, dist in distancias.items():
    print(f"Distancia a {nodo}: {dist}")

# Función para reconstruir el camino más corto desde el nodo inicial a un destino dado
def reconstruir_camino(padres, destino):
    camino = []
    while destino:
        camino.append(destino)
        destino = padres[destino]
    camino.reverse()
    return camino

# Mostrar los caminos más cortos hacia cada nodo
print("\nCaminos más cortos desde el nodo A:")
for nodo in V:
    if nodo != v1:
        camino = reconstruir_camino(padres, nodo)
        print(f"Camino hacia {nodo}: {' -> '.join(camino)}")
