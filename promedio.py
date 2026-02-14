import os
os.system("cls")

diccionario = []
menu = int(input("Ingrese el número de alumnos que desea registrar: "))
print("|--------------------------------------------|")

for i in range(menu):

    alumno = {} 

    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    materia = input("Materia: ")
    calificacion = float(input("Calificación: "))  #convertir

    alumno["nombre"] = nombre
    alumno["edad"] = edad
    alumno["materia"] = materia
    alumno["calificacion"] = calificacion

    diccionario.append(alumno)

print("-------------------")
print("|------- Lista de alumnos -------|")

for alumno in diccionario:
    print(alumno)

print("|----------------------------------|")
 
suma = 0
for alumno in diccionario:
    suma += alumno["calificacion"]

if len(diccionario) > 0:
    promedio = suma / len(diccionario)
    print("El promedio es:", promedio)
else:
    print("No hay datos para calcular promedio.")


alumno = {
    "registro": len(diccionario)
}
print("Registro en el diccionario: ", len(diccionario))