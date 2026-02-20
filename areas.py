import os, math
os.system("cls")
def cuadrado():
    lado = float(input("Ingrese la medida del lado del cuadrado: "))
    area = lado * lado
    print("El area del cuadrado es: {}".format(area))
    input("Presione Enter para continuar...")

def rectangulo():
    base = float(input("Ingrese la base del rectangulo: "))
    altura = float(input("Ingrese la altura del rectangulo: "))
    area = base * altura
    print("El area del rectangulo es: {}".format(area))
    input("Presione Enter para continuar...")

def triangulo():
    base = float(input("Ingrese la base del triangulo: "))
    altura = float(input("Ingrese la altura del triangulo: "))
    area = (base * altura) / 2
    print("El area del triangulo es: {}".format(area))
    input("Presione Enter para continuar...")

def circulo():
    radio = float(input("Ingrese el radio del circulo: "))
    area = math.pi *(radio ** 2)
    print("El area del circulo es: {}".format(area))
    input("Presione Enter para continuar...")

def trapecio():
    menor = float(input("Ingrese la base menor del trapecio: "))
    mayor = float(input("Ingrese la base mayor del trapecio: "))
    altura = float(input("Ingrese la altura del trapecio: "))
    area = ((menor + mayor) * altura) / 2
    print("El area del trapecio es: {}".format(area))
    input("Presione Enter para continuar...")

def menu():
    opcion = 0
    
    while opcion != 6:
        os.system("cls") 
        print("Seleccione la operación que desea:")
        print("1.- Cuadrado")
        print("2.- Rectangulo")
        print("3.- Triangulo")
        print("4.- Circulo")
        print("5.- Trapecio")
        print("6.- Salir")
        try:
            opcion = int(input("Ingrese la opcion (1/2/3/4/5/6): "))
        except ValueError:
            print("Debe ingresar un numero valido.")
            input("Presione Enter para continuar...")
            continue
        if opcion == 1:
            cuadrado()
        elif opcion == 2:
            rectangulo()
        elif opcion == 3:
            triangulo()
        elif opcion == 4:
            circulo()
        elif opcion == 5:
            trapecio()
        elif opcion == 6:
            print("Hasta luego!!!!")
        else:
            print("Opcion no valida.")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    menu()