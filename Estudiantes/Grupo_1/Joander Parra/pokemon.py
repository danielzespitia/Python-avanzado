class Pokemon:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.__nivel = 1
        self.__salud = 100

    def atacar(self, objetivo, dano):
        if self.__salud <= 0:
            print(f"{self.nombre} no puede atacar porque está debilitado.")
            return
        if dano <= 0:
            print("El daño debe ser positivo.")
            return
        print(f"{self.nombre} ataca a {objetivo.nombre} causando {dano} de daño.")
        objetivo.recibir_dano(dano)

    def recibir_dano(self, dano):
        if dano < 0:
            print("El daño no puede ser negativo.")
            return
        self.__salud -= dano
        if self.__salud < 0:
            self.__salud = 0
        print(f"{self.nombre} ha recibido {dano} de daño. Salud actual: {self.__salud}")

    def subir_nivel(self):
        self.__nivel += 1
        print(f"{self.nombre} ha subido al nivel {self.__nivel}.")

    def estado(self):
        print(f"Nombre: {self.nombre}")
        print(f"Tipo: {self.tipo}")
        print(f"Nivel: {self.__nivel}")
        print(f"Salud: {self.__salud}")

class PokemonLegendario(Pokemon):
    def __init__(self, nombre, tipo, habilidad_especial):
        super().__init__(nombre, tipo)
        self.__habilidad_especial = habilidad_especial

    def atacar(self, objetivo, dano):
        nivel = getattr(self, "_Pokemon__nivel")
        dano_total = dano
        if nivel > 50:
            dano_total += 20
            print(f"{self.nombre} usa su poder legendario (+20 daño)!")
        super().atacar(objetivo, dano_total)

    def usar_habilidad(self):
        print(f"{self.nombre} usa su habilidad especial: {self.__habilidad_especial} !")

if __name__ == "__main__":
    pikachu = Pokemon("Pikachu", "Eléctrico")
    charizard = PokemonLegendario("Charizard", "Fuego", "Llama Eterna")

    pikachu.estado()
    charizard.estado()
    pikachu.atacar(charizard, 30)
    charizard.subir_nivel()
    for _ in range(50):
        charizard.subir_nivel()
    charizard.atacar(pikachu, 40)
    charizard.usar_habilidad()
    pikachu.estado()