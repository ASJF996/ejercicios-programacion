class Paleta:
    def __init__(self, sabor, precio):
        self.sabor = sabor
        self.precio = precio

    def mostrar_informacion(self):
        print(f"La paleta de {self.sabor} cuesta: ${self.precio}")

class PaletaAgua(Paleta):
    def __init__(self, sabor, precio, base_agua: bool):
        super().__init__(sabor, precio)
        self.base_agua = base_agua

    def mostrar_base_agua(self):
        if self.base_agua:
            print("La paleta tiene base de agua.")
        else:
            print("La paleta no tiene base de agua.")

class PaletaCrema(Paleta):
    def __init__(self, sabor, precio, cremosa: bool):
        super().__init__(sabor, precio)
        self.cremosa = cremosa

    def mostrar_textura_cremosa(self):
        if self.cremosa:
            print("La paleta es cremosa.")
        else:
            print("La paleta no es cremosa.")

def main():
    p1 = PaletaAgua('mango', 4, True)
    p1.mostrar_informacion()
    p1.mostrar_base_agua()

    print("---")

    p2 = PaletaCrema('Nuez', 8, False)
    p2.mostrar_informacion()
    p2.mostrar_textura_cremosa()

if __name__ == "__main__":
    main()