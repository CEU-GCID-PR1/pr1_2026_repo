import numpy as np

def normalizar_por_defecto(matriz):
    minimo = np.min(matriz)
    if minimo > 0:
        minimo = 0
    maximo = np.max(matriz)
    matriz_norm = matriz + abs(minimo)
    return matriz_norm / (maximo + abs(minimo))

def normalizar(matriz, modo="Por_defecto"):
    matriz_norm = None
    if modo == "Por_defecto":
        matriz_norm = normalizar_por_defecto(matriz)
    elif modo == "Columnas":
        #print(matriz)
        minimos = np.min(matriz, axis=0)
        min_neg = np.where(minimos < 0, abs(minimos), 0)
        matriz_norm = matriz + min_neg
        matriz_norm = matriz_norm / np.max(matriz_norm, axis=0)
    elif modo == "Filas":
        minimos = matriz.min(axis=1)
        min_neg = np.where(minimos < 0, abs(minimos), 0)
        min_neg_col = min_neg.reshape(-1,1)
        matriz_norm = matriz + min_neg_col
        max = matriz_norm.max(axis=1)
        max_col = max.reshape(-1,1)
        matriz_norm = matriz_norm / max_col
    elif modo == "Centrada_en_cero":
        matriz_norm = normalizar_por_defecto(matriz) - 0.5
    else:
        raise ValueError("El modo no es correcto")
    return matriz_norm

matriz1 = np.array([-1,4,1])
print(normalizar(matriz1))

matriz = np.array([[-1,2,4,6],[4,2,-4,3],[1,0,5,-4]])
print("\nMatriz original:\n", matriz)
print("\nMatriz normalizada:\n", normalizar(matriz))
print("\nMatriz normalizada por columnas:\n", normalizar(matriz, "Columnas"))
print("\nMatriz normalizada por filas:\n", normalizar(matriz, "Filas"))
print("\nMatriz normalizada centrada en cero:\n", normalizar(matriz, "Centrada_en_cero"))
# print("\nError:\n", normalizar(matriz, "Otro"))
