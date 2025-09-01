class Paleta:
    def __init__(self, sabor, precio):
        self.sabor = sabor
        self.precio = precio

    def mostrar_informacion(self):
        print(f"La paleta de {self.sabor} cuesta: ${self.precio}")

    def mostrar_detalle(self):
        print("Esta paleta no tiene detalles adicionales.")

class PaletaAgua(Paleta):
    def __init__(self, sabor, precio, base_agua: bool):
        super().__init__(sabor, precio)
        self.base_agua = base_agua

    def mostrar_detalle(self):
        if self.base_agua:
            print("La paleta tiene base de agua.")
        else:
            print("La paleta no tiene base de agua.")

class PaletaCrema(Paleta):
    def __init__(self, sabor, precio, cremosa: bool):
        super().__init__(sabor, precio)
        self.cremosa = cremosa

    def mostrar_detalle(self):
        if self.cremosa:
            print("La paleta es cremosa.")
        else:
            print("La paleta no es cremosa.")

def main():
    paletas = [
        PaletaAgua('Mango', 4, True),
        PaletaCrema('Nuez', 8, False)
    ]

    for paleta in paletas:
        paleta.mostrar_informacion()
        paleta.mostrar_detalle()
        print("---")

if __name__ == "__main__":
    main()