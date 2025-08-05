class Pokemon:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.__nivel = 1
        self.__salud = 100

    def atacar(self, objetivo, dano):
        """
        Reduce la salud del objetivo, verificando que el atacante tenga salud
        y el daño sea positivo.
        """
        if self.__salud <= 0:
            print(f"🚫 {self.nombre} no puede atacar, su salud es 0.")
            return

        if dano <= 0:
            print(f"❌ El daño debe ser un valor positivo.")
            return

        print(f"⚔️ {self.nombre} ataca a {objetivo.nombre} con {dano} de daño.")
        objetivo.recibir_dano(dano)

    def recibir_dano(self, dano):
        """
        Resta salud al Pokémon, asegurando que no sea negativa.
        """
        if dano < 0:
            print(f"❌ El daño recibido no puede ser negativo.")
            return

        self.__salud -= dano
        if self.__salud < 0:
            self.__salud = 0
        print(f"🩹 {self.nombre} recibe {dano} de daño. Salud actual: {self.__salud}")
        if self.__salud == 0:
            print(f"💀 {self.nombre} ha sido debilitado.")

    def subir_nivel(self):
        """
        Aumenta el nivel del Pokémon en 1.
        """
        self.__nivel += 1
        print(f"⬆️ {self.nombre} subió a nivel {self.__nivel}!")

    def estado(self):
        """
        Muestra el nombre, tipo, nivel y salud actual del Pokémon.
        """
        print("\n--- Estado del Pokémon ---")
        print(f"Nombre: {self.nombre}")
        print(f"Tipo: {self.tipo}")
        print(f"Nivel: {self.__nivel}")
        print(f"Salud: {self.__salud}")
        print("--------------------------")

    # Método para acceder al nivel (útil para la subclase)
    def _get_nivel(self):
        return self.__nivel

    # Método para acceder a la salud (útil para la subclase o depuración)
    def _get_salud(self):
        return self.__salud


class PokemonLegendario(Pokemon):
    def __init__(self, nombre, tipo, habilidad_especial):
        super().__init__(nombre, tipo)
        self.__habilidad_especial = habilidad_especial

    def atacar(self, objetivo, dano):
        """
        Sobreescribe el método atacar para añadir +20 de daño adicional
        si el Pokémon está en nivel > 50.
        """
        dano_total = dano
        if self._get_nivel() > 50:
            dano_total += 20
            print(f"✨ ¡{self.nombre} usa su poder legendario y añade +20 de daño extra!")
        super().atacar(objetivo, dano_total)

    def usar_habilidad(self):
        """
        Muestra el nombre de la habilidad especial y un mensaje de efecto.
        """
        print(f"🤖✨ {self.nombre} usa su habilidad especial: '{self.__habilidad_especial}'!")
        print("¡Una energía mística inunda el área!")


# --- Ejemplo de Uso ---
if __name__ == "__main__":
    # Creamos algunos Pokémon
    pikachu = Pokemon("Pikachu", "Eléctrico")
    charmander = Pokemon("Charmander", "Fuego")

    print("--- Estado Inicial ---")
    pikachu.estado()
    charmander.estado()

    print("\n--- Simulación de Batalla ---")
    pikachu.atacar(charmander, 30)
    charmander.atacar(pikachu, 25)

    print("\n--- Subiendo de Nivel ---")
    pikachu.subir_nivel()
    pikachu.subir_nivel()
    pikachu.estado()

    print("\n--- Recibiendo Daño Grave ---")
    pikachu.recibir_dano(150) # Pikachu será debilitado
    pikachu.estado()
    pikachu.atacar(charmander, 10) # Intentar atacar con salud 0

    print("\n--- Probando Pokémon Legendario ---")
    mewtwo = PokemonLegendario("Mewtwo", "Psíquico", "Rayo Psíquico")
    mewtwo.estado()
    mewtwo.usar_habilidad()

    print("\n--- Subiendo de nivel a Mewtwo para activar habilidad extra ---")
    for _ in range(55):  # Sube 55 niveles para asegurar que el nivel sea > 50
        mewtwo.subir_nivel()
    mewtwo.estado()

    print("\n--- Ataque de Mewtwo Legendario con Bonificación ---")
    mewtwo.atacar(charmander, 40) # Ahora debería añadir +20 de daño
    charmander.estado()