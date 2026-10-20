def nota_media(notas):
    suma = 0
    for nota in notas:
        suma += nota
    return round(suma / len(notas), 2)

def mayusculas(nombre):
    nombre.upper()

def resultados(estudiantes):
    for estudiante in estudiantes:
        print("La nota promedio de " + estudiante + " es ", nota_media(estudiantes[estudiante]))

estudiantes = {}
quedanEstudiantes = True

while quedanEstudiantes:
    nombre = input("Introduzca el nombre del estudiante. Introduzca terminar para acabar el programa: ")
    if nombre == "terminar":
        quedanEstudiantes = False
    else:
        notas = input("Introduzca todas las notas de estudiante separadas por comas: ") # 8.2,7,9.1
        lista_notas = []
        for nota in notas.split(","):
            lista_notas.append(float(nota))
        estudiantes[nombre] = lista_notas
        # print("La nota media de " + nombre + " es " + str(nota_media(lista_notas)))
print(estudiantes)

resultados(estudiantes)