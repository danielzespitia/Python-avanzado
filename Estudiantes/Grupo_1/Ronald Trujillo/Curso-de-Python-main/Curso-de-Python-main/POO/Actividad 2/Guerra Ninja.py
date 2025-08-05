import random


# Clase base Ninja
class Ninja:
    def __init__(self, nombre, vida, ataque, defensa, clan):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.clan = clan

    def esta_vivo(self):
        return self.vida > 0

    def atacar(self, objetivo):
        danio = max(0, self.ataque - objetivo.defensa)
        print(f"{self.nombre} ({self.clan}) ataca a {objetivo.nombre} y causa {danio} de daño.")
        objetivo.recibir_daño(danio)

    def recibir_daño(self, valor):
        self.vida -= valor
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nombre} ahora tiene {self.vida} de vida.")

    def curarse(self):
        curacion = random.randint(10, 20)
        self.vida += curacion
        print(f"{self.nombre} se cura {curacion} puntos de vida. Vida actual: {self.vida}")

    def mostrar_estado(self):
        print(f"{self.nombre} ({self.clan}) - Vida: {self.vida}")

# Subclase Uchiha
class Uchiha(Ninja):
    def __init__(self, nombre):
        super().__init__(nombre, vida=75, ataque=30, defensa=8, clan="Uchiha")

    def sharingan(self, objetivo):
        danio = 45
        print(f"{self.nombre} activa el Sharingan y causa {danio} de daño a {objetivo.nombre}.")
        objetivo.recibir_daño(danio)

# Subclase Hyuga
class Hyuga(Ninja):
    def __init__(self, nombre):
        super().__init__(nombre, vida=80, ataque=25, defensa=12, clan="Hyuga")

    def byakugan(self, objetivo):
        danio = 35
        print(f"{self.nombre} usa Byakugan y golpea puntos de chakra de {objetivo.nombre}, causando {danio} de daño.")
        objetivo.recibir_daño(danio)

# Clase Clan
class Clan:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ninjas = []

    def agregar_ninja(self, ninja):
        self.ninjas.append(ninja)

    def seleccionar_ninja(self):
        vivos = [n for n in self.ninjas if n.esta_vivo()]
        return random.choice(vivos) if vivos else None

    def tiene_ninjas_vivos(self):
        return any(n.esta_vivo() for n in self.ninjas)

    def estado_clan(self):
        print(f"\nEstado del {self.nombre}:")
        for ninja in self.ninjas:
            ninja.mostrar_estado()

# Clase Batalla
class Batalla:
    def __init__(self, clan1, clan2):
        self.clan1 = clan1
        self.clan2 = clan2
        self.turno_actual = 0

    def iniciar(self):
        print(f"\nComienza la batalla entre el {self.clan1.nombre} y el {self.clan2.nombre}.\n")
        while self.clan1.tiene_ninjas_vivos() and self.clan2.tiene_ninjas_vivos():
            self.turno()
        self.verificar_ganador()

    def turno(self):
        atacante_clan = self.clan1 if self.turno_actual % 2 == 0 else self.clan2
        defensor_clan = self.clan2 if self.turno_actual % 2 == 0 else self.clan1

        atacante = atacante_clan.seleccionar_ninja()
        defensor = defensor_clan.seleccionar_ninja()

        if not atacante or not defensor:
            return

        accion = random.random()

        if isinstance(atacante, Uchiha) and accion < 0.3:
            atacante.sharingan(defensor)
        elif isinstance(atacante, Hyuga) and accion < 0.3:
            atacante.byakugan(defensor)
        else:
            if accion < 0.2:
                atacante.curarse()
            else:
                atacante.atacar(defensor)

        self.turno_actual += 1

    def verificar_ganador(self):
        if self.clan1.tiene_ninjas_vivos():
            print(f"\nEl {self.clan1.nombre} ha ganado la batalla.")
        elif self.clan2.tiene_ninjas_vivos():
            print(f"\nEl {self.clan2.nombre} ha ganado la batalla.")
        else:
            print("\nEmpate. Ambos clanes han sido derrotados.")

# Ejecución del combate
if __name__ == "__main__":
    # Crear clanes
    clan_uchiha = Clan("Clan Uchiha")
    clan_hyuga = Clan("Clan Hyuga")

    # Agregar ninjas al Clan Uchiha
    clan_uchiha.agregar_ninja(Uchiha("Sasuke"))
    clan_uchiha.agregar_ninja(Uchiha("Itachi"))
    clan_uchiha.agregar_ninja(Uchiha("Shisui"))

    # Agregar ninjas al Clan Hyuga
    clan_hyuga.agregar_ninja(Hyuga("Neji"))
    clan_hyuga.agregar_ninja(Hyuga("Hinata"))
    clan_hyuga.agregar_ninja(Hyuga("Hiashi"))

    # Estado inicial
    clan_uchiha.estado_clan()
    clan_hyuga.estado_clan()

    # Iniciar batalla
    batalla = Batalla(clan_uchiha, clan_hyuga)
    batalla.iniciar()

    # Estado final
    clan_uchiha.estado_clan()
    clan_hyuga.estado_clan()
