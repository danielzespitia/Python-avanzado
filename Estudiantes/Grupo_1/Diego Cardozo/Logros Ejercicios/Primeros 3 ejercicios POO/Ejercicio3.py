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
                print(f"El {self.marca} {self.modelo} ha sido encendido.")
            else:
                print(f"El {self.marca} {self.modelo} ya está encendido.")
        else:
            print(f"No hay suficiente combustible para encender el {self.marca} {self.modelo}. (Nivel: {self.__nivel_combustible}%)")

    def apagar(self):
        if self.__encendido:
            self.__encendido = False
            print(f"El {self.marca} {self.modelo} ha sido apagado.")
        else:
            print(f"El {self.marca} {self.modelo} ya está apagado.")

    def conducir(self, kilometros):
        if not self.__encendido:
            print(f"No se puede conducir el {self.marca} {self.modelo} porque está apagado.")
            return

        if kilometros <= 0:
            print("Los kilómetros a conducir deben ser un valor positivo.")
            return

        combustible_necesario = kilometros * 1
        
        if self.__nivel_combustible >= combustible_necesario:
            self.__nivel_combustible -= combustible_necesario
            print(f"El {self.marca} {self.modelo} ha conducido {kilometros} km.")
            print(f"Nivel de combustible restante: {self.__nivel_combustible}%.")
        else:
            print(f"No hay suficiente combustible para conducir {kilometros} km. Quedan {self.__nivel_combustible}% y necesitas {combustible_necesario}%.")
            print("El auto se ha detenido.")
            self.apagar()

    def recargar_combustible(self, cantidad):
        if cantidad <= 0:
            print("La cantidad a recargar debe ser un valor positivo.")
            return
        
        nueva_cantidad = self.__nivel_combustible + cantidad
        
        if nueva_cantidad > 100:
            recargado_real = 100 - self.__nivel_combustible
            self.__nivel_combustible = 100
            print(f"Recargado {recargado_real}% de combustible. El tanque está lleno (100%).")
        else:
            self.__nivel_combustible = nueva_cantidad
            print(f"Recargado {cantidad}% de combustible. Nivel actual: {self.__nivel_combustible}%.")
    
    def estado(self):
        estado_encendido = "ENCENDIDO" if self.__encendido else "APAGADO"
        return (f"--- Estado del Auto ---\n"
                f"Marca: {self.marca}\n"
                f"Modelo: {self.modelo}\n"
                f"Estado: {estado_encendido}\n"
                f"Nivel de Combustible: {self.__nivel_combustible}%")

class AutoElectrico(Auto):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        
        self.__nivel_bateria = 50
        
        self.modo_autopiloto = False 

    def cargar_bateria(self, cantidad):
        if cantidad <= 0:
            print("La cantidad a cargar debe ser un valor positivo.")
            return
        
        nueva_cantidad = self.__nivel_bateria + cantidad
        
        if nueva_cantidad > 100:
            recargado_real = 100 - self.__nivel_bateria
            self.__nivel_bateria = 100
            print(f"Batería cargada {recargado_real}% (máx). Batería cargada al 100%.")
        else:
            self.__nivel_bateria = nueva_cantidad
            print(f"Batería cargada al {self.__nivel_bateria}%.")

    def conducir(self, kilometros):
        if not self._Auto__encendido:
            print(f"No se puede conducir el {self.marca} {self.modelo} eléctrico porque está apagado.")
            return

        if kilometros <= 0:
            print("Los kilómetros a conducir deben ser un valor positivo.")
            return

        bateria_necesaria = kilometros * 1
        
        if self.__nivel_bateria >= bateria_necesaria:
            self.__nivel_bateria -= bateria_necesaria
            print(f"El {self.marca} {self.modelo} eléctrico ha conducido {kilometros} km.")
            print(f"Nivel de batería restante: {self.__nivel_bateria}%.")
        else:
            print(f"No hay suficiente batería para conducir {kilometros} km. Queda {self.__nivel_bateria}% y necesitas {bateria_necesaria}%.")
            print("El auto eléctrico se ha detenido.")
            self.apagar()

    def activar_autopiloto(self):
        if not self._Auto__encendido:
            print("No se puede activar el autopiloto si el auto está apagado.")
            return
        
        if not self.modo_autopiloto:
            self.modo_autopiloto = True
            print("Autopiloto activado. Conduciendo automáticamente")
        else:
            print("El autopiloto ya está activado.")

    def desactivar_autopiloto(self):
        if self.modo_autopiloto:
            self.modo_autopiloto = False
            print("Autopiloto desactivado. Vuelve al control manual.")
        else:
            print("El autopiloto ya está desactivado.")

    def estado(self):
        estado_encendido = "ENCENDIDO" if self._Auto__encendido else "APAGADO"
        estado_autopiloto = "ACTIVADO" if self.modo_autopiloto else "DESACTIVADO"
        return (f"--- Estado del Auto Eléctrico ---\n"
                f"Marca: {self.marca}\n"
                f"Modelo: {self.modelo}\n"
                f"Estado: {estado_encendido}\n"
                f"Nivel de Batería: {self.__nivel_bateria}%\n"
                f"Modo Autopiloto: {estado_autopiloto}")


mi_auto = Auto("Toyota", "Corolla")
print(mi_auto.estado())

mi_auto.conducir(5)
mi_auto.encender()
mi_auto.conducir(20)
print(mi_auto.estado())

mi_auto.recargar_combustible(30)
print(mi_auto.estado())
mi_auto.recargar_combustible(70)
print(mi_auto.estado())
mi_auto.recargar_combustible(-10)

mi_auto.conducir(100)
print(mi_auto.estado())
mi_auto.encender()
mi_auto.recargar_combustible(50)
mi_auto.encender()
mi_auto.apagar()
print(mi_auto.estado())


mi_auto_electrico = AutoElectrico("Tesla", "Model 3")
print(mi_auto_electrico.estado())

mi_auto_electrico.conducir(5)
mi_auto_electrico.encender()
mi_auto_electrico.conducir(20)
print(mi_auto_electrico.estado())

mi_auto_electrico.cargar_bateria(30)
print(mi_auto_electrico.estado())
mi_auto_electrico.cargar_bateria(70)
print(mi_auto_electrico.estado())
mi_auto_electrico.cargar_bateria(-10)

mi_auto_electrico.activar_autopiloto()
mi_auto_electrico.activar_autopiloto()

mi_auto_electrico.conducir(100)
print(mi_auto_electrico.estado())
mi_auto_electrico.encender()
mi_auto_electrico.cargar_bateria(50)
mi_auto_electrico.encender()
mi_auto_electrico.desactivar_autopiloto()
mi_auto_electrico.apagar()
print(mi_auto_electrico.estado())