'''
    Preguntas Conceptuales y Análisis

    * Sobre Encapsulamiento: ¿Por qué el atributo _saldo se escribe con doble guion bajo (_) al principio? ¿Qué intenta prevenir el programador al hacer esto?

    * Métodos "Getters": ¿Cuál es el propósito del método get_saldo()? Si ya tenemos el atributo __saldo, ¿por qué no lo leemos directamente desde fuera de la clase?

    * Lógica de Validación: En el método _init, ¿por qué se utiliza self.depositar(saldo_inicial) en lugar de asignar directamente self._saldo = saldo_inicial? ¿Qué ventaja nos da hacerlo de esa manera?

    * Predicción de Errores: Si intentas ejecutar el siguiente código, ¿qué mensaje se imprimirá en la pantalla y por qué?
        mi_cuenta_nueva = CuentaBancaria("Juan Pérez")
    mi_cuenta_nueva.retirar(100)

    * Análisis de Flujo: ¿Qué valor tendría el saldo final si se ejecutan estas tres operaciones en orden sobre una cuenta que empieza con $500?
        * depositar(200)
        * retirar(800)
        * retirar(700)
'''

print('se usa el doble guión bajo en el atributo __saldo para indicar que se convierta en privado, previniendo el acceso o modificación directa desde fuera creando un encapsulamiento')
print('el método get_saldo() sirve para proteger y controlar el acceso al atributo privado, por eso, no se debe leer directamente el atributo privado desde fuera de la clase')
print('usar self.depositar(saldo_inicial) en el constructor aplica automáticamente todas las validaciones del método, evita duplicar lógica y asegura que el objeto se inicializa correctamente y en un estado válido')
print('se imprime un mensaje de error porque el constructor espera que el saldo inicial sea un número, sin embargo, se le está pasando una cadena de texto')
print('el saldo final sería $0, suponiendo que la clase no permite retiros superiores al saldo disponible')

'''
    Ejercicios Prácticos de Código

    * Crear y Usar un Objeto:

    * Crea una instancia de CuentaBancaria para un titular llamado "Carlos Gómez" con un saldo inicial de $2,500.
    
    * Realiza un depósito de $500.

    * Intenta realizar un retiro de $3,500.

    * Realiza un retiro válido de $1,200.

    * Al final, llama al método mostrar_informacion() para ver el estado final de la cuenta.

    * Modificar la Clase (Desafío):

    * Añade un nuevo atributo "privado" a la clase llamado __numero_transacciones, que comenzará en 0.

    * Modifica los métodos depositar y retirar para que cada vez que se realice una operación exitosa, este contador se incremente en 1.

    * Modifica el método mostrar_informacion() para que también muestre el total de transacciones realizadas.
'''

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.__saldo = 0
        self.__numero_transacciones = 0
        self.depositar(saldo_inicial)
    
    def depositar(self, monto):
        if monto <= 0:
            print("El depósito debe ser mayor que cero.")
            return
        self.__saldo += monto
        self.__numero_transacciones += 1

    def retirar(self, monto):
        if monto <= 0:
            print("El retiro debe ser mayor que cero.")
            return
        if monto > self.__saldo:
            print("Fondos insuficientes para realizar el retiro.")
            return
        self.__saldo -= monto
        self.__numero_transacciones += 1

    def mostrar_informacion(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo actual: ${self.__saldo}")
        print(f"Total de transacciones: {self.__numero_transacciones}")

cuenta = CuentaBancaria("Carloz Gómez", 2500)
cuenta.depositar(500)
cuenta.retirar(3500)
cuenta.retirar(1200)
cuenta.mostrar_informacion()
