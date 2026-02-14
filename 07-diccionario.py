import os
os.system("cls")

'''
dict=diccionario
¿Qué es un diccionario?
Un diccionario es una estructura de datos que almacena informacion 
en pares clave-valor.

No se accede por posición si no por clave.
'''

#Ejemplo
alumno ={
    "nombre":"Ana",
    "edad":21,
    "carrera": "Ingenieria"
}

print(type(alumno))
print(alumno)

print("print(alumno['nombre'])= ", alumno["nombre"])
print("print(alumno.get('edad'))= ",alumno.get("edad"))


#agregar o modificar valores

alumno["promedio"]=9.2
print(alumno)
alumno["edad"]=22
print(alumno)

#eliminar ya sea por clave o por valor
del alumno["carrera"]
print(alumno)

#recorrer un diccionario
for clave in alumno:
    print(clave)
    print(clave, ":", alumno[clave])


#funciones útiles para diccionarios
print("Claves pares clave-valor: ",len(alumno))
print("Claves del diccionario: ",alumno.keys())
print("Valores del diccionario: ",alumno.values())
print("Pares clave-valor. ",alumno.items())

ico201=[alumno,alumno,alumno]
print(ico201)



alumno ={
    "nombre":"",
    "edad": 0,
    "carrera": ""
}

diccionario= []

menu=int(input("Ingrese el número de diccionarios que desea obtener: "))

for i in range(menu):

    nombre=input("Nombre: ")
    edad=int(input("Edad : "))
    carrera=input("Carrera: ")
    

    alumno["nombre"] = nombre
    alumno["edad"]=edad
    alumno["carrera"]=carrera

    diccionario.append(alumno.copy())

print("Lista de diccionario")
for alumno in diccionario:
    print(alumno)