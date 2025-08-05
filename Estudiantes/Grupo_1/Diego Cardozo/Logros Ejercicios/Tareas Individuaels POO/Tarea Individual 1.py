import random

class Guerrero:
    def __init__(self, nombre, vida, ataque, defensa, tipo):
        self.__nombre = nombre
        self.__vida = vida
        self.__vida_maxima = vida
        self.__ataque = ataque
        self.__defensa = defensa
        self.__tipo = tipo
        self.__esta_vivo = True

    def get_nombre(self):
        return self.__nombre

    def get_vida(self):
        return self.__vida

    def get_ataque(self):
        return self.__ataque

    def get_defensa(self):
        return self.__defensa

    def get_tipo(self):
        return self.__tipo

    def esta_vivo(self):
        return self.__esta_vivo

    def atacar(self, objetivo):
        if not self.__esta_vivo:
            return

        print(f"{self.__nombre} ({self.__tipo}) ataca a {objetivo.get_nombre()} ({objetivo.get_tipo()})")
        daño_causado = self.__ataque - objetivo.get_defensa()
        if daño_causado < 0:
            daño_causado = 0

        objetivo.recibir_daño(daño_causado)
        return daño_causado

    def recibir_daño(self, valor):
        if not self.__esta_vivo:
            return

        self.__vida -= valor
        if self.__vida <= 0:
            self.__vida = 0
            self.__esta_vivo = False
            print(f"{self.__nombre} ha sido derrotado.")
        else:
            print(f"{self.__nombre} recibe {valor} de daño. Vida restante: {self.__vida}")

    def curarse(self):
        if not self.__esta_vivo:
            return

        valor_curacion = int(self.__vida_maxima * 0.2)
        vida_antes = self.__vida
        self.__vida += valor_curacion
        if self.__vida > self.__vida_maxima:
            self.__vida = self.__vida_maxima
        
        curacion_realizada = self.__vida - vida_antes
        if curacion_realizada > 0:
            print(f"{self.__nombre} se cura {curacion_realizada} puntos. Vida actual: {self.__vida}")

    def mostrar_estado(self):
        estado = "Vivo" if self.__esta_vivo else "Caido"
        print(f"  {self.__nombre} ({self.__tipo}): Vida={self.__vida}/{self.__vida_maxima}, Ataque={self.__ataque}, Defensa={self.__defensa}, Estado: {estado}")


class Mago(Guerrero):
    def __init__(self, nombre):
        super().__init__(nombre, vida=70, ataque=20, defensa=5, tipo="Mago")
        self.__mana = 50
        self.__mana_maximo = 50

    def get_mana(self):
        return self.__mana

    def atacar(self, objetivo):
        if not self.esta_vivo():
            print(f"{self.__nombre} esta caido y no puede atacar.")
            return

        daño_base = super().atacar(objetivo)
        return daño_base

    def lanzar_hechizo(self, objetivo):
        if not self.esta_vivo():
            print(f"{self.__nombre} esta caido y no puede lanzar hechizos.")
            return
        if self.__mana < 20:
            print(f"{self.__nombre} no tiene suficiente mana para lanzar un hechizo (Necesita 20, tiene {self.__mana}).")
            return 0
        
        costo_mana = 20
        daño_hechizo = self.get_ataque() * 1.8
        self.__mana -= costo_mana
        
        print(f"{self.get_nombre()} lanza un hechizo devastador a {objetivo.get_nombre()}!")
        objetivo.recibir_daño(daño_hechizo)
        print(f"Mana restante de {self.get_nombre()}: {self.__mana}")
        return daño_hechizo

    def recargar_mana(self):
        mana_antes = self.__mana
        self.__mana += 15
        if self.__mana > self.__mana_maximo:
            self.__mana = self.__mana_maximo
        print(f"{self.get_nombre()} recarga mana. Mana actual: {self.__mana}")



