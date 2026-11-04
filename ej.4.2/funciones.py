import parametros

def suma(a, b):
    return a+b

def resta(a,b):
    return a-b

def division(a,b):
    if b == 0:
        raise ZeroDivisionError()
    return a/b

def radianes_a_grados(radianes):
    return radianes * parametros.RADIANES_A_GRADOS

if __name__ == "__main__":
    assert suma(2,3) == 5
    assert resta(6,2) == 4
    assert division(8,4) == 2
    print(radianes_a_grados(90))