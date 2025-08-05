class Pokemon:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self._nivel = 1       

    def atacar(self, objetivo_pokemon, cantidad_daño):
        if not isinstance(objetivo_pokemon, Pokemon):
            print(f"{self.nombre} no puede atacar a un objetivo que no es un Pokémon.")
            return

        print(f"\n¡{self.nombre} ataca a {objetivo_pokemon.nombre}!")
        objetivo_pokemon.recibir_daño(cantidad_daño)
        
    def recibir_daño(self, daño):
        if daño <= 0:
            print(f"{self.nombre} no recibió daño.")
            return

        print(f"{self.nombre} recibe {daño} puntos de daño.")
        self._salud -= daño

        if self._salud <= 0:
            self._salud = 0
            print(f"¡{self.nombre} se ha debilitado!")
        else:
            print(f"A {self.nombre} le quedan {self._salud} puntos de salud.")


    def subir_nivel(self):
        self._nivel += 1
        print(f"¡{self.nombre} ha subido al nivel {self._nivel}!")

    def estado(self):
        return f"Nombre: {self.nombre} / Tipo: {self.tipo} / Nivel: {self._nivel} / Salud: {self._salud}"

   

    def salud(self, nueva_salud):
        if nueva_salud >= 0:
            self._salud = nueva_salud
        else:
            self._salud = 0
            
class PokemonLegendario(Pokemon):
    def __init__(self, nombre, tipo, habilidad_especial):
        super().__init__(nombre, tipo) 
        self.__habilidad_especial = habilidad_especial 
        self._salud = 150 
        self._nivel = 50 


    def atacar(self, objetivo_pokemon, cantidad_daño_base):
        print(f"\n¡{self.nombre} (Legendario) desata un ataque!")
        
        daño_final = cantidad_daño_base

        if self._nivel > 50:
            daño_adicional = 20
            daño_final += daño_adicional
            print(f"Debido a su alto nivel ({self._nivel}), {self.nombre} inflige +{daño_adicional} de daño adicional")

        super().atacar(objetivo_pokemon, daño_final)


    def usar_habilidad(self):
        print(f"\n¡{self.nombre} usa su habilidad especial: {self.__habilidad_especial}!")
        print("¡TODO SU PODER envuelve el campo de batalla! ") 


pikachu = Pokemon("Pikachu", "Eléctrico")
charmander = Pokemon("Charmander", "Fuego")
squirtle = Pokemon("Squirtle", "Agua")

print(pikachu.estado())
print(charmander.estado())
print(squirtle.estado())

pikachu.atacar(charmander, 20)
print(charmander.estado())

charmander.atacar(squirtle, 15)
print(squirtle.estado())


squirtle.recibir_daño(5)
print(squirtle.estado())


pikachu.subir_nivel()
print(pikachu.estado())


