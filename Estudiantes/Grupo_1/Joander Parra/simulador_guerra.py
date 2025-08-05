import random

class Guerrero:
    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa

    def atacar(self, objetivo):
        daño = max(0, self.ataque - objetivo.defensa)
        print(f"{self.nombre} ataca a {objetivo.nombre} causando {daño} de daño.")
        objetivo.recibir_daño(daño)

    def recibir_daño(self, valor):
        self.vida -= valor
        print(f"{self.nombre} recibe {valor} de daño. Vida restante: {self.vida}")

    def curarse(self):
        curacion = random.randint(5, 15)
        self.vida += curacion
        print(f"{self.nombre} se cura {curacion} puntos. Vida actual: {self.vida}")

    def mostrar_estado(self):
        print(f"{self.nombre} | Vida: {self.vida} | Ataque: {self.ataque} | Defensa: {self.defensa}")

    def esta_vivo(self):
        return self.vida > 0

class Arquero(Guerrero):
    def __init__(self, nombre):
        super().__init__(nombre, vida=60, ataque=18, defensa=8)

class Espadachin(Guerrero):
    def __init__(self, nombre):
        super().__init__(nombre, vida=80, ataque=15, defensa=12)

class Mago(Guerrero):
    def __init__(self, nombre):
        super().__init__(nombre, vida=50, ataque=22, defensa=6)

    def curarse(self):
        curacion = random.randint(10, 25)
        self.vida += curacion
        print(f"{self.nombre} (Mago) se cura {curacion} puntos. Vida actual: {self.vida}")

class Clan:
    def __init__(self, nombre, estrategia="aleatoria"):
        self.nombre = nombre
        self.lista_guerreros = []
        self.estrategia = estrategia

    def agregar_guerrero(self, guerrero):
        self.lista_guerreros.append(guerrero)

    def seleccionar_guerrero(self):
        vivos = [g for g in self.lista_guerreros if g.esta_vivo()]
        if vivos:
            return random.choice(vivos)
        return None

    def estado_clan(self):
        print(f"\nEstado del clan {self.nombre}:")
        for g in self.lista_guerreros:
            g.mostrar_estado()

    def tiene_guerreros_vivos(self):
        return any(g.esta_vivo() for g in self.lista_guerreros)

class Batalla:
    def __init__(self, clan1, clan2, max_turnos=50):
        self.clan1 = clan1
        self.clan2 = clan2
        self.max_turnos = max_turnos

    def iniciar(self):
        turno = 1
        print("¡Comienza la batalla!")
        while (self.clan1.tiene_guerreros_vivos() and self.clan2.tiene_guerreros_vivos()
               and turno <= self.max_turnos):
            print(f"\n--- Turno {turno} ---")
            self.turno(self.clan1, self.clan2)
            if not self.clan2.tiene_guerreros_vivos():
                break
            self.turno(self.clan2, self.clan1)
            turno += 1
        if turno > self.max_turnos:
            print("\n¡Empate por límite de turnos!")
        self.verificar_ganador()

    def turno(self, clan_atacante, clan_defensor):
        atacante = clan_atacante.seleccionar_guerrero()
        defensor = clan_defensor.seleccionar_guerrero()
        if atacante and defensor:
            accion = random.choice(["atacar", "curarse"])
            if accion == "atacar":
                atacante.atacar(defensor)
            else:
                atacante.curarse()
        clan_atacante.estado_clan()
        clan_defensor.estado_clan()

    def verificar_ganador(self):
        if self.clan1.tiene_guerreros_vivos():
            print(f"\n¡El clan ganador es {self.clan1.nombre}!")
        elif self.clan2.tiene_guerreros_vivos():
            print(f"\n¡El clan ganador es {self.clan2.nombre}!")
        else:
            print("\n¡Empate! Ambos clanes han caído.")

if __name__ == "__main__":
    clanA = Clan("Dragones")
    clanA.agregar_guerrero(Arquero("Robin"))
    clanA.agregar_guerrero(Espadachin("Arthur"))
    clanA.agregar_guerrero(Mago("Merlin"))

    clanB = Clan("Lobos")
    clanB.agregar_guerrero(Arquero("Legolas"))
    clanB.agregar_guerrero(Espadachin("Conan"))
    clanB.agregar_guerrero(Mago("Gandalf"))

    batalla = Batalla(clanA, clanB, max_turnos=10)
    batalla.iniciar()

