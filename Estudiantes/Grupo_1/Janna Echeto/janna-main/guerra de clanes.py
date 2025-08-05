import random

class Guerrero:
    def __init__(self, nombre, vida, ataque, defensa, tipo):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.tipo = tipo

    def atacar(self, objetivo):
        
        dano = max(0, self.ataque - objetivo.defensa)
        objetivo.recibir_dano(dano)
        print(f"{self.nombre} ({self.tipo}) ataca a {objetivo.nombre} y causa {dano} de daño.")

    def recibir_dano(self, valor):
        self.vida -= valor
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nombre} recibe {valor} de daño. Vida restante: {self.vida}")

    def curarse(self):
       
        cantidad_curacion = random.randint(10, 25)
        self.vida += cantidad_curacion
        print(f"{self.nombre} se cura {cantidad_curacion} puntos de vida. Vida actual: {self.vida}")

    def mostrar_estado(self):
        return f"{self.nombre} ({self.tipo}) - Vida: {self.vida}, Ataque: {self.ataque}, Defensa: {self.defensa}"


class Arquero(Guerrero):
    def __init__(self, nombre, vida, ataque, defensa):
        super().__init__(nombre, vida, ataque, defensa, "Arquero")

class Espadachin(Guerrero):
    def __init__(self, nombre, vida, ataque, defensa):
        super().__init__(nombre, vida, ataque, defensa, "Espadachin")

class Mago(Guerrero):
    def __init__(self, nombre, vida, ataque, defensa):
        super().__init__(nombre, vida, ataque, defensa, "Mago")
    
    def atacar(self, objetivo):
        
        dano = self.ataque
        objetivo.recibir_dano(dano)
        print(f"{self.nombre} ({self.tipo}) lanza un hechizo a {objetivo.nombre} y causa {dano} de daño (ignora defensa).")


class Clan:
    def __init__(self, nombre, estrategia):
        self.nombre = nombre
        self.guerreros = []
        self.estrategia = estrategia 

    def agregar_guerrero(self, guerrero):
        self.guerreros.append(guerrero)
        print(f"{guerrero.nombre} se ha unido al clan {self.nombre}.")

    def seleccionar_guerrero(self):
        
        if self.guerreros:
            return random.choice(self.guerreros)
        return None

    def atacar_clan(self, objetivo_clan):
        guerrero_atacante = self.seleccionar_guerrero()
        guerrero_defensor = objetivo_clan.seleccionar_guerrero()
        
        if guerrero_atacante and guerrero_defensor:
            guerrero_atacante.atacar(guerrero_defensor)
            
            if guerrero_defensor.vida <= 0:
                objetivo_clan.guerreros.remove(guerrero_defensor)
                print(f"¡{guerrero_defensor.nombre} ha sido derrotado!")

    def estado_clan(self):
        print(f"\n--- Estado del Clan {self.nombre} ---")
        if not self.guerreros:
            print("El clan no tiene guerreros. ¡Ha sido derrotado!")
        else:
            for guerrero in self.guerreros:
                print(guerrero.mostrar_estado())


class Batalla:
    def __init__(self, clan1, clan2):
        self.clan1 = clan1
        self.clan2 = clan2
        self.turno_actual = 1

    def iniciar(self):
        print("¡La batalla ha comenzado!")
        while self.clan1.guerreros and self.clan2.guerreros:
            self.turno()
            if not self.clan1.guerreros or not self.clan2.guerreros:
                break
            input("\nPresiona Enter para el siguiente turno...")
        self.verificar_ganador()

    def turno(self):
        print(f"\n===== Turno {self.turno_actual} =====")
        
        if random.choice([True, False]):
            self.clan1.atacar_clan(self.clan2)
            if self.clan2.guerreros: 
                self.clan2.atacar_clan(self.clan1)
        else:
            self.clan2.atacar_clan(self.clan1)
            if self.clan1.guerreros:
                self.clan1.atacar_clan(self.clan2)
        
        self.turno_actual += 1

    def verificar_ganador(self):
        print("\n--- Fin de la Batalla ---")
        if self.clan1.guerreros and not self.clan2.guerreros:
            print(f"¡El Clan {self.clan1.nombre} ha ganado la guerra!")
        elif self.clan2.guerreros and not self.clan1.guerreros:
            print(f"¡El Clan {self.clan2.nombre} ha ganado la guerra!")
        else:
            print("La batalla ha terminado en empate.") 

if __name__ == "__main__":
    clan_fuego = Clan("Clan del Fuego", "ofensiva")
    clan_hielo = Clan("Clan del Hielo", "defensiva")

    clan_fuego.agregar_guerrero(Espadachin("Kael", 100, 20, 15))
    clan_fuego.agregar_guerrero(Mago("Lyra", 80, 25, 10))
    clan_fuego.agregar_guerrero(Arquero("Talon", 70, 18, 12))

    clan_hielo.agregar_guerrero(Espadachin("Borin", 110, 18, 18))
    clan_hielo.agregar_guerrero(Arquero("Elara", 75, 20, 10))
    clan_hielo.agregar_guerrero(Mago("Zane", 85, 22, 8))

    batalla = Batalla(clan_fuego, clan_hielo)
    batalla.iniciar()