class Clan:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__lista_guerreros = []

    def get_nombre(self):
        return self.__nombre

    def get_guerreros_vivos(self):
        return [g for g in self.__lista_guerreros if g.esta_vivo()]

    def agregar_guerrero(self, guerrero):
        self.__lista_guerreros.append(guerrero)

    def seleccionar_guerrero(self):
        guerreros_vivos = self.get_guerreros_vivos()
        if not guerreros_vivos:
            return None
        return random.choice(guerreros_vivos)

    def seleccionar_objetivo(self, clan_enemigo):
        guerreros_enemigos_vivos = clan_enemigo.get_guerreros_vivos()
        if not guerreros_enemigos_vivos:
            return None
        return random.choice(guerreros_enemigos_vivos)

    def estado_clan(self):
        print(f"\n--- Estado del Clan {self.__nombre} ---")
        guerreros_vivos = self.get_guerreros_vivos()
        if guerreros_vivos:
            for guerrero in self.__lista_guerreros:
                guerrero.mostrar_estado()
        else:
            print(f"El clan {self.__nombre} no tiene guerreros en pie.")


class Batalla:
    def __init__(self, clan1, clan2):
        self.__clan1 = clan1
        self.__clan2 = clan2
        self.__turno_actual = 0
        print(f"La batalla comienza entre {clan1.get_nombre()} y {clan2.get_nombre()}!")

    def verificar_ganador(self):
        clan1_vivos = self.__clan1.get_guerreros_vivos()
        clan2_vivos = self.__clan2.get_guerreros_vivos()

        if not clan1_vivos and not clan2_vivos:
            return "Empate"
        elif not clan1_vivos:
            return self.__clan2.get_nombre()
        elif not clan2_vivos:
            return self.__clan1.get_nombre()
        else:
            return None

    def turno(self):
        self.__turno_actual += 1
        print(f"\n===== TURNO {self.__turno_actual} =====")

        clanes = [self.__clan1, self.__clan2]
        random.shuffle(clanes)

        for clan_atacante in clanes:
            clan_defensor = self.__clan2 if clan_atacante == self.__clan1 else self.__clan1

            atacante = clan_atacante.seleccionar_guerrero()
            objetivo = clan_atacante.seleccionar_objetivo(clan_defensor)

            if atacante and objetivo:
               
                if isinstance(atacante, Mago):
                    if atacante.get_mana() >= 20 and random.random() < 0.7: 
                        atacante.lanzar_hechizo(objetivo)
                    elif atacante.get_mana() < 20 and random.random() < 0.5: 
                        atacante.recargar_mana()
                    else:
                        atacante.atacar(objetivo)
                else: 
                    if atacante.get_vida() < atacante._Guerrero__vida_maxima * 0.3 and random.random() < 0.5:
                        atacante.curarse()
                    else:
                        atacante.atacar(objetivo)
            elif atacante:
                print(f"El clan {clan_defensor.get_nombre()} no tiene objetivos validos para {atacante.get_nombre()}.")
            
            ganador = self.verificar_ganador()
            if ganador:
                return ganador

        self.__clan1.estado_clan()
        self.__clan2.estado_clan()
        
        return None

    def iniciar(self):
        ganador = None
        while ganador is None:
            ganador = self.turno()
            if ganador is None:
                input("Presiona Enter para el siguiente turno...")

        print(f"\nBatalla Terminada!")
        if ganador == "Empate":
            print("La batalla ha terminado en empate! Ambos clanes fueron aniquilados.")
        else:
            print(f"El ganador es el clan {ganador}!")


if __name__ == "__main__":
    guerreros_clan_lobo = [
        Guerrero("Arthas", 100, 20, 10, "Guerrero"),
        Mago("Gandalf"), 
        Guerrero("Legolas", 80, 25, 8, "Guerrero"),
        Guerrero("Varian", 110, 22, 12, "Guerrero")
    ]

    guerreros_clan_dragon = [
        Guerrero("Grommash", 105, 21, 11, "Guerrero"),
        Mago("Jaina"), 
        Guerrero("Tyrande", 85, 23, 9, "Guerrero"),
        Guerrero("Thrall", 95, 19, 10, "Guerrero")
    ]

    clan_lobo = Clan("Colmillo de Lobo")
    for g in guerreros_clan_lobo:
        clan_lobo.agregar_guerrero(g)

    clan_dragon = Clan("Escamas de Dragon")
    for g in guerreros_clan_dragon:
        clan_dragon.agregar_guerrero(g)

    clan_lobo.estado_clan()
    clan_dragon.estado_clan()
    
    input("\nPresiona Enter para iniciar la batalla...")

    batalla_epica = Batalla(clan_lobo, clan_dragon)
    batalla_epica.iniciar()