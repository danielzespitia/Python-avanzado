class Auto:
def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.__encendido = False
        self.__nivel_combustible =  50

    def encender(self):
        if self.__nivel_combustible >= 10:
            self.__encendido = True
            print(f"{self.marca} {self.modelo} encendido ✅")
        else:
            print("No hay suficiente combustible para encender (mínimo 10 unidades)")

    def apagar(self):
        self.__encendido = False
        print(f"{self.marca} {self.modelo} apagado 📴")

    def conducir(self, kilometros):
        if not self.__encendido:
            print("No se puede conducir: el auto está apagado")
            return
        
        if kilometros <= self.__nivel_combustible:
            self.__nivel_combustible -= kilometros
            print(f"Conduciendo {kilometros} km 🚀. Combustible restante: {self.__nivel_combustible}")
        else:
            print(f"No hay suficiente combustible para {kilometros} km. Máximo posible: {self.__nivel_combustible} km")

    def recargar_combustible(self, cantidad):
        if cantidad < 0:
            print("No se puede recargar con valores negativos")
            return
        
        nuevo_nivel = self.__nivel_combustible + cantidad
        if nuevo_nivel > 100:
            self.__nivel_combustible = 100
            print(f"Tanque lleno (100 unidades). Sobraron {nuevo_nivel - 100} unidades")
        else:
            self.__nivel_combustible = nuevo_nivel
            print(f"Combustible recargado. Nuevo nivel: {self.__nivel_combustible}")

    def estado(self):
        estado = "encendido" if self.__encendido else "apagado"
        print(f"\nEstado de {self.marca} {self.modelo}:")
        print(f"• Encendido: {estado}")
        print(f"• Nivel de combustible: {self.__nivel_combustible}")
        print("-----------------------")


class AutoElectrico(Auto):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.__nivel_bateria = 50  # Reemplaza el combustible por batería
        self.modo_autopiloto = False  # Nuevo atributo

    def encender(self):
        if self.__nivel_bateria >= 10:
            self._Auto__encendido = True  # Accediendo al atributo privado de la clase padre
            print(f"{self.marca} {self.modelo} encendido ✅ (Batería: {self.__nivel_bateria}%)")
        else:
            print("No hay suficiente batería para encender (mínimo 10%)")

    def conducir(self, kilometros):
        if not self._Auto__encendido:
            print("No se puede conducir: el auto está apagado")
            return
        
        if kilometros <= self.__nivel_bateria:
            self.__nivel_bateria -= kilometros
            print(f"Conduciendo {kilometros} km 🚗⚡. Batería restante: {self.__nivel_bateria}%")
            if self.modo_autopiloto:
                print("Autopiloto activado. Conduciendo automáticamente 🚘🤖")
        else:
            print(f"No hay suficiente batería para {kilometros} km. Máximo posible: {self.__nivel_bateria} km")

    def cargar_bateria(self, cantidad):
        if cantidad < 0:
            print("No se puede cargar con valores negativos")
            return
        
        nuevo_nivel = self.__nivel_bateria + cantidad
        if nuevo_nivel > 100:
            self.__nivel_bateria = 100
            print(f"Batería cargada al 100% ⚡. Sobraron {nuevo_nivel - 100}%")
        else:
            self.__nivel_bateria = nuevo_nivel
            print(f"Batería cargada al {self.__nivel_bateria}% ⚡")

    def activar_autopiloto(self):
        if self._Auto__encendido:
            self.modo_autopiloto = True
            print("Autopiloto activado. Conduciendo automáticamente 🚘🤖")
        else:
            print("No se puede activar autopiloto: el auto está apagado")

    def estado(self):
        estado = "encendido" if self._Auto__encendido else "apagado"
        autopiloto = "activado" if self.modo_autopiloto else "desactivado"
        print(f"\nEstado de {self.marca} {self.modelo} (Eléctrico):")
        print(f"• Encendido: {estado}")
        print(f"• Nivel de batería: {self.__nivel_bateria}%")
        print(f"• Modo autopiloto: {autopiloto}")
        print("-----------------------")

