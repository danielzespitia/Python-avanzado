class Pokemon:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.__nivel = 1
        self.__salud = 100

    def atacar(self, objetivo, daño):
        if daño <= 0:
            print(f"{self.nombre} no puede atacar con daño no positivo.")
            return
        if self.__salud <= 0:
            print(f"{self.nombre} no puede atacar porque está debilitado.")
            return
        print(f"{self.nombre} ataca a {objetivo.nombre} causando {daño} de daño.")
        objetivo.recibir_daño(daño)

    def recibir_daño(self, daño):
        if daño < 0:
            print("El dañono puede ser negativo.")
            return
        else:
            self.__salud -= daño
        print(f"{self.nombre} recibe {daño} de daño. Salud actual: {self.__salud}")

    def subir_nivel(self):
        self.__nivel += 1
        print(f"{self.nombre} sube a nivel {self.__nivel}.")

    def estado(self):
        print(f"Nombre: {self.nombre}")
        print(f"Tipo: {self.tipo}")
        print(f"Nivel: {self.__nivel}")
        print(f"Salud: {self.__salud}")

    @property
    def nivel(self):
        return self.__nivel

    @property
    def salud(self):
        return self.__salud

class PokemonLegendario(Pokemon):
    def __init__(self, nombre, tipo, habilidad_especial):
        super().__init__(nombre, tipo)
        self.__habilidad_especial = habilidad_especial

    def atacar(self, objetivo, dano):
        dano_extra = 0
        if self.nivel > 50:
            dano_extra = 20
            print(f"{self.nombre} usa su poder legendario! (+20 daño adicional)")
        super().atacar(objetivo, dano + dano_extra)

    def usar_habilidad(self):
        print(f"{self.nombre} usa su habilidad especial: {self.__habilidad_especial}!")
        print(f"¡Un efecto increíble ocurre en el campo de batalla!")

# Ejemplo de uso:
if __name__ == "__main__":
    Ceruledge = Pokemon("Ceruledge", "Fantasma/Fuego")
    Necrozma = PokemonLegendario("Necrozma", "Psíquico", "Géiser Fotónico")

    Ceruledge.estado()
    Necrozma.estado()

    print("\nTurno de ataque:")
    Ceruledge.atacar(Necrozma, 25)
    Necrozma.atacar(Ceruledge, 40)

    print("\nSubimos de nivel a Necrozma (hasta 51):")
    for _ in range(51 - Necrozma.nivel):
        Necrozma.subir_nivel()

    Necrozma.estado()
    print("\nAtaque legendario:")
    Necrozma.atacar(Ceruledge, 30)

    print("\nUso de habilidad especial:")
    Necrozma.usar_habilidad()
