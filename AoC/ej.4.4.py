def contar_caracteres(nombre_fichero):
    with open(nombre_fichero, 'r', encoding='UTF-8') as reader:
        texto = reader.read()
        contador = {}
        for caracter in texto:
            if caracter in contador:
                contador[caracter] += 1
            else:
                contador[caracter] = 1
    return contador

print(contar_caracteres("el_quijote.txt"))