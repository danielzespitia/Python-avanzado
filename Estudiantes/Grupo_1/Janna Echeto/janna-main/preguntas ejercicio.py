Preguntas para el Ejercicio 1: CuentaBancaria 🏦
Preguntas Conceptuales y de Análisis
 * Sobre Encapsulamiento: ¿Por qué el atributo _saldo se escribe con doble guion bajo (_) al principio? ¿Qué intenta prevenir el programador al hacer esto? # se realiza para decir que algo es privado (esta protegido), se hace para que una persona no autorizada modifique el saldo
 * Métodos "Getters": ¿Cuál es el propósito del método get_saldo()? Si ya tenemos el atributo __saldo, ¿por qué no lo leemos directamente desde fuera de la clase? # es para ver el saldo fuera de la clse, de una forma controlada y asi no modificar el codigo en un futuro
 * Lógica de Validación: En el método _init, ¿por qué se utiliza self.depositar(saldo_inicial) en lugar de asignar directamente self._saldo = saldo_inicial? ¿Qué ventaja nos da hacerlo de esa manera? # se usa self.depositar en _init_ para volver a usar la logica de validación del metodo depositar, asi me aseguro de que el saldo inicial cumpla las mismas reglas que cualquier otro depósito, evitando duplicar codigo.
 * Predicción de Errores: Si intentas ejecutar el siguiente código, ¿qué mensaje se imprimirá en la pantalla y por qué?
   mi_cuenta_nueva = CuentaBancaria("Juan Pérez") 
mi_cuenta_nueva.retirar(100) # mostrara AttributeError, en Python renombra los atributos con doble guion bajo haciéndolos inaccesibles directamente.

 * Análisis de Flujo: ¿Qué valor tendría el saldo final si se ejecutan estas tres operaciones en orden sobre una cuenta que empieza con $500?
   * depositar(200)
   * retirar(800)
   * retirar(700)

# Saldo inicial
saldo_final = 500
print(f"Saldo inicial: ${saldo_final}")

# 1. a depositar(200)
saldo_final += 200
print(f"Después de depositar 200: ${saldo_final}")

# 2.para retirar(800)
saldo_final -= 800
print(f"Después de retirar 800: ${saldo_final}")

# 3. retirar(700)
saldo_final -= 700
print(f"Después de retirar 700: ${saldo_final}")

print(f"\nEl valor final del saldo es: ${saldo_final}")