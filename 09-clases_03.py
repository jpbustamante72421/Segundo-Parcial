import os,math
os.system("cls")
class areas:
    def init(self):
        self.res = 0

    def cuadrado(self):
        lado = float(input("Lado: "))
        self.res = lado * lado
        return self.res

    def rectangulo(self):
        base = float(input("Base: "))
        altura = float(input("Altura: "))
        self.res = base * altura
        return self.res

    def triangulo(self):
        base = float(input("Base: "))
        altura = float(input("Altura: "))
        self.res = (base * altura) / 2
        return self.res

    def circulo(self):
        radio = float(input("Radio: "))
        self.res = math.pi * (radio ** 2)
        return self.res

    def trapecio(self):
        B = float(input("Base mayor: "))
        b = float(input("Base menor: "))
        h = float(input("Altura: "))
        self.res = ((B + b) * h) / 2
        return self.res
    
    def imprimir(self):
        print("El área es:", self.res)
def main():
    obj=areas()
    op=0
    while op != 6:
        os.system("cls")
        print("1 Cuadrado")
        print("2 Reactangulo")
        print("3 Triangulo")
        print("4 Circulo")
        print("5 Trapecio")
        print("6 Salir")
        op = int(input("Opción: "))
        if op == 1:
            obj.cuadrado()
            obj.imprimir()
            input()
        if op == 2:
            obj.rectangulo()
            obj.imprimir()
            input()
        if op == 3:
            obj.triangulo()
            obj.imprimir()
            input()
        if op == 4:
            obj.circulo()
            obj.imprimir()
            input()

        if op == 5:
            obj.trapecio()
            obj.imprimir()
            input()

if __name__ == "__main__":
    main()