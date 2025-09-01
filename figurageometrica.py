import math

class FiguraGeometrica:
    def __init__(self, nombre):
        self.nombre = nombre

    def calculararea(self):
        return 0  

class Rectangulo(FiguraGeometrica):
    def __init__(self, nombre, lado):
        super().__init__(nombre)
        self.lado = lado

    def calculararea(self):
        return self.lado ** 2

class Circulo(FiguraGeometrica):
    def __init__(self, nombre, radio):
        super().__init__(nombre)
        self.radio = radio

    def calculararea(self):
        return math.pi * self.radio ** 2

class Triangulo(FiguraGeometrica):
    def __init__(self, nombre, base, altura):
        super().__init__(nombre)
        self.base = base
        self.altura = altura

    def calculararea(self):
        return (self.base * self.altura) / 2

def tabla():
    print("_" * 50)

def main():
    n = int(input("Ingresa la cantidad de figuras geométricas que necesitas crear: "))
    listafiguras = []

    print("\nLas figuras que puedes agregar son: circulo, rectangulo y triangulo\n")

    for i in range(n):
        tipo = input(f"Figura #{i+1} - Ingresa el tipo de figura: ").lower()

        if tipo == "circulo":
            radio = float(input("Ingresa el radio del círculo: "))
            figura = Circulo("Círculo", radio)

        elif tipo == "rectangulo":
            lado = float(input("Ingresa el lado del rectángulo: "))
            figura = Rectangulo("Rectángulo", lado)

        elif tipo == "triangulo":
            base = float(input("Ingresa la base del triángulo: "))
            altura = float(input("Ingresa la altura del triángulo: "))
            figura = Triangulo("Triángulo", base, altura)

        else:
            print("Tipo de figura no válido. Intenta nuevamente.")
            continue

        listafiguras.append(figura)

    tabla()
    print("Tabla de Figuras Geométricas y sus Áreas")
    tabla()

    for figura in listafiguras:
        print(f"Figura: {figura.nombre}")
        print(f"Área: {figura.calculararea():.2f}")
        tabla()

main()