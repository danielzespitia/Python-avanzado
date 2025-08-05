class Auto:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.__encendido = False
        self.__nivel_combustible = 50

    def encender(self):
        if self.__nivel_combustible >= 10:
            self.__encendido = True
            print("Auto encendido.")
        else:
            print("No hay suficiente combustible para encender el auto.")

    def apagar(self):
        self.__encendido = False
        print("Auto apagado.")

    def conducir(self, kilometros):
        if not self.__encendido:
            print("No se puede conducir, el auto está apagado.")
            return
        consumo = kilometros
        if consumo > self.__nivel_combustible:
            print("No hay suficiente combustible para recorrer esa distancia.")
            return
        self.__nivel_combustible -= consumo
        print(f"Condujiste {kilometros} km. Combustible restante: {self.__nivel_combustible}")

    def recarga_combustible(self, cantidad):
        if cantidad <= 0:
            print("La cantidad debe ser positiva.")
            return
        if self.__nivel_combustible + cantidad > 100:
            print("No se puede exceder el nivel máximo de combustible (100).")
            return
        self.__nivel_combustible += cantidad
        print(f"Combustible recargado. Nivel actual: {self.__nivel_combustible}")

    def estado(self):
        encendido = "Sí" if self.__encendido else "No"
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"¿Encendido?: {encendido}")
        print(f"Nivel de combustible: {self.__nivel_combustible}")

class AutoElectrico(Auto):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self._AutoElectrico__nivel_bateria = 50
        self.modo_autopiloto = False

    def cargar_bateria(self, cantidad):
        if cantidad <= 0:
            print("La cantidad debe ser positiva.")
            return
        if self._AutoElectrico__nivel_bateria + cantidad > 100:
            print("No se puede exceder el nivel máximo de batería (100).")
            return
        self._AutoElectrico__nivel_bateria += cantidad
        print(f"Batería cargada al {self._AutoElectrico__nivel_bateria}%")

    def estado(self):
        encendido = "Sí" if self._Auto__encendido else "No"
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"¿Encendido?: {encendido}")
        print(f"Nivel de batería: {self._AutoElectrico__nivel_bateria}")
        print(f"Modo autopiloto: {'Activado' if self.modo_autopiloto else 'Desactivado'}")

    def activar_autopiloto(self):
        self.modo_autopiloto = True
        print("Autopiloto activado. Conduciendo automáticamente.")

    def conducir(self, kilometros):
        if not self._Auto__encendido:
            print("No se puede conducir, el auto está apagado.")
            return
        consumo = kilometros
        if consumo > self._AutoElectrico__nivel_bateria:
            print("No hay suficiente batería para recorrer esa distancia.")
            return
        self._AutoElectrico__nivel_bateria -= consumo
        print(f"Condujiste {kilometros} km. Batería restante: {self._AutoElectrico__nivel_bateria}")

    def recarga_combustible(self, cantidad):
        print("Este auto no utiliza combustible.")

if __name__ == "__main__":
    print("--- AUTO NORMAL ---")
    auto = Auto("Toyota", "Corolla")
    auto.estado()
    auto.encender()
    auto.conducir(20)
    auto.recarga_combustible(40)
    auto.estado()
    auto.apagar()

    print("\n--- AUTO ELÉCTRICO ---")
    tesla = AutoElectrico("Tesla", "Model 3")
    tesla.estado()
    tesla.encender()
    tesla.conducir(30)
    tesla.cargar_bateria(40)
    tesla.estado()
    tesla.activar_autopiloto()