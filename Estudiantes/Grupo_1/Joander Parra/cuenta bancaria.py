#Sobre Encapsulamiento: �Por qu� el atributo _saldo se escribe con doble guion bajo (_) al principio? �Qu� intenta prevenir el programador al hacer esto?
#R: Para indicar que es un atributo privado

# M�todos "Getters": �Cu�l es el prop�sito del m�todo get_saldo()? Si ya tenemos el atributo __saldo, �por qu� no lo leemos directamente desde fuera de la clase?
#R:  es proporcionar una interfaz controlada y p�blica para acceder al valor del atributo desde fuera de la clase

#L�gica de Validaci�n: En el m�todo _init, �por qu� se utiliza self.depositar(saldo_inicial) en lugar de asignar directamente self._saldo = saldo_inicial? 
# �Qu� ventaja nos da hacerlo de esa manera?
#R: Garantiza que el saldo inicial se establezca de la misma manera controlada y validada que cualquier otro dep�sito posterior. 
#Esto mantiene la consistencia del estado interno del objeto desde el momento de su creaci�n.

# * Predicci�n de Errores: Si intentas ejecutar el siguiente c�digo, �qu� mensaje se imprimir� en la pantalla y por qu�?
#  mi_cuenta_nueva = CuentaBancaria("Juan P�rez")
#mi_cuenta_nueva.retirar(100)
#R: lo msa probable es que imprima en la pantalla un mensaje typerror

#* An�lisis de Flujo: �Qu� valor tendr�a el saldo final si se ejecutan estas tres operaciones en orden sobre una cuenta que empieza con $500?
#   * depositar(200)
#   * retirar(800)
#   * retirar(700)
#R: queda la cuenta en 0



class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial
        self.__numero_transacciones = 0 

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            self.__numero_transacciones += 1
            print(f"Deposito exitoso de ${cantidad}.")
            return True
        print("Cantidad de deposito invalida.")
        return False

    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            self.__numero_transacciones += 1
            print(f"Retiro exitoso de ${cantidad}.")
            return True
        print("Retiro invalido o fondos insuficientes.")
        return False

    def mostrar_informacion(self):
        print(f"Titular:
       {self.titular}")
        print(f"Saldo actual: ${self.saldo}")
        print(f"Total de transacciones realizadas: {self.__numero_transacciones}")

cuenta = CuentaBancaria("Carlos Gomez", 2500)
cuenta.depositar(500)
cuenta.retirar(3500)   
cuenta.retirar(1200)   
cuenta.mostrar_informacion()


