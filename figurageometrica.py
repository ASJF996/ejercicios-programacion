import math
class FiguraGeometrica:
    def __init__(self,nombre):
        self.nombre=nombre
       
    def calculararea(self):
     return print('El area es')
    
class rectangulo(FiguraGeometrica):
    def __init__(self, nombre,lado):
        super().__init__(nombre)
        self.lado=lado

    def calculararea(self):
        return print(self.lado**2)

class circulo(FiguraGeometrica):
    def __init__(self, nombre,radio):
        super().__init__(nombre)
        self.radio=radio

    def calculararea(self):
        return print(math.pi*self.radio**2)

class triangulo(FiguraGeometrica):
    def __init__(self, nombre,base,altura):
        super().__init__(nombre)
        self.base=base
        self.altura=altura

    def calculararea(self):
        return print(self.base*self.altura/2)

def main():
    circ=circulo('circulo',1)
    circ.calculararea()
    rec=rectangulo('rectangulo',12)
    rec.calculararea()
    tr=triangulo('triangulo',5,2)
    tr.calculararea()
main()

