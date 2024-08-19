class Pokemon:
    nombre = None
    tipo = None
    vida = None
    evolucion = None
    ataque = None

    def __init__(self, n, t, v, e):
        self.nombre = n
        self.tipo = t
        self.vida = v
        self.evolucion = e # 1 o 2 o 3
        self.ataque = []
    def setataque(self, ataque):
        self.ataque.append(ataque)
    def atacar(self, i):
        print(f"{self.nombre} ataco con {self.ataque[i]}")
    def defenderse(self):
        print(f"{self.nombre} se deefendio")
    

if __name__ == "__main__":
    picachu = Pokemon(n = "Pikachu", t = "electrico", v = 200, e = 2)
    charizar = Pokemon(n = "Charizar", t = "fuego", v = 300, e = 3 )
    picachu.setataque("impactrueno")
    picachu.setataque("rafaga")
    picachu.setataque("arañazo")

    print(picachu.atacar(0))
    print(charizar.defenderse())
