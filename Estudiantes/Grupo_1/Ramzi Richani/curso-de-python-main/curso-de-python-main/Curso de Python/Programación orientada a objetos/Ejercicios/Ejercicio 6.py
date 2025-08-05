import random

class Guerrero:
    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.vida_max = vida

    def atacar(self, objetivo):
        danio = max(0, self.ataque - objetivo.defensa + random.randint(-2, 2))
        print(f"{self.nombre} ataca a {objetivo.nombre} e intenta causar {danio} de daño.")
        objetivo.recibir_daño(danio)
        return danio

    def recibir_daño(self, valor):
        self.vida -= valor
        print(f"{self.nombre} recibe {valor} de daño. Vida actual: {self.vida}")

    def curarse(self):
        cantidad = random.randint(5, 15)
        self.vida = min(self.vida_max, self.vida + cantidad)
        print(f"{self.nombre} se cura {cantidad} puntos. Vida actual: {self.vida}")

    def mostrar_estado(self):
        print(f"{self.nombre} - Vida: {self.vida}/{self.vida_max}, Ataque: {self.ataque}, Defensa: {self.defensa}")

    def esta_vivo(self):
        return self.vida > 0

    def habilidad_especial(self, objetivo):
        pass

class Arquero(Guerrero):
    def __init__(self, nombre):
        super().__init__(nombre, vida=60, ataque=18, defensa=8)

    def habilidad_especial(self, objetivo):
        print(f"{self.nombre} usa Disparo Doble sobre {objetivo.nombre}!")
        for _ in range(2):
            self.atacar(objetivo)

class Espadachin(Guerrero):
    def __init__(self, nombre):
        super().__init__(nombre, vida=80, ataque=15, defensa=12)

    def habilidad_especial(self, objetivo):
        print(f"{self.nombre} usa Contraataque!")
        self.atacar(objetivo)
        self.defensa += 5
        print(f"{self.nombre} obtiene +5 defensa temporal.")
    
    def resetear_defensa(self):
        self.defensa = 12

class Mago(Guerrero):
    def __init__(self, nombre):
        super().__init__(nombre, vida=50, ataque=22, defensa=5)

    def habilidad_especial(self, objetivo):
        danio = random.randint(20, 30)
        print(f"{self.nombre} lanza Hechizo de Fuego sobre {objetivo.nombre} e ignora la defensa. Daño: {danio}")
        objetivo.recibir_daño(danio)

class Clan:
    def __init__(self, nombre, estrategia="aleatorio"):
        self.nombre = nombre
        self.lista_guerreros = []
        self.estrategia = estrategia

    def agregar_guerrero(self, guerrero):
        self.lista_guerreros.append(guerrero)
        print(f"{guerrero.nombre} ({guerrero.__class__.__name__}) se une al clan {self.nombre}.")

    def guerreros_vivos(self):
        return [g for g in self.lista_guerreros if g.esta_vivo()]

    def seleccionar_guerrero(self):
        vivos = self.guerreros_vivos()
        if not vivos:
            return None
        if self.estrategia == "aleatorio":
            return random.choice(vivos)
        elif self.estrategia == "fuerte":
            return max(vivos, key=lambda g: g.ataque)
        elif self.estrategia == "debil":
            return min(vivos, key=lambda g: g.vida)
        else:
            return random.choice(vivos)

    def atacar_clan(self, objetivo_clan):
        atacante = self.seleccionar_guerrero()
        objetivo = objetivo_clan.seleccionar_guerrero()
        if atacante and objetivo:
            accion = random.choice(["atacar", "curar", "especial"])
            if accion == "atacar":
                atacante.atacar(objetivo)
            elif accion == "curar":
                atacante.curarse()
            elif accion == "especial":
                atacante.habilidad_especial(objetivo)
            if isinstance(atacante, Espadachin):
                atacante.resetear_defensa()
        else:
            print("No hay guerreros disponibles para atacar.")

    def estado_clan(self):
        print(f"\nClan {self.nombre} - Estado de los guerreros:")
        for g in self.guerreros_vivos():
            g.mostrar_estado()
        print()

class Batalla:
    def __init__(self, clan1, clan2):
        self.clan1 = clan1
        self.clan2 = clan2
        self.turno_actual = 1

    def iniciar(self):
        print(f"Inicia la batalla entre {self.clan1.nombre} y {self.clan2.nombre}!")
        while not self.verificar_ganador():
            print(f"\n--- Turno {self.turno_actual} ---")
            if self.turno_actual % 2 == 1:
                self.clan1.atacar_clan(self.clan2)
            else:
                self.clan2.atacar_clan(self.clan1)
            self.clan1.estado_clan()
            self.clan2.estado_clan()
            self.turno_actual += 1

        ganador = self.verificar_ganador()
        if ganador:
            print(f"\n¡El clan {ganador.nombre} ha ganado la guerra!")

    def verificar_ganador(self):
        if not self.clan1.guerreros_vivos():
            return self.clan2
        elif not self.clan2.guerreros_vivos():
            return self.clan1
        else:
            return None

if __name__ == "__main__":
    clan_rojo = Clan("Rojos", estrategia="aleatorio")
    clan_azul = Clan("Azules", estrategia="fuerte")

    for i in range(2):
        clan_rojo.agregar_guerrero(Arquero(f"ArqueroRojo{i+1}"))
        clan_rojo.agregar_guerrero(Espadachin(f"EspadachinRojo{i+1}"))
        clan_rojo.agregar_guerrero(Mago(f"MagoRojo{i+1}"))

        clan_azul.agregar_guerrero(Arquero(f"ArqueroAzul{i+1}"))
        clan_azul.agregar_guerrero(Espadachin(f"EspadachinAzul{i+1}"))
        clan_azul.agregar_guerrero(Mago(f"MagoAzul{i+1}"))

    batalla = Batalla(clan_rojo, clan_azul)
    batalla.iniciar()