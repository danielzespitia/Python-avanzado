class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = 0
        self.__numero_transacciones = 0
        self.depositar(saldo_inicial)

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            self.__numero_transacciones += 1
            print(f"Depósito exitoso de ${monto}")
        else:
            print("Monto inválido para depositar.")

    def retirar(self, monto):
        if monto <= 0:
            print("Monto inválido para retirar.")
        elif monto > self.__saldo:
            print("Fondos insuficientes.")
        else:
            self.__saldo -= monto
            self.__numero_transacciones += 1
            print(f"Retiro exitoso de ${monto}")

    def get_saldo(self):
        return self.__saldo

    def mostrar_informacion(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo: ${self.__saldo}")
        print(f"Número de transacciones: {self.__numero_transacciones}")
        print()


# Ejemplo de uso
cuenta = CuentaBancaria("Juan Perez", 1000)
cuenta.mostrar_informacion()

cuenta.depositar(500)
cuenta.mostrar_informacion()

cuenta.retirar(200)
cuenta.mostrar_informacion()

cuenta.retirar(1500)  # Fondos insuficientes
cuenta.mostrar_informacion()
cuenta.retirar(-100)  # Monto inválido
cuenta.mostrar_informacion()
cuenta.depositar(-50)  # Monto inválido
cuenta.mostrar_informacion()
cuenta.depositar(300)
cuenta.mostrar_informacion()    

