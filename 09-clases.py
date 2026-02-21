'''
crear una clase con la palabra class

self se utiliza siempre para una clase (para poner una propiedad de ella)

solamente el self para definir objetos en una clase

'''

class Persona:
    def inicializar(self,nom):
        self.nombre=nom
    def imprimir(self):
        print("Nombre:",self.nombre)    



#bloque principal

persona1=Persona() #creando un objeto
persona1.inicializar("Pedro")
persona1.imprimir()

persona2=Persona() #creando un objeto
persona2.inicializar("Carla")
persona2.imprimir()

class operasBas:
    n1=0
    n2=0
    res=0
    def sumar(self,a,b):
        return a+b
    
    def pedirNumeros(self):
        self.n1=int(input("N1: "))
        self.n2=int(input("N2: "))
        print("La suma es: ",self.sumar(self.n1,self.n2))

obj=operasBas()
obj.pedirNumeros()