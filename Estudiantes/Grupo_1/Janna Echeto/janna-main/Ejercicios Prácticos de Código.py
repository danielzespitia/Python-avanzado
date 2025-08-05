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
Preguntas para el Ejercicio 2: Producto 📦
Preguntas Conceptuales y de Análisis
 * Atributos Públicos vs. Privados: En la clase Producto, el nombre es un atributo público, pero __precio y __stock son privados. ¿Cuál crees que es la razón de esta diferencia de diseño?
 * Métodos "Setters": ¿Cuál es la función principal del método set_precio()? ¿Qué problema podría ocurrir si el precio se pudiera cambiar directamente sin este método?
 * Lógica Unificada: El método actualizar_stock() sirve tanto para añadir como para quitar unidades. ¿Cómo sabe el método si debe aumentar o disminuir el stock basándose en el número que recibe?
 * Predicción de Estado: Si creas un producto así: mi_producto = Producto("Lámpara", -20, 5), ¿cuál será el precio real del producto según el código y por qué?
 * Análisis de Flujo: Un producto tiene un stock inicial de 15. ¿Cuál será el stock final después de ejecutar estas dos operaciones en orden? Explica por qué.
   * actualizar_stock(-10)
   * actualizar_stock(-10)
Ejercicios Prácticos de Código
 * Crear y Gestionar un Producto:
   * Crea una instancia de la clase Producto para un "Teclado Mecánico", con un precio de $95 y un stock inicial de 30 unidades.
   * Simula la venta de 5 teclados.
   * El proveedor envía 10 teclados más. Actualiza el stock para reflejar su llegada.
   * Debido a una oferta, actualiza el precio del teclado a $89.99.
   * Muestra el detalle final del producto.
 * Modificar la Clase (Desafío):
   * Añade un método llamado vender(cantidad). Este método debe ser una forma más intuitiva de disminuir el stock. Internamente, deberá llamar a actualizar_stock() con el número correcto (es decir, un número negativo).
   * El método vender debe imprimir un mensaje específico como "Venta realizada: Se vendieron X unidades." si la venta es exitosa. Si no hay stock, debe indicarlo.