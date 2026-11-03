import random
import os.path

FICHERO_ALUMNOS = "lista_alumnos.txt"
FICHERO_ALUMNOS_PENDIENTES = "lista_alumnos_pendientes.txt"

def obtenerAlumnosDeFichero(fichero):
    if (os.path.exists(fichero)):
        with open(fichero, 'r', encoding='UTF-8') as reader:
            return reader.read().splitlines()
    return []

def seleccionarAlumno(lista_alumnos):
    alumno_seleccionado = lista_alumnos.pop()
    print(alumno_seleccionado)
    # texto = ""
    # for alumno in lista_alumnos:
    #     texto += alumno + '\n'
    # with open(FICHERO_ALUMNOS_PENDIENTES, 'w', encoding='UTF-8') as writer:
    #     writer.write(texto)
    with open(FICHERO_ALUMNOS_PENDIENTES, 'w', encoding='UTF-8') as writer:
        writer.write('\n'.join(str(alumno) for alumno in lista_alumnos))
    
alumnos_pendientes = obtenerAlumnosDeFichero(FICHERO_ALUMNOS_PENDIENTES)
if len(alumnos_pendientes) == 0:
    alumnos_pendientes = obtenerAlumnosDeFichero(FICHERO_ALUMNOS)
    random.shuffle(alumnos_pendientes)
seleccionarAlumno(alumnos_pendientes)
