class Auto:
    def __init__(self, marca, modelo):
        self.marca = marca  
        self.modelo = modelo  
        self.__encendido = False  
        self.__nivel_combustible = 50  

    def encender(self):
        if self.__nivel_combustible >= 10:
            self.__encendido = True
            print(f" {self.marca} {self.modelo} ha sido encendido.")
        else:
            print(" Combustible insuficiente para encender el auto.")

    def apagar(self):
        self.__encendido = False
        print(f" {self.marca} {self.modelo} ha sido apagado.")

    def conducir(self, kilometros):
        if not self.__encendido:
            print(" No se puede conducir. El auto está apagado.")
            return
        consumo = kilometros
        if consumo > self.__nivel_combustible:
            print(" No hay suficiente combustible para recorrer esa distancia.")
        else:
            self.__nivel_combustible -= consumo
            print(f" Conduciendo {kilometros} km. Combustible restante: {self.__nivel_combustible}")

    def recargar_combustible(self, cantidad):
        if cantidad <= 0:
            print(" No se puede recargar con una cantidad negativa o cero.")
        elif self.__nivel_combustible + cantidad > 100:
            print(" No se puede exceder el máximo de 100 unidades de combustible.")
        else:
            self.__nivel_combustible += cantidad
            print(f" Combustible recargado. Nivel actual: {self.__nivel_combustible}")

    def estado(self):
        encendido_str = "Encendido" if self.__encendido else "Apagado"
        print("\n Estado del Auto:")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Estado: {encendido_str}")
        print(f"Nivel de combustible: {self.__nivel_combustible}")



class AutoElectrico(Auto):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.__nivel_bateria = 50  
        self.modo_autopiloto = False  

    def encender(self):
        if self.__nivel_bateria >= 10:
            print(f" {self.marca} {self.modelo} ha sido encendido (eléctrico).")
            self._Auto__encendido = True  
        else:
            print(" Batería insuficiente para encender el auto eléctrico.")

    def conducir(self, kilometros):
        if not self._Auto__encendido:
            print(" No se puede conducir. El auto eléctrico está apagado.")
            return
        consumo = kilometros
        if consumo > self.__nivel_bateria:
            print(" No hay suficiente batería para recorrer esa distancia.")
        else:
            self.__nivel_bateria -= consumo
            print(f" Conduciendo {kilometros} km. Batería restante: {self.__nivel_bateria}")

    def cargar_bateria(self, cantidad):
        if cantidad <= 0:
            print(" No se puede cargar con una cantidad negativa o cero.")
        elif self.__nivel_bateria + cantidad > 100:
            print(" No se puede exceder el máximo de 100% de batería.")
        else:
            self.__nivel_bateria += cantidad
            print(f" Batería cargada al {self.__nivel_bateria}%")

    def activar_autopiloto(self):
        self.modo_autopiloto = True
        print(" Autopiloto activado. Conduciendo automáticamente 🚘")

    def estado(self):
        encendido_str = "Encendido" if self._Auto__encendido else "Apagado"
        print("\n Estado del Auto Eléctrico:")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Estado: {encendido_str}")
        print(f"Nivel de batería: {self.__nivel_bateria}%")
        print(f"Autopiloto: {'Activado' if self.modo_autopiloto else 'Desactivado'}")


# Ejemplo de uso
print(" AUTO TRADICIONAL")
mi_auto = Auto("Toyota", "Corolla")
mi_auto.estado()
mi_auto.conducir(20)
mi_auto.encender()
mi_auto.conducir(30)
mi_auto.recargar_combustible(40)
mi_auto.estado()

print("\n AUTO ELÉCTRICO")
tesla = AutoElectrico("Tesla", "Model S")
tesla.estado()
tesla.encender()
tesla.conducir(45)
tesla.cargar_bateria(30)
tesla.activar_autopiloto()
tesla.estado()
