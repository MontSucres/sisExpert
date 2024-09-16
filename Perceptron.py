import numpy as np
import random

# Generar pesos aleatorios iniciales (Altura, Peso, Edad)
W = np.array([random.uniform(-1, 1) for _ in range(3)])  # Pesos aleatorios
Wn = W.copy()

# Datos de entrada (Altura, Peso, Edad) - Características de 4 personas
# Altura: 1 = Alta, -1 = Baja
# Peso: 1 = Pesado, -1 = Ligero
# Edad: 1 = Joven, -1 = Mayor
x = np.array([[1, -1, -1],  # Persona 1: Alta, Ligera, Mayor
              [1, 1, -1],   # Persona 2: Alta, Pesada, Mayor
              [1, -1, 1],   # Persona 3: Alta, Ligera, Joven
              [1, 1, 1]])   # Persona 4: Alta, Pesada, Joven

# Etiquetas: 1 = Apta para trabajo físico, -1 = No apta
# Suponemos que solo las personas jóvenes y pesadas son aptas
y = np.array([-1, -1, -1, 1])

# Arreglo para almacenar las salidas predichas
yf = np.zeros(4)

print("Pesos iniciales aleatorios:", Wn)

# Proceso de ajuste de pesos
for i in range(4):
    # Predicción (producto punto entre los pesos y las características)
    yp = np.sign(np.dot(Wn, x[i, :]))
    
    # Ajuste de pesos basado en el error de la predicción
    Wn = (Wn + (y[i] - yp) * (x[i, :]) / 2)
    
    # Mostrar los pesos ajustados en cada iteración
    print(f"Iteración {i + 1}: Pesos ajustados {Wn}")

# Predicción final con los pesos ajustados
for i in range(4):
    yf[i] = np.sign(np.dot(Wn, x[i, :]))

# Mostrar resultados
print("\nSalidas predichas después del ajuste de pesos:")
for i in range(4):
    print(f"Persona {i + 1}: Altura: {'Alta' if x[i, 0] == 1 else 'Baja'}, "
          f"Peso: {'Pesado' if x[i, 1] == 1 else 'Ligero'}, "
          f"Edad: {'Joven' if x[i, 2] == 1 else 'Mayor'} -> "
          f"Etiqueta real: {'Apta' if y[i] == 1 else 'No apta'}, "
          f"Predicción: {'Apta' if int(yf[i]) == 1 else 'No apta'}")
