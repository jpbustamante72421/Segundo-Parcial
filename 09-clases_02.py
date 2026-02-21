import os

class operasBas:
    n1=0
    n2=0
    res=0
    def sumar(self):
        self.res=self.n1+self.n2
        return self.res
    
    def restar(self):
        self.res=self.n1-self.n2
        return self.res
    
    def multiplicar(self):
        self.res=self.n1*self.n2
        return self.res
    
    def dividir(self):
        self.res=self.n1/self.n2
        return self.res
    
    def pedirNumeros(self):
        self.n1=int(input("N1: "))
        self.n2=int(input("N2: "))
        #print("La suma es: ",self.sumar(self.n1,self.n2))

    def imprimir(self):
        print("El resultado será: ",self.res)    

def main():
    obj=operasBas()
    print("La suma es: ", obj.sumar())
    op=0
    while op!=5:
        os.system("cls")
        print("1.- +\n 2.- -\n 3.- *\n 4.- /\n 5.- Salir\n")
        op=int(input("Opción: "))
        if op==1:
            obj.pedirNumeros()
            obj.sumar()
            obj.imprimir()
            input()
        if op==2:
            obj.pedirNumeros() 
            obj.restar()   
            obj.imprimir()
if __name__=="__main__":
    main()