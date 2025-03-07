import random

class Personaje:
    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa

    def atacar(self, enemigo):
        dano = max(0, self.ataque - enemigo.defensa + random.randint(-3, 3))
        enemigo.vida -= dano
        print(f"{self.nombre} ataca a {enemigo.nombre} causando {dano} de daño.")
        if enemigo.vida <= 0:
            print(f"{enemigo.nombre} ha sido derrotado.")

    def estado(self):
        return f"{self.nombre} - Vida: {self.vida}"

class Guerrero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida=40, ataque=10, defensa=8)

class Mago(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida=25, ataque=15, defensa=5)

jugador = Guerrero("Arthur")
enemigo = Mago("Morgana")

def combate(jugador, enemigo):
    print("¡Comienza la batalla!")
    print(jugador.estado())
    print(enemigo.estado())
    print("---")

    while jugador.vida > 0 and enemigo.vida > 0:
        jugador.atacar(enemigo)
        if enemigo.vida > 0:
            enemigo.atacar(jugador)
        print(jugador.estado())
        print(enemigo.estado())
        print("---")

    if jugador.vida > 0:
        print(f"{jugador.nombre} ha ganado la batalla!")
    else:
        print(f"{enemigo.nombre} ha ganado la batalla!")

combate(jugador, enemigo)
