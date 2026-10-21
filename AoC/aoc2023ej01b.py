numeroTexto = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

# Devuelve un int si hay un número en texto escrito al principio o -1 en caso contrario
def buscarNumeroTexto(linea):
    for i,numero in enumerate(numeroTexto):
        if linea[:len(numero)] == numero:
            return i + 1
    return -1


def buscarNumeroOne(linea):
    return linea[:3] == "one"

print(buscarNumeroTexto("abcone2threexyz")) # -1
print(buscarNumeroTexto("one2threexyz")) # 1
print(buscarNumeroTexto("eightwothree")) # 8
print(buscarNumeroTexto("on")) # 8
