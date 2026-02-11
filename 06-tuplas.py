tupla=(1,2,3,4,5,2,3,2)

print(type(tupla))#el tipo de dato que es tupla
print(tupla)#imprime todo el contenido de la tupla
print("El elemento de la tupla es: ",tupla[2]) #nos dará la posicion deseada de la tupla

for i in tupla:   # nos dara el valor uno por uno de la tupla
    print(i)

print("La cantidadd de elementos de la tupla es esta: ",len(tupla))
print("La cantidadd de veces que se repite el numero 2: ",tupla.count(2))
print("El índice del numero 3 es: ",tupla.index(3))

#la tupla es un valor inmutable y no se puede modificar ni agregar nigun dato