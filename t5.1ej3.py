import numpy as np

def estandarizar(matriz, modo="Por_defecto"):
    matriz_n = matriz.copy()
    filas, _ = matriz_n.shape

    # Compruebo que el primer argumento es un ndarray
    if type(matriz) != np.ndarray:
        raise ValueError("El primer argumento de la función debe ser un array.")
    
    if modo == "Por_defecto":
        mean = matriz_n.mean()
        std = matriz_n.std()
        matriz_n = (matriz_n - mean)/std
    elif modo == "Columnas":
        mean = matriz_n.mean(axis=0)
        std = matriz_n.std(axis=0)
        matriz_n = (matriz_n - mean)/std
    elif modo == "Filas":
        mean = matriz_n.mean(axis=1).reshape(filas,1)
        std = matriz_n.std(axis=1).reshape(filas,1)
        matriz_n = (matriz_n - mean)/std
    else:
        raise ValueError("El modo introducido no es correcto.")
    return matriz_n

matriz = np.array([[1,2,3,4],
                   [4,5,6,7],
                   [7,8,9,10]],
                   dtype=float)

print("La matriz original es:\n", matriz)
print("\nLa matriz estandarizada:\n", estandarizar(matriz))
print("\nLa matriz estandarizada por columnas:\n", estandarizar(matriz, modo="Columnas"))
print("\nLa matriz estandarizada por filas:\n", estandarizar(matriz, modo="Filas"))
# print("\nError:", estandarizar(matriz, modo="Error"))
