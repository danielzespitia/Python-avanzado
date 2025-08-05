class Auto:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.__encendido = False
        self.__nivel_combustible = 50

    def encender(self):
        if not self.__encendido:
            if self.__nivel_combustible >= 10:
                self.__encendido = True
                print(f"El {self.marca} {self.modelo} se ha encendido. ¡Listo para rodar!")
            else:
                print(f"No hay suficiente combustible para encender el {self.marca} {self.modelo}. Necesita al menos 10 unidades.")
        else:
            print(f"El {self.marca} {self.modelo} ya está encendido.")

    def apagar(self):
        if self.__encendido:
            self.__encendido = False
            print(f"El {self.marca} {self.modelo} se ha apagado.")
        else:
            print(f"El {self.marca} {self.modelo} ya está apagado.")

    def conducir(self, kilometros):
        if not self.__encendido:
            print(f"Error: El {self.marca} {self.modelo} está apagado. Enciéndelo primero.")
            return

        if kilometros < 0:
            print("Los kilómetros a conducir no pueden ser negativos.")
            return

        combustible_necesario = kilometros
        if self.__nivel_combustible >= combustible_necesario:
            self.__nivel_combustible -= combustible_necesario
            print(f"Conduciendo {kilometros} km. Combustible restante: {self.__nivel_combustible} unidades.")
        else:
            print(f"No hay suficiente combustible para conducir {kilometros} km. Quedan {self.__nivel_combustible} unidades.")
            self.__nivel_combustible = 0 
            self.apagar() 
            print("El auto se ha quedado sin combustible y se ha apagado.")


    def recargar_combustible(self, cantidad):
        if cantidad < 0:
            print("La cantidad a recargar no puede ser negativa.")
            return

        nueva_cantidad = self.__nivel_combustible + cantidad
        if nueva_cantidad > 100:
            recargado = 100 - self.__nivel_combustible
            self.__nivel_combustible = 100
            print(f"Recargado {recargado} unidades de combustible. Tanque lleno ({self.__nivel_combustible}/100).")
        else:
            self.__nivel_combustible = nueva_cantidad
            print(f"Recargado {cantidad} unidades de combustible. Nivel actual: {self.__nivel_combustible}/100.")

    def estado(self):
        estado_encendido = "Encendido" if self.__encendido else "Apagado"
        print(f"\n--- Estado del Auto: {self.marca} {self.modelo} ---")
        print(f"Estado: {estado_encendido}")
        print(f"Nivel de Combustible: {self.__nivel_combustible}/100 unidades")
        print("---------------------------------------")


class AutoElectrico(Auto):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self._Auto__nivel_combustible = 50 
        self.__nivel_bateria = 50 
        self.modo_autopiloto = False 
   
    def conducir(self, kilometros):
        if not self._Auto__encendido: 
            print(f"Error: El {self.marca} {self.modelo} está apagado. Enciéndelo primero.")
            return

        if kilometros < 0:
            print("Los kilómetros a conducir no pueden ser negativos.")
            return

        consumo_bateria = kilometros
        if self.__nivel_bateria >= consumo_bateria:
            self.__nivel_bateria -= consumo_bateria
            print(f"Conduciendo {kilometros} km. Batería restante: {self.__nivel_bateria}% .")
        else:
            print(f"No hay suficiente batería para conducir {kilometros} km. Queda {self.__nivel_bateria}% .")
            self.__nivel_bateria = 0
            self.apagar()
            print("El auto eléctrico se ha quedado sin batería y se ha apagado.")

  
    def recargar_combustible(self, cantidad):
        print("Este es un auto eléctrico. Usa 'cargar_bateria()' en su lugar.")

    def cargar_bateria(self, cantidad):
        if cantidad < 0:
            print("La cantidad a cargar no puede ser negativa.")
            return

        nueva_cantidad = self.__nivel_bateria + cantidad
        if nueva_cantidad > 100:
            cargado = 100 - self.__nivel_bateria
            self.__nivel_bateria = 100
            print(f"Batería cargada al {self.__nivel_bateria}% (se añadió {cargado}%).")
        else:
            self.__nivel_bateria = nueva_cantidad
            print(f"Batería cargada al {self.__nivel_bateria}% (se añadió {cantidad}%).")

   
    def estado(self):
        estado_encendido = "Encendido" if self._Auto__encendido else "Apagado" # Acceso al atributo privado de la clase base
        print(f"\n--- Estado del Auto Eléctrico: {self.marca} {self.modelo} ---")
        print(f"Estado: {estado_encendido}")
        print(f"Nivel de Batería: {self.__nivel_bateria}%")
        print(f"Modo Autopiloto: {'Activado' if self.modo_autopiloto else 'Desactivado'}")
        print("---------------------------------------")

    def activar_autopiloto(self):
        if self._Auto__encendido:
            self.modo_autopiloto = True
            print("Autopiloto activado. Conduciendo automáticamente ")
        else:
            print("El auto debe estar encendido para activar el autopiloto.")


print("\n--- Ejercicio 3: Clase Auto ---")
mi_auto = Auto("Toyota", "Corolla")
mi_auto.estado()

mi_auto.encender()
mi_auto.conducir(20)
mi_auto.recargar_combustible(10)
mi_auto.conducir(45) 
mi_auto.recargar_combustible(80)
mi_auto.recargar_combustible(-10) 
mi_auto.apagar()
mi_auto.conducir(5) 
mi_auto.estado()

print("\n--- Pruebas de Auto Eléctrico ---")
tesla = AutoElectrico("Tesla", "Model 3")
tesla.estado()

tesla.encender()
tesla.conducir(30)
tesla.cargar_bateria(20)
tesla.activar_autopiloto()
tesla.conducir(80) 
tesla.cargar_bateria(100) 
tesla.estado()
