import os
os.system("cls")
alumnos = []
while True:
    try:
        num = int(input("¿Cuántos almnos quieres ingresar?"))
        break #Si la conversión es exitosa, salimos del bucle
    except ValueError:
        print("Error: Por favor ingresa un numero entero valido")

for i in range(num):
    nombre = input("Nombre del alumno: ")  
    edad = int(input("Edad del alumno: "))
    materia = input("Materia del alumno: ")
    calificacion = float(input("Calificacion del alumno: 0"))

alumno = {
    "nombre": nombre,
    "edad": edad,
    "materia":materia,
    "calificacion":calificacion
}
alumnos.append(alumno)
#calcular el promedio de calificaciones
if alumnos:
    total_calificaciones = sum(alumno["calificacion"] for alumno in alumnos)
    promedio = total_calificaciones / len(alumnos)
    print("Promedio de califiaciones {promedio}")
else:
    print("No se ingresaronn calificaciones.")
#mostrar la lista completa de alumnos
print("Lista completa de alumnos: ")
for alumno in alumnos:
    print(alumno)