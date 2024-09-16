import pandas as pd

# Representamos estaciones eléctricas (a-h) y costos de transmisión entre ellas
V = list('abcdefgh')  # a-h son estaciones eléctricas
grafo_red = pd.DataFrame(index=V, columns=V)

# Costos de transmisión entre estaciones (pesos en los caminos)
grafo_red.loc['a', ['b', 'c', 'g']] = [12, 20, 25]
grafo_red.loc['b', ['a', 'd', 'g']] = [12, 30, 35]
grafo_red.loc['c', ['a', 'd', 'e']] = [20, 40, 50]
grafo_red.loc['d', ['b', 'c', 'f']] = [30, 40, 55]
grafo_red.loc['e', ['c', 'f', 'g']] = [50, 45, 35]
grafo_red.loc['f', ['d', 'e', 'h']] = [55, 45, 60]
grafo_red.loc['g', ['a', 'b', 'e']] = [25, 35, 35]
grafo_red.loc['h', ['f']] = [60]

# Grafo final (visualización)
print("Matriz de costos de transmisión entre estaciones eléctricas (en unidades de costo):")
print(grafo_red)

# Función de recorrido por profundidad
def Prof(grafo_red, nodo_inicial):
    visitados = set()  # Conjunto para almacenar los nodos visitados
    arbol_expansion = []  # Lista para almacenar el árbol de expansión

    # Función interna para explorar recursivamente
    def explorar(nodo, visitados, arbol_expansion):
        visitados.add(nodo)  # Marcar el nodo como visitado
        # Iterar sobre los vecinos con caminos disponibles (> 0)
        for vecino in grafo_red.columns[(grafo_red.loc[nodo] > 0)]:
            if vecino not in visitados:
                arbol_expansion.append((nodo, vecino, grafo_red.loc[nodo, vecino]))  # Guardar nodo, vecino y costo
                explorar(vecino, visitados, arbol_expansion)  # Llamada recursiva para explorar vecinos

    # Comenzar la exploración desde el nodo inicial
    explorar(nodo_inicial, visitados, arbol_expansion)
    return arbol_expansion

# Realizamos el recorrido desde el nodo 'a' (puede ser cambiado)
arbol_expansion = Prof(grafo_red, 'a')  # 'a' es el nodo inicial (estación inicial)
print("\nÁrbol de expansión por profundidad:")
for (origen, destino, costo) in arbol_expansion:
    print(f"De estación {origen} a estación {destino}: {costo} unidades de costo")
