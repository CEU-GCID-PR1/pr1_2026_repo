import parametros

def suma(a, b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a, b):
    return a * b

def division(a,b):
    if b == 0:
        raise ZeroDivisionError()
    return a/b

def potencia(base, exponente):
    return base ** exponente

def raiz_cuadrada(a):
    if a < 0:
        raise ValueError("Error: No se puede calcular la raíz cuadrada de un número negativo")
    return a ** 0.5

def valor_absoluto(a):
    return abs(a)

def radianes_a_grados(radianes):
    return radianes * parametros.RADIANES_A_GRADOS

def grados_a_radianes(grados):
    return grados / parametros.RADIANES_A_GRADOS

if __name__ == "__main__":
    assert suma(2,3) == 5
    assert resta(6,2) == 4
    assert multiplicacion(4,6) == 24
    assert division(8,4) == 2
    assert potencia(3,2) == 9
    assert raiz_cuadrada(25) == 5
    assert valor_absoluto(-12) == 12
    assert valor_absoluto(16) == 16
    print(radianes_a_grados(2.0943951))
    print(grados_a_radianes(90))