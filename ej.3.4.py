def add_libro(biblioteca, titulo, autor, copias):
    if (titulo in biblioteca):
        # libro = biblioteca[titulo]
        # libro["copias"] += copias
        biblioteca[titulo]["copias"] += copias
    else:
        biblioteca[titulo] = {
            "autor": autor,
            "copias": copias,
            "prestamos": 0
        }

def prestar_libro(biblioteca, titulo):
    if (titulo in biblioteca):
        libro = biblioteca[titulo]
        if (libro["prestamos"] < libro["copias"]):
            libro["prestamos"] += 1
        else:
            print("No quedan copias para prestar de", titulo)
    else:
        print("El libro", titulo, "no existe en la biblioteca")
    

def devolver_libro(biblioteca, titulo):
    if (titulo in biblioteca):
        libro = biblioteca[titulo]
        if (libro["prestamos"] > 0):
            libro["prestamos"] -= 1
        else:
            print("El libro", titulo, "no está prestado")
    else:
        print("El libro", titulo, "no existe en la biblioteca")

def listar_libros(biblioteca):
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
add_libro(biblioteca, "El Quijote", "Miguel de Cervantes", 1)
add_libro(biblioteca, "El Señor de los Anillos", "J.R.R. Tolkien", 2)
prestar_libro(biblioteca, "El Señor de los Anillos")
prestar_libro(biblioteca, "El Señor de los Anillos")
prestar_libro(biblioteca, "El Señor de los Anillos")
prestar_libro(biblioteca, "El Señor de los Anillos")
prestar_libro(biblioteca, "El Padrino")
devolver_libro(biblioteca, "El Señor de los Anillos")
devolver_libro(biblioteca, "El Quijote")
devolver_libro(biblioteca, "El Padrino")
listar_libros(biblioteca)
listar_libros({})