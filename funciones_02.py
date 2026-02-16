import os

def suma():
    os.system("cls")
    a=int(input("Numero1: "))
    b=int(input("Numero1: "))
    res=a+b
    print("La suma es: ",res)
    input()
    return res

def resta():
    os.system("cls")
    a=int(input("Numero1: "))
    b=int(input("Numero1: "))
    res=a-b
    print("La resta es: ",res)
    input()    
    return res
def menu():
    op=0
    while op!=5:
        os.system("cls")
        print("1.- +\n2.- - \n3.- *\n4.- /\n5.- salir\n")
        op=int(input("Opcion: "))
        if op == 1:
            suma()
        if op == 2:
            resta()               
if __name__==("__main__"):
   menu()  