import funciones

def mostrar_menu():
    print("Selecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("7. Radianes a grados")
    print("8. Salir")

def preguntar_dos_numeros():
    n1 = input("Introduce el primer número: ")
    n2 = input("Introduce el segundo número: ")
    return n1,n2

opcion = 0
print("\nCalculadora\n")
while opcion != "8":
    mostrar_menu()
    opcion = input("Seleccione la opción: ")
    match opcion:
        case "1":
            n1,n2 = preguntar_dos_numeros()
            print(funciones.suma(n1,n2))
        case _:
            print("Opción introducida incorrecta")
print("Se terminó el programa")