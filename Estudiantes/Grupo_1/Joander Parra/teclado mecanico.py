class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.__precio = precio
        self.__stock = stock

    def actualizar_stock(self, cantidad):
        if self.__stock + cantidad >= 0:
            self.__stock += cantidad
            return True
        else:
            return False

    def actualizar_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio

    def mostrar_detalle(self):
        print(f"Producto: {self.nombre}")
        print(f"Precio: ${self.__precio}")
        print(f"Stock: {self.__stock} unidades")

    def vender(self, cantidad):
        if cantidad <= 0:
            print("La cantidad a vender debe ser positiva.")
            return
        if self.actualizar_stock(-cantidad):
            print(f"Venta realizada: Se vendieron {cantidad} unidades.")
        else:
            print("No hay suficiente stock para realizar la venta.")

# Crear el producto
producto = Producto("Teclado Mecanico", 95, 30)

producto.vender(5)             
producto.actualizar_stock(10)   
producto.actualizar_precio(89.99) 

producto.mostrar_detalle()       

# El nombre es público, pero __precio y __stock son privados. ¿Por qué?
# El nombre es público para que pueda ser accedido directamente, mientras que __precio y __stock son privados
# para proteger la integridad de los datos y evitar modificaciones directas desde fuera de la clase

#Cuál es el propósito de set_precio()?
#R: El propósito de set_precio() es permitir la actualización controlada del precio de un producto.

# ¿Qué problema podría ocurrir si modificamos el precio directamente?
#R: Si se modifica el precio directamente, se podría establecer un valor inválido (por ejemplo, negativo)
# y no habría forma de validar o controlar este cambio, lo que podría llevar a inconsistencias en la lógica del negocio.

#¿Cómo actualizar_stock() decide si debe aumentar o disminuir el stock basado en el número recibido?
#R: La función actualizar_stock() recibe un número que puede ser positivo o negativo. Si el número es positivo, aumenta el stock,
# y si es negativo, disminuye el stock. Antes de realizar la actualización, verifica que el stock resultante no sea negativo,
# asegurando que no se pueda tener un stock negativo.

# Si creas un producto así:
#python
#mi_producto = Producto("Lámpara", -20, 5)
# ¿Cuál será el precio real del producto y por qué?
# R: El precio real del producto será -20, ya que el constructor de la clase Producto no valida el precio al momento de la creación.
# Esto significa que se puede crear un producto con un precio negativo

#Un producto tiene stock inicial de 15. Después de ejecutar:
#1. actualizar_stock(-10)
#2. actualizar_stock(-10)
#¿Cuál será el stock final? Justifica.
#R: El stock final será 5. La primera llamada a actualizar_stock(-10) reduce el stock de 15 a 5, y la segunda llamada a actualizar_stock(-10) no se puede realizar porque resultaría en un stock negativo.