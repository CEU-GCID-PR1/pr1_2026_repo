import numpy as np
def elementos_mayores(matriz, n):
    return matriz[matriz > n]

matriz = np.random.rand(4,4)
print(matriz)
print(elementos_mayores(matriz, 0.5))