input = '''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
1
'''

lineas = input.split()
suma = 0

for linea in lineas:
    digito1 = ""
    digito2 = ""
    for caracter in linea:
        if caracter.isdigit():
            digito1 = caracter
            break

    for indice in range(len(linea) - 1, -1, -1):
        caracter = linea[indice]
        if caracter.isdigit():
            digito2 = caracter
            break
    
    suma += int(digito1) * 10 + int(digito2)
    # suma += int(digito1 + digito2)
print(suma)