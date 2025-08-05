# Clase base para representar un Pokémon
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
            print("Error: El daño debe ser positivo.")
            return
        objetivo.recibir_dano(dano)
        print(f"{self.nombre} atacó a {objetivo.nombre} causando {dano} de daño.")

    def recibir_dano(self, dano):
        if dano < 0:
            print("Error: El daño no puede ser negativo.")
            return
        self.__salud -= dano
        if self.__salud < 0:
            self.__salud = 0  # No puede tener salud negativa

    def subir_nivel(self):
        self.__nivel += 1

    def estado(self):
        print(f"\nEstado de {self.nombre}")
        print(f"Tipo: {self.tipo}")
        print(f"Nivel: {self.__nivel}")
        print(f"Salud: {self.__salud}")

    # Métodos para obtener información desde fuera
    def obtener_salud(self):
        return self.__salud

    def obtener_nivel(self):
        return self.__nivel


# Subclase para Pokémon Legendarios
class PokemonLegendario(Pokemon):
    def __init__(self, nombre, tipo, habilidad_especial):
        super().__init__(nombre, tipo)
        self.__habilidad_especial = habilidad_especial

    def atacar(self, objetivo, dano):
        if self.obtener_salud() <= 0:
            print(f"{self.nombre} no puede atacar porque está debilitado.")
            return
        if dano <= 0:
            print("Error: El daño debe ser positivo.")
            return

        if self.obtener_nivel() > 50:
            dano += 20
            print(f"{self.nombre} usó su poder legendario. Daño aumentado +20.")

        objetivo.recibir_dano(dano)
        print(f"{self.nombre} lanzó un ataque poderoso a {objetivo.nombre} causando {dano} de daño.")

    def usar_habilidad(self):
        print(f"{self.nombre} activó su habilidad especial: {self.__habilidad_especial}")
        print("El campo de batalla se altera con una energía extraña.")


# Simulación de combate con narrativa sencilla
print("🌌 En un bosque misterioso, un pequeño Pokémon se prepara para luchar...")

# Crear Pokémon
bulbasaur = Pokemon("Bulbasaur", "🌿 Planta")
mewtwo = PokemonLegendario("Mewtwo", "🧠 Psíquico", "Pulso Mental")

print("\n🌿 Bulbasaur aparece entre la hierba, listo para proteger su territorio.")
print("🧠 Mewtwo llega volando, su presencia impone respeto.")

print("\nEstado inicial:")
bulbasaur.estado()
mewtwo.estado()

print("\nBulbasaur ataca primero.")
bulbasaur.atacar(mewtwo, 25)

print("\nMewtwo comienza a subir de nivel...")
for _ in range(50):
    mewtwo.subir_nivel()

print("\nMewtwo ha alcanzado un nivel impresionante.")
mewtwo.estado()

print("\nAhora Mewtwo ataca con fuerza aumentada.")
mewtwo.atacar(bulbasaur, 35)

print("\nMewtwo también usa su habilidad especial.")
mewtwo.usar_habilidad()

print("\nEstado final del combate:")
bulbasaur.estado()
mewtwo.estado()

print("\nFin del combate. Aunque Bulbasaur luchó con valentía, Mewtwo demostró su poder legendario.")
