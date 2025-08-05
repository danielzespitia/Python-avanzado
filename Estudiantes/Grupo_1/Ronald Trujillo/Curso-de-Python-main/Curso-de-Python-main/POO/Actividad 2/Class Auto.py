class Auto:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.__encendido = False
        self.__nivel_combustible = 50  # empieza con 50 unidades

    def encender(self):
        if self.__nivel_combustible < 10:
            print("No hay suficiente combustible para encender el auto.")
            return
        if self.__encendido:
            print(f"El auto {self.marca} {self.modelo} ya está encendido.")
            return
        self.__encendido = True
        print(f"Auto {self.marca} {self.modelo} encendido.")

    def apagar(self):
        if not self.__encendido:
            print(f"El auto {self.marca} {self.modelo} ya está apagado.")
            return
        self.__encendido = False
        print(f"Auto {self.marca} {self.modelo} apagado.")

    def conducir(self, kilometros):
        if not self.__encendido:
            print("No puedes conducir. El auto está apagado.")
            return
        if kilometros <= 0:
            print("La distancia a conducir debe ser positiva.")
            return
        if kilometros > self.__nivel_combustible:
            print(f"No hay suficiente combustible para conducir {kilometros} km.")
            return
        self.__nivel_combustible -= kilometros
        print(f"Has conducido {kilometros} km. Combustible restante: {self.__nivel_combustible}.")

    def recargar_combustible(self, cantidad):
        if cantidad <= 0:
            print("La cantidad a recargar debe ser positiva.")
            return
        if self.__nivel_combustible + cantidad > 100:
            print("No puedes recargar más del máximo (100 unidades).")
            return
        self.__nivel_combustible += cantidad
        print(f"Combustible recargado. Nivel actual: {self.__nivel_combustible}.")

    def estado(self):
        print(f"\nEstado del auto {self.marca} {self.modelo}:")
        print(f" Encendido: {'Sí' if self.__encendido else 'No'}")
        print(f" Nivel de combustible: {self.__nivel_combustible}")


class AutoElectrico(Auto):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.__nivel_bateria = 50  # empieza con 50% de batería
        self.modo_autopiloto = False

    # Reemplaza recargar_combustible por cargar_bateria
    def cargar_bateria(self, porcentaje):
        if porcentaje <= 0:
            print("El porcentaje a cargar debe ser positivo.")
            return
        if self.__nivel_bateria + porcentaje > 100:
            print("No puedes cargar más del 100% de batería.")
            return
        self.__nivel_bateria += porcentaje
        print(f"Batería cargada al {self.__nivel_bateria}%.")

    def conducir(self, kilometros):
        if not self._Auto__encendido:
            print("No puedes conducir. El auto está apagado.")
            return
        if kilometros <= 0:
            print("La distancia a conducir debe ser positiva.")
            return
        if kilometros > self.__nivel_bateria:
            print(f"No hay suficiente batería para conducir {kilometros} km.")
            return
        self.__nivel_bateria -= kilometros
        print(f"Has conducido {kilometros} km. Batería restante: {self.__nivel_bateria}%.")

    def estado(self):
        print(f"\nEstado del auto eléctrico {self.marca} {self.modelo}:")
        print(f" Encendido: {'Sí' if self._Auto__encendido else 'No'}")
        print(f" Nivel de batería: {self.__nivel_bateria}%")
        print(f" Modo autopiloto: {'Activado' if self.modo_autopiloto else 'Desactivado'}")

    def activar_autopiloto(self):
        if not self._Auto__encendido:
            print("No puedes activar el autopiloto. El auto está apagado.")
            return
        self.modo_autopiloto = True
        print("Autopiloto activado. Conduciendo automáticamente 🚘🤖")


# === Ejemplo de uso ===

print("=== Auto de gasolina ===")
auto1 = Auto("Toyota", "Corolla")
auto1.estado()
auto1.encender()
auto1.conducir(20)
auto1.recargar_combustible(30)
auto1.apagar()
auto1.estado()

print("\n=== Auto eléctrico ===")
auto_elec = AutoElectrico("Tesla", "Model 3")
auto_elec.estado()
auto_elec.encender()
auto_elec.conducir(10)
auto_elec.cargar_bateria(40)
auto_elec.activar_autopiloto()
auto_elec.apagar()
auto_elec.estado()
