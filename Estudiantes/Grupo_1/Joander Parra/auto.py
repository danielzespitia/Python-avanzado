class Auto:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.__encendido = False
        self.__nivel_combustible = 50

    def encender(self):
        if self.__nivel_combustible >= 10:
            if not self.__encendido:
                self.__encendido = True
                print("El auto ha sido encendido.")
            else:
                print("El auto ya está encendido.")
        else:
            print("No hay suficiente combustible para encender el auto.")

    def apagar(self):
        if self.__encendido:
            self.__encendido = False
            print("El auto ha sido apagado.")
        else:
            print("El auto ya está apagado.")

    def conducir(self, kilometros):
        if not self.__encendido:
            print("No puedes conducir: el auto está apagado.")
            return
        if kilometros <= 0:
            print("La distancia debe ser positiva.")
            return
        if self.__nivel_combustible < kilometros:
            print("No hay suficiente combustible para recorrer esa distancia.")
            return
        self.__nivel_combustible -= kilometros
        print(f"Has conducido {kilometros} km. Combustible restante: {self.__nivel_combustible}")

    def recargar_combustible(self, cantidad):
        if cantidad <= 0:
            print("La cantidad debe ser positiva.")
            return
        if self.__nivel_combustible + cantidad > 100:
            print("No puedes exceder el máximo de 100 de combustible.")
            self.__nivel_combustible = 100
        else:
            self.__nivel_combustible += cantidad
            print(f"Combustible recargado. Nivel actual: {self.__nivel_combustible}")

    def estado(self):
        encendido_str = "Encendido" if self.__encendido else "Apagado"
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Estado: {encendido_str}")
        print(f"Nivel de combustible: {self.__nivel_combustible}")

class AutoElectrico(Auto):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.__nivel_bateria = 50
        self.modo_autopiloto = False

    def cargar_bateria(self, cantidad):
        if cantidad <= 0:
            print("La cantidad debe ser positiva.")
            return
        if self.__nivel_bateria + cantidad > 100:
            self.__nivel_bateria = 100
            print("Batería cargada al 100%")
        else:
            self.__nivel_bateria += cantidad
            print(f"Batería cargada al {self.__nivel_bateria}%")

    def conducir(self, kilometros):
        if not self._Auto__encendido:
            print("No puedes conducir: el auto está apagado.")
            return
        if kilometros <= 0:
            print("La distancia debe ser positiva.")
            return
        if self.__nivel_bateria < kilometros:
            print("No hay suficiente batería para recorrer esa distancia.")
            return
        self.__nivel_bateria -= kilometros
        print(f"Has conducido {kilometros} km. Batería restante: {self.__nivel_bateria}%")

    def estado(self):
        encendido_str = "Encendido" if self._Auto__encendido else "Apagado"
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Estado: {encendido_str}")
        print(f"Nivel de batería: {self.__nivel_bateria}%")
        print(f"Modo autopiloto: {'Activado' if self.modo_autopiloto else 'Desactivado'}")

    def activar_autopiloto(self):
        self.modo_autopiloto = True
        print("Autopiloto activado. Conduciendo automáticamente.")

if __name__ == "__main__":
    print("=== AUTO COMBUSTION ===")
    auto1 = Auto("Toyota", "Corolla")
    auto1.estado()
    auto1.encender()
    auto1.conducir(20)
    auto1.recargar_combustible(30)
    auto1.conducir(70)
    auto1.apagar()
    auto1.estado()

    print("\n=== AUTO ELECTRICO ===")
    electrico1 = AutoElectrico("Tesla", "Model 3")
    electrico1.estado()
    electrico1.encender()
    electrico1.conducir(30)
    electrico1.cargar_bateria(40)