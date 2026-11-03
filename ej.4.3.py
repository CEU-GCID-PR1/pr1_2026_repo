import csv
import os.path
import datetime

ARCHIVO = "asistencia.csv"
asistencia = {}
# alumnos = ["Alumno 1", "Alumno 2", "Alumno 3", "Alumno 4", "Alumno 5"]

def pasarAsistencia():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, 'r', encoding='UTF-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            count = 0
            for linea in csv_reader:
                if count > 0:
                    nombre = linea[0]
                    respuesta = ""
                    while respuesta != "s" and respuesta != "n":
                        respuesta = input(f"Asistencia de {nombre} (s/n): ")
                    if respuesta == "s":
                        asistencia[nombre] = 1
                    else:
                        asistencia[nombre] = 0
                count += 1
        with open(ARCHIVO, 'w', newline='', encoding='UTF-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['nombre', datetime.date.today()])
            for nombre in asistencia:
                csv_writer.writerow([nombre, asistencia[nombre]])
                
pasarAsistencia()