import numpy as np

def normalizar(matriz, modo="Por_defecto"):
    if modo == "Por_defecto":
        minimo = np.min(matriz)
        if minimo > 0:
            minimo = 0
        maximo = np.max(matriz)
        matriz = matriz + abs(minimo)
        print(matriz)
        matriz = matriz / (maximo + abs(minimo))
        return matriz
    elif modo == "Columnas":
        minimos = np.min(matriz, axis=0)
        min_neg = np.where(minimos < 0, abs(minimos), 0)
        matriz += min_neg
        matriz = matriz / np.max(matriz, axis=0)
        return matriz

matriz1 = np.array([-1,4,1])
print(normalizar(matriz1))

matriz = np.array([[-1,2,3,7],[4,2,4,3],[1,0,2,-4]])
print(normalizar(matriz))
print(normalizar(matriz, "Columnas"))
