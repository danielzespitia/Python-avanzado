class Pokemon:
    def __init__(self, nombre, tipo):
        self.nombre = nombre  
        self.tipo = tipo      
        self.__nivel = 1      
        self.__salud = 100    

    def atacar(self, objetivo, dano):
        if dano > 0 and self.__salud > 0:
            print(f"{self.nombre} ataca a {objetivo.nombre} causando {dano} de daño.")
            objetivo.recibir_dano(dano)
        else:
            print(" Ataque fallido: daño inválido o salud insuficiente.")

    def recibir_dano(self, dano):
        if dano > 0:
            if dano >= self.__salud:
                self.__salud = 0
            else:
                self.__salud -= dano
            print(f"{self.nombre} recibió {dano} de daño. Salud restante: {self.__salud}")
        else:
            print(" El daño debe ser positivo.")

    def subir_nivel(self):
        self.__nivel += 1
        print(f" {self.nombre} subió al nivel {self.__nivel}")

    def estado(self):
        print(f"\n Estado de {self.nombre}:")
        print(f"Tipo: {self.tipo}")
        print(f"Nivel: {self.__nivel}")
        print(f"Salud: {self.__salud}")

    def get_nivel(self):
        return self.__nivel 

    def get_salud(self):
        return self.__salud  


class PokemonLegendario(Pokemon):
    def __init__(self, nombre, tipo, habilidad_especial):
        super().__init__(nombre, tipo)
        self.__habilidad_especial = habilidad_especial  

    def atacar(self, objetivo, dano):
        nivel = self.get_nivel()
        if dano > 0 and self.get_salud() > 0:
            if nivel > 50:
                dano += 20
                print(" Ataque potenciado por nivel legendario (+20 daño adicional)!")
            print(f"{self.nombre} lanza un ataque legendario a {objetivo.nombre} causando {dano} de daño.")
            objetivo.recibir_dano(dano)
        else:
            print(" Ataque fallido: daño inválido o salud insuficiente.")

    def usar_habilidad(self):
        print(f"\n {self.nombre} activa su habilidad especial: {self.__habilidad_especial}")
        print(" ¡El campo de batalla tiembla con poder legendario!")


# Ejemplo de uso
pikachu = Pokemon("Pikachu", "Eléctrico")
charizard = PokemonLegendario("Charizard", "Fuego", "Llama Eterna")

# Acciones básicas
pikachu.estado()
charizard.estado()

pikachu.atacar(charizard, 25)
charizard.subir_nivel()
for _ in range(51):
    charizard.subir_nivel()

charizard.atacar(pikachu, 30)
charizard.usar_habilidad()

pikachu.estado()
charizard.estado()
