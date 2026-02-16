'''
Docstring for operasBas

Realizar
1.- +
2.- -
3.- *
4.- /
5.- Salir

pedir la opcion con un menu (), y cada operacion sra una funcion:
suma(), resta(), dividir(), multiplicacion()

Antes de limpiar la pantalla mostrar el resultado de la operacion
'''
import os
os.system("cls")

def suma():
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    resultado = num1 + num2
    print("El resultado de la suma de {} y {} es: {}".format(num1, num2, resultado))

def resta():
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    resultado = num1 - num2
    print("El resultado de la resta de {} y {} es: {}".format(num1, num2, resultado))

def multiplicacion():
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    resultado = num1 * num2
    print("El resultado de la multiplicacion de {} y {} es: {}".format(num1, num2, resultado))
  
def division():
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    resultado = num1 / num2
    print("El resultado de la division de {} y {} es: {}".format(num1, num2, resultado))

print("Seleccione la operación que desea:")
print("1.- +")
print("2.- -")
print("3.- *")
print("4.- /")
print("5.- Salir")

menu = int(input("Ingrese la opcion a realizar (1/2/3/4/5): "))
os.system("cls")
if menu == 1:
    suma()
elif menu == 2:
    resta()
elif menu == 3:
    multiplicacion()
elif menu == 4:
    division()
elif menu == 5:
    print("Hasta luego")