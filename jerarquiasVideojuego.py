class Personaje:
    def __init__(self,nombre,nivel):
        self.nombre=nombre
        self.nivel=nivel
    def atacar(self):
        print("ataquen!")

class Jugador(Personaje):
    def __init__(self,nombre,nivel,clase):
        super().__init__(nombre,nivel)
        self.clase=clase

    def habilidadEspecial(self):
        print("Usar transformacion")

class Enemigo(Personaje):
    def __init__(self,nombre,nivel,tipo):
        super().__init__(nombre,nivel)
        self.tipo=tipo
    def gritar(self):
        print("grito de guerra aaaaaaa")

def main():
   
    player=Jugador('el12',12,'Mago')
    player.atacar()
    player.habilidadEspecial()

    player1=Enemigo('ek23',4,'Essqueleto')
    player1.atacar()
    player1.gritar()
    
main()