def add_libro(biblioteca, titulo, autor, copias):
    # Posibles fallos:
    # ✓ copias negativas
    # ✓ Que ya exista el título y no coincida el autor
    # ✓ autor es un string vacío
    # ✓ titulo es un string vacío
    # - copias no es un número entero
    # - autor no es un string
    # - titulo no es un string
    # - biblioteca no es un diccionario
    # - biblioteca es un diccionario pero no tiene el formato adecuado
    if copias <= 0:
        raise ValueError("copias tiene que ser un entero positivo")
    if autor == "" or titulo == "":
        raise ValueError("autor y título no pueden estar vacíos")
    if (titulo in biblioteca):
        if biblioteca[titulo]['autor'] == autor: # Los autores coinciden
            # libro = biblioteca[titulo]
            # libro["copias"] += copias
            biblioteca[titulo]["copias"] += copias
        else: # Los autores no coinciden
            raise ValueError("Los autores no coinciden para el mismo libro")
    else:
        biblioteca[titulo] = {
            "autor": autor,
            "copias": copias,
            "prestamos": 0
        }

def prestar_libro(biblioteca, titulo):
    # Posibles fallos:
    # - No quedan copias para prestar
    # - El libro no está en la biblioteca
    # - titulo es un string vacío
    # - titulo no es un string
    # - biblioteca no es un diccionario
    # - biblioteca es un diccionario pero no tiene el formato adecuado
    if (titulo in biblioteca):
        libro = biblioteca[titulo]
        if (libro["prestamos"] < libro["copias"]):
            libro["prestamos"] += 1
        else:
            print("No quedan copias para prestar de", titulo)
    else:
        print("El libro", titulo, "no existe en la biblioteca")
    

def devolver_libro(biblioteca, titulo):
    # Posibles fallos:
    # - No hay ninguna copia de ese libro prestado
    # - El libro no está en la biblioteca
    # - titulo es un string vacío
    # - titulo no es un string
    # - biblioteca no es un diccionario
    # - biblioteca es un diccionario pero no tiene el formato adecuado
    if (titulo in biblioteca):
        libro = biblioteca[titulo]
        if (libro["prestamos"] > 0):
            libro["prestamos"] -= 1
        else:
            print("El libro", titulo, "no está prestado")
    else:
        print("El libro", titulo, "no existe en la biblioteca")

def listar_libros(biblioteca):
    # Posibles fallos:
    # - biblioteca no es un diccionario
    # - biblioteca es un diccionario pero no tiene el formato adecuado
    if len(biblioteca) == 0:
        print("La biblioteca esta vacía")
    else:
        print("\nLos libros de la biblioteca son los siguientes:")
        for titulo in biblioteca:
            libro = biblioteca[titulo]
            print(titulo)
            print("\tAutor:", libro["autor"])
            print("\tNúmero de copias:", libro["copias"])
            print("\tNúmero de préstamos:", libro["prestamos"])
            print()

biblioteca = {}
add_libro(biblioteca, "El Señor de los Anillos", "J.R.R. Tolkien", 1)
print(biblioteca)
print(biblioteca['El Señor de los Anillos'])
print(biblioteca['El Señor de los Anillos']['autor'])
print('El Señor de los Anillos' in biblioteca)
print('autor' in biblioteca['El Señor de los Anillos'])

biblioteca = {}
add_libro(biblioteca, "El Señor de los Anillos", "J.R.R. Tolkien", 1)
# add_libro(biblioteca, "El Señor de los Anillos", "J.R.R. Tolkien", -1)
# add_libro(biblioteca, "El Señor de los Anillos", "Tolkien", 1)

def opcion_add():
    titulo = input("Indique el título")
    autor = input("Indique el autor")
    copias = int(input("Indique el número de copias del libro"))
    try:
        add_libro(biblioteca, titulo, autor, copias)
    except:
        print("Los datos introducidos no son correctos")

def opcion_prestar():
    return

def opcion_devolver():
    return

def opcion_listar():
    return

def opcion_salir():
    print("Hasta pronto")

biblioteca = {}
opcion = ""
while opcion != "0":
    print("Elija una de las siguientes opciones:")
    print("\t1. Añadir un libro")
    print("\t2. Prestar un libro")
    print("\t3. Devolver un libro")
    print("\t4. Listar libros")
    print("\t0. Salir")
    opcion = input("")
    match(opcion):
        case "1":
            opcion_add()
        case "2":
            opcion_prestar()
        case "3":
            opcion_devolver()
        case "4":
            opcion_listar()
        case "0":
            opcion_salir()
        case _:
            print(opcion, " no es una opción válida")