import random
numero_secreto = random.randrange(1,101)
intentos = 0
is_running = True

while is_running:
    datos_introducidos = input("Introduzca un número entre el 1 y el 100")
    datos_validos = True
    for letra in datos_introducidos:
        if letra not in "0123456789":
            datos_validos = False
    if datos_validos:
        numero_usuario = int(datos_introducidos)
        if numero_usuario >= 1 and numero_usuario <= 100:
            intentos += 1
            if numero_usuario == numero_secreto:
                print("¡Felicidades!")
                print("El número de intentos ha sido: ", intentos)
                is_running = False
            elif numero_usuario > numero_secreto:
                print("El número que buscas es menor que ", numero_usuario)
            else:
                print("El número que buscas es mayor que ", numero_usuario)
        else:
            print("El número introducido no está en el rango")
    else:
        print("No has introducido datos correctos")
   