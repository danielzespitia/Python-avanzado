# 1)Preguntas Conceptuales y de Análisis
# Sobre Encapsulamiento: ¿Por qué el atributo _saldo se escribe con doble guion bajo (_) al principio? ¿Qué intenta prevenir el programador al hacer esto?
#Respueta:Usamos doble guion para indicar que es un atributo Privado

#2)Métodos "Getters": ¿Cuál es el propósito del método get_saldo()? Si ya tenemos el atributo __saldo, ¿por qué no lo leemos directamente desde fuera de la clase?
#Respuesta: es una forma mas controlada a acceder al atributo

#3)Lógica de Validación: En el método _init, ¿por qué se utiliza self.depositar(saldo_inicial) en lugar de asignar directamente self._saldo = saldo_inicial? ¿Qué ventaja nos da hacerlo de esa manera?
# Respuesta: nos permite que el estado del objeto siempre se mantenga válido y consistente
 
#4)Predicción de Errores: Si intentas ejecutar el siguiente código, ¿qué mensaje se imprimirá en la pantalla y por qué?
#mi_cuenta_nueva = CuentaBancaria("Juan Pérez")
#mi_cuenta_nueva.retirar(100)
