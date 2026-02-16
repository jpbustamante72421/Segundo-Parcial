import os
os.system("cls")

'''
Docstring for 08-funciones
Las funciones en python son bloques de codigo reutilizables
que realizan una tarea especifica.
Sirven para organizar, reutilizar y hacer mas claro el codigo.

¿Para que sirven?

Evitan repetir codigo
Permiten dividir un problema grande en partes pequeñas
Hacen el programa mas facil de mantener
Mejora la legibilidad

#EN PYTHON SE DEFINEN CON LA PALABRA: def:

def nombre_funcion(parametros):
    #bloque de codigo
    return valor
'''

def nombre(): #funcion que no recibe ni regresa nada
    print("Hola mundo!!")
nombre()    

def suma():
    a=6
    print("Dentro de la funcion: ",a)
    b=7
    c = a + b
    return c

print("La suma es: ",suma())
a=3
print("Fuera de la funcion: ",a)
b=7
c = a + b

def multiplica(x,y):
    return x*y
print("La multiplicación es: ",multiplica(a,b))
