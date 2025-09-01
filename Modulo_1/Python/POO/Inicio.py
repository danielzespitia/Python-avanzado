
"""
TUTORIAL AVANZADO DE PROGRAMACIÓN ORIENTADA A OBJETOS (POO) EN PYTHON

Bienvenido a este tutorial completo sobre POO en Python. Aquí exploraremos desde
los conceptos más básicos hasta las características más avanzadas que Python
ofrece para este paradigma de programación.

La POO es un paradigma que organiza el software alrededor de "objetos" en lugar de
"acciones" y "lógica". Un objeto es una entidad que contiene tanto datos (atributos)
como comportamiento (métodos).

--- ÍNDICE ---
1.  Fundamentos: Clases y Objetos
2.  Constructores y Atributos
3.  Métodos: El Comportamiento de los Objetos
4.  Los 4 Pilares de la POO:
    4.1. Encapsulamiento
    4.2. Herencia
    4.3. Polimorfismo
    4.4. Abstracción
5.  Conceptos Avanzados:
    5.1. Métodos Especiales (Dunder Methods)
    5.2. Decoradores en Clases (@property, @classmethod, @staticmethod)
    5.3. Data Classes
    5.4. Metaclases
"""

# =============================================================================
# 1. FUNDAMENTOS: CLASES Y OBJETOS
# =============================================================================
print("--- 1. Clases y Objetos ---")

# Explicación 1.1: La Plantilla (Clase) y la Instancia (Objeto)
# Una 'clase' es como un plano o un molde para crear 'objetos'. Define un conjunto
# de atributos (variables) y métodos (funciones) que los objetos de esa clase tendrán.
# Un 'objeto' es una instancia concreta de una clase. Si la clase 'Coche' es el plano,
# un coche específico con un color y matrícula determinados es el objeto.

# Explicación 1.2: Sintaxis Básica
# Para definir una clase, usamos la palabra clave `class` seguida del nombre de la
# clase (por convención, en CamelCase). El contenido de la clase se indenta.
# La instrucción `pass` se usa para indicar un bloque vacío.

# Explicación 1.3: Creación de Instancias
# Para crear un objeto (instanciar una clase), simplemente llamamos a la clase como
# si fuera una función.

# Ejemplo 1.1: Definiendo una clase simple y creando objetos
class Gato:
    pass  # Por ahora, nuestra clase no hace nada.

# Creando instancias (objetos) de la clase Gato
gato_1 = Gato()
gato_2 = Gato()

print(f"gato_1 es un objeto de tipo: {type(gato_1)}")
print(f"gato_2 es un objeto de tipo: {type(gato_2)}")
print(f"¿Son gato_1 y gato_2 el mismo objeto? {'Sí' if gato_1 is gato_2 else 'No'}")

# Ejemplo 1.2: Una clase para representar un Videojuego
class Videojuego:
    pass

mi_juego_favorito = Videojuego()
juego_nuevo = Videojuego()

print(f"\nmi_juego_favorito es un: {type(mi_juego_favorito)}")
print(f"juego_nuevo es un: {type(juego_nuevo)}")


# =============================================================================
# 2. CONSTRUCTORES Y ATRIBUTOS
# =============================================================================
print("\n--- 2. Constructores y Atributos ---")

# Explicación 2.1: El Constructor `__init__`
# El método `__init__` es un método especial (dunder method) que se llama
# automáticamente cuando se crea una nueva instancia de una clase. Su función
# principal es inicializar los atributos del objeto. El primer parámetro de
# `__init__` es siempre `self`, que representa la instancia que se está creando.

# Explicación 2.2: Atributos de Instancia
# Son datos que pertenecen a un objeto específico. Cada instancia puede tener
# valores diferentes para sus atributos de instancia. Se definen dentro de
# `__init__` usando `self.nombre_atributo = valor`.

# Explicación 2.3: Atributos de Clase
# Son datos que se comparten entre todas las instancias de una clase. Se definen
# directamente dentro del cuerpo de la clase, fuera de cualquier método.

# Ejemplo 2.1: Clase 'Libro' con atributos de instancia
class Libro:
    def __init__(self, titulo, autor, paginas):
        # Atributos de instancia
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        print(f"Se ha creado el libro '{self.titulo}'.")

# Creando instancias con diferentes atributos
libro_1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 432)
libro_2 = Libro("El Señor de los Anillos", "J.R.R. Tolkien", 1200)

print(f"Título del libro 1: {libro_1.titulo}")
print(f"Autor del libro 2: {libro_2.autor}")

# Ejemplo 2.2: Clase 'Personaje' con atributos de instancia y de clase
class Personaje:
    # Atributo de clase: compartido por todos los personajes
    especie = "Homo Sapiens"

    def __init__(self, nombre, profesion):
        # Atributos de instancia: específicos de cada personaje
        self.nombre = nombre
        self.profesion = profesion

heroe = Personaje("Aragorn", "Explorador")
mago = Personaje("Gandalf", "Mago")

# Accediendo a atributos de instancia
print(f"\nNombre: {heroe.nombre}, Profesión: {heroe.profesion}")
print(f"Nombre: {mago.nombre}, Profesión: {mago.profesion}")

# Accediendo al atributo de clase (se puede hacer desde la clase o la instancia)
print(f"Especie de Héroe: {heroe.especie}")
print(f"Especie de Mago: {mago.especie}")
print(f"Especie definida en la clase: {Personaje.especie}")

# Modificar un atributo de clase afecta a todas las instancias
Personaje.especie = "Seres de la Tierra Media"
print(f"Nueva especie de Héroe: {heroe.especie}")


# =============================================================================
# 3. MÉTODOS: EL COMPORTAMIENTO DE LOS OBJETOS
# =============================================================================
print("\n--- 3. Métodos ---")

# Explicación 3.1: Métodos de Instancia
# Son funciones definidas dentro de una clase que operan sobre una instancia
# de esa clase. Siempre reciben `self` como su primer argumento, lo que les
# permite acceder y modificar los atributos de la instancia.

# Explicación 3.2: El parámetro `self`
# `self` es una convención (podría llamarse de otra forma, pero no deberías).
# Se refiere a la instancia sobre la cual se está llamando el método. Python
# lo pasa automáticamente cuando llamas al método desde un objeto.
# `mi_objeto.mi_metodo(arg1)` es azúcar sintáctico para `MiClase.mi_metodo(mi_objeto, arg1)`.

# Explicación 3.3: Métodos y Atributos
# Los métodos son la forma principal en que un objeto interactúa con sus propios
# datos (atributos). Permiten realizar acciones y cálculos basados en el estado
# del objeto.

# Ejemplo 3.1: Clase 'CuentaBancaria' con métodos de instancia
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    # Método para depositar dinero
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito de ${cantidad} realizado. Nuevo saldo: ${self.saldo}")
        else:
            print("La cantidad a depositar debe ser positiva.")

    # Método para retirar dinero
    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro de ${cantidad} realizado. Nuevo saldo: ${self.saldo}")
        else:
            print("Fondos insuficientes o cantidad inválida.")

    # Método para mostrar el saldo
    def mostrar_saldo(self):
        print(f"El saldo de la cuenta de {self.titular} es ${self.saldo}")

mi_cuenta = CuentaBancaria("Juan Pérez", 1000)
mi_cuenta.mostrar_saldo()
mi_cuenta.depositar(500)
mi_cuenta.retirar(200)
mi_cuenta.retirar(2000) # Intentar retirar más de lo que hay
mi_cuenta.mostrar_saldo()

# Ejemplo 3.2: Clase 'Coche' con métodos que modifican su estado
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
        self.velocidad = 0

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"El {self.marca} {self.modelo} ha sido encendido.")
        else:
            print("El coche ya está encendido.")

    def acelerar(self, incremento):
        if self.encendido:
            self.velocidad += incremento
            print(f"Acelerando. Velocidad actual: {self.velocidad} km/h.")
        else:
            print("No se puede acelerar, el coche está apagado.")

    def frenar(self, decremento):
        if self.velocidad - decremento >= 0:
            self.velocidad -= decremento
        else:
            self.velocidad = 0
        print(f"Frenando. Velocidad actual: {self.velocidad} km/h.")

mi_coche = Coche("Toyota", "Corolla")
mi_coche.acelerar(50) # No funciona, está apagado
mi_coche.encender()
mi_coche.acelerar(50)
mi_coche.frenar(20)


# =============================================================================
# 4. LOS 4 PILARES DE LA POO
# =============================================================================

# -----------------------------------------------------------------------------
# 4.1. ENCAPSULAMIENTO
# -----------------------------------------------------------------------------
print("\n--- 4.1. Encapsulamiento ---")

# Explicación 4.1.1: Ocultación de Información
# El encapsulamiento consiste en agrupar datos (atributos) y los métodos que
# operan sobre esos datos dentro de una misma unidad (la clase). Además, restringe
# el acceso directo a algunos de los componentes del objeto. Es como una cápsula
# que protege el estado interno del objeto de manipulaciones indebidas.

# Explicación 4.1.2: Convenciones de Visibilidad en Python
# Python no tiene palabras clave como `private` o `public` (como Java o C++).
# En su lugar, usa convenciones de nomenclatura:
# - `nombre`: Atributo/método público. Accesible desde cualquier lugar.
# - `_nombre`: Atributo/método "protegido". Indica que no debe ser accedido
#              desde fuera de la clase o sus subclases, pero no hay una
#              restricción real. Es una advertencia para el programador.
# - `__nombre`: Atributo/método "privado". Python realiza un proceso llamado
#               "Name Mangling", cambiando el nombre a `_Clase__nombre`. Esto
#               dificulta (pero no imposibilita) su acceso desde fuera.

# Explicación 4.1.3: Getters y Setters
# Para permitir un acceso controlado a los atributos "privados", se utilizan
# métodos públicos:
# - Getters: Métodos para obtener el valor de un atributo (ej. `get_nombre()`).
# - Setters: Métodos para establecer el valor de un atributo, a menudo con
#            lógica de validación (ej. `set_nombre(nuevo_valor)`).

# Ejemplo 4.1.1: Clase 'Empleado' con diferentes niveles de acceso
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre          # Público
        self._id_empleado = "E" + str(hash(nombre)) # Protegido
        self.__salario = salario      # Privado

    def mostrar_info_publica(self):
        print(f"Nombre: {self.nombre}")

    def _generar_reporte_interno(self):
        print(f"Reporte para empleado ID: {self._id_empleado}")

    def __calcular_impuestos(self):
        return self.__salario * 0.20

    def obtener_salario_con_impuestos(self):
        impuestos = self.__calcular_impuestos()
        print(f"El salario de {self.nombre} es confidencial.")
        print(f"Impuestos a pagar: ${impuestos}")

emp = Empleado("Ana López", 50000)
print(f"Nombre público: {emp.nombre}")
# Acceso a un atributo protegido (posible, pero no recomendado)
print(f"ID protegido: {emp._id_empleado}")

# Intentar acceder a un atributo privado directamente dará un error
try:
    print(emp.__salario)
except AttributeError as e:
    print(f"Error esperado: {e}")

# El acceso "privado" es posible a través del "name mangling" (no hacer esto en producción)
print(f"Salario accedido con name mangling: {emp._Empleado__salario}")

# Usamos métodos públicos para interactuar con datos privados
emp.obtener_salario_con_impuestos()

# Ejemplo 4.1.2: Uso de Getters y Setters para validación
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.__precio = 0 # Inicializamos como privado
        self.set_precio(precio) # Usamos el setter en el constructor

    # Getter para el precio
    def get_precio(self):
        return self.__precio

    # Setter para el precio con validación
    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("Error: El precio debe ser un valor positivo.")

prod = Producto("Laptop", 1200)
print(f"Precio inicial: ${prod.get_precio()}")

prod.set_precio(-50) # Intento de poner un precio inválido
print(f"Precio después de intento inválido: ${prod.get_precio()}")

prod.set_precio(1100) # Precio válido
print(f"Precio final: ${prod.get_precio()}")


# -----------------------------------------------------------------------------
# 4.2. HERENCIA
# -----------------------------------------------------------------------------
print("\n--- 4.2. Herencia ---")

# Explicación 4.2.1: Reutilización de Código
# La herencia permite que una clase (llamada 'clase hija' o 'subclase') adquiera
# los atributos y métodos de otra clase (llamada 'clase padre' o 'superclase').
# Esto promueve la reutilización de código y establece una relación "es un"
# (ej. un Perro "es un" Animal).

# Explicación 4.2.2: Sintaxis y `super()`
# Para heredar, se pone el nombre de la clase padre entre paréntesis después del
# nombre de la clase hija. Dentro de la clase hija, se puede usar la función
# `super()` para llamar a métodos de la clase padre, especialmente útil en el
# constructor `__init__` para inicializar los atributos heredados.

# Explicación 4.2.3: Sobrescritura de Métodos (Method Overriding)
# Una clase hija puede proporcionar una implementación específica de un método
# que ya está definido en su clase padre. Esto se llama sobrescritura. Permite
# a la subclase adaptar el comportamiento heredado a sus necesidades.

# Ejemplo 4.2.1: Herencia simple
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        raise NotImplementedError("La subclase debe implementar este método")

    def moverse(self):
        print("Este animal se mueve.")

class Perro(Animal): # Perro hereda de Animal
    def hablar(self): # Sobrescribe el método hablar
        return "¡Guau!"

class Gato(Animal): # Gato hereda de Animal
    def hablar(self): # Sobrescribe el método hablar
        return "¡Miau!"

mi_perro = Perro("Fido")
mi_gato = Gato("Misi")

print(f"{mi_perro.nombre} dice: {mi_perro.hablar()}")
mi_perro.moverse() # Llama al método heredado de Animal

print(f"{mi_gato.nombre} dice: {mi_gato.hablar()}")
mi_gato.moverse()

# Ejemplo 4.2.2: Uso de `super()` y extensión de métodos
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def mostrar_info(self):
        return f"Marca: {self.marca}"

class CocheElectrico(Vehiculo):
    def __init__(self, marca, autonomia):
        # Llama al __init__ de la clase padre (Vehiculo) para establecer la marca
        super().__init__(marca)
        # Añade un nuevo atributo específico de CocheElectrico
        self.autonomia = autonomia

    # Sobrescribe y extiende el método mostrar_info
    def mostrar_info(self):
        # Llama al método original del padre y añade más información
        info_padre = super().mostrar_info()
        return f"{info_padre}, Autonomía: {self.autonomia} km"

mi_tesla = CocheElectrico("Tesla", 500)
print(f"\nInformación del coche eléctrico: {mi_tesla.mostrar_info()}")

# Ejemplo 4.2.3: Herencia Múltiple y Orden de Resolución de Métodos (MRO)
# Una clase puede heredar de varias clases padre. Python busca los métodos
# en un orden específico (MRO): primero en la clase actual, luego en las clases
# padre de izquierda a derecha, y luego en los ancestros de esas clases.

class Pinguino(Animal):
    def hablar(self):
        return "Sonido de pingüino"

class AveVoladora:
    def volar(self):
        print("Estoy volando.")

class Pato(Animal, AveVoladora): # Hereda de Animal y AveVoladora
    def hablar(self):
        return "¡Cuac!"

pato_lucas = Pato("Lucas")
print(f"\n{pato_lucas.nombre} dice: {pato_lucas.hablar()}")
pato_lucas.moverse() # Heredado de Animal
pato_lucas.volar()   # Heredado de AveVoladora

# Puedes ver el MRO de una clase
print(f"MRO de Pato: {Pato.mro()}")


# -----------------------------------------------------------------------------
# 4.3. POLIMORFISMO
# -----------------------------------------------------------------------------
print("\n--- 4.3. Polimorfismo ---")

# Explicación 4.3.1: "Muchas Formas"
# Polimorfismo significa "muchas formas". En POO, se refiere a la capacidad de
# objetos de diferentes clases de responder al mismo mensaje (llamada de método).
# Permite tratar a objetos de tipos distintos de la misma manera.

# Explicación 4.3.2: Duck Typing
# Python utiliza un concepto llamado "Duck Typing" (tipado de pato): "Si camina
# como un pato y grazna como un pato, entonces debe ser un pato". Esto significa
# que no importa la clase del objeto, sino los métodos que tiene. Si un objeto
# tiene el método `hablar()`, podemos llamarlo, sin importar si es un `Perro` o
# un `Pato`.

# Explicación 4.3.3: Polimorfismo con Herencia
# El polimorfismo se logra comúnmente a través de la herencia, donde múltiples
# subclases sobrescriben un método de la superclase. Una función puede entonces
# trabajar con cualquier objeto que herede de esa superclase, confiando en que
# cada objeto implementará el método a su manera.

# Ejemplo 4.3.1: Polimorfismo con una función (Duck Typing)
# La función `hacer_hablar` no se preocupa por el tipo de `animal`, solo
# por si tiene un método `hablar()`.
def hacer_hablar(animal):
    print(animal.hablar())

# Usamos los objetos creados en la sección de herencia
hacer_hablar(mi_perro)
hacer_hablar(mi_gato)
hacer_hablar(pato_lucas)

# Ejemplo 4.3.2: Polimorfismo en un bucle
documentos = [
    {"tipo": "pdf", "contenido": "Texto del PDF"},
    {"tipo": "word", "contenido": "Texto del Word"},
]

class LectorPDF:
    def leer(self, documento):
        print(f"Leyendo PDF: {documento['contenido']}")

class LectorWord:
    def leer(self, documento):
        print(f"Leyendo Word: {documento['contenido']}")

# Creamos instancias de los lectores
lector_pdf = LectorPDF()
lector_word = LectorWord()

# Un diccionario para mapear tipos a lectores
lectores = {"pdf": lector_pdf, "word": lector_word}

# Bucle polimórfico
for doc in documentos:
    lector = lectores[doc["tipo"]]
    lector.leer(doc) # La misma llamada `leer` funciona para diferentes objetos


# -----------------------------------------------------------------------------
# 4.4. ABSTRACCIÓN
# -----------------------------------------------------------------------------
print("\n--- 4.4. Abstracción ---")

# Explicación 4.4.1: Ocultar la Complejidad
# La abstracción consiste en ocultar los detalles complejos de implementación y
# mostrar solo la funcionalidad esencial al usuario. Una clase abstracta define
# una interfaz común para un grupo de subclases, obligándolas a implementar
# ciertos métodos, pero sin decirles *cómo* hacerlo.

# Explicación 4.4.2: Clases Base Abstractas (ABC)
# En Python, la abstracción se implementa usando el módulo `abc` (Abstract Base
# Classes). Una clase que hereda de `ABC` se convierte en una clase abstracta.
# No se pueden crear instancias de una clase abstracta.

# Explicación 4.4.3: Métodos Abstractos
# Usando el decorador `@abstractmethod`, podemos definir métodos que las subclases
# *deben* implementar. Si una subclase no implementa todos los métodos abstractos
# de su padre, también se convierte en abstracta y no puede ser instanciada.

# Ejemplo 4.4.1: Definiendo una Clase Base Abstracta
from abc import ABC, abstractmethod

class FormaGeometrica(ABC): # Hereda de ABC para ser abstracta
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod # Declara este método como abstracto
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass

    def describir(self):
        print(f"Soy una forma geométrica llamada {self.nombre}")

# No podemos instanciar una clase abstracta
try:
    forma = FormaGeometrica("forma")
except TypeError as e:
    print(f"Error esperado: {e}")

# Ejemplo 4.4.2: Implementando la clase abstracta
class Circulo(FormaGeometrica):
    def __init__(self, nombre, radio):
        super().__init__(nombre)
        self.radio = radio

    # Debemos implementar todos los métodos abstractos
    def calcular_area(self):
        return 3.14159 * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * 3.14159 * self.radio

class Rectangulo(FormaGeometrica):
    def __init__(self, nombre, base, altura):
        super().__init__(nombre)
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

# Ahora sí podemos crear instancias de las clases concretas
mi_circulo = Circulo("Círculo 1", 10)
mi_rectangulo = Rectangulo("Rectángulo A", 5, 4)

formas = [mi_circulo, mi_rectangulo]

# Usando polimorfismo con la abstracción
for forma in formas:
    forma.describir()
    print(f"Área: {forma.calcular_area():.2f}")
    print(f"Perímetro: {forma.calcular_perimetro():.2f}\n")


# =============================================================================
# 5. CONCEPTOS AVANZADOS
# =============================================================================

# -----------------------------------------------------------------------------
# 5.1. MÉTODOS ESPECIALES (DUNDER METHODS)
# -----------------------------------------------------------------------------
print("\n--- 5.1. Métodos Especiales (Dunder Methods) ---")

# Explicación 5.1.1: Comportamiento Integrado
# Los métodos Dunder (Double Underscore) permiten que nuestros objetos se integren
# con el comportamiento nativo de Python. Por ejemplo, podemos definir qué sucede
# cuando usamos el operador `+` con nuestros objetos, o cuando llamamos a `len()`
# sobre ellos.

# Explicación 5.1.2: Representación de Objetos
# - `__str__`: Devuelve una representación "amigable" del objeto en forma de string,
#   para ser mostrada al usuario final. Es lo que llama `print()`.
# - `__repr__`: Devuelve una representación "inequívoca" del objeto, que idealmente
#   debería ser código Python válido para recrear el objeto. Es para los desarrolladores.
# Si `__str__` no está definido, `print()` usará `__repr__`.

# Explicación 5.1.3: Emulación de Tipos Numéricos y de Colección
# - Comparación: `__eq__` (==), `__ne__` (!=), `__lt__` (<), `__gt__` (>), etc.
# - Aritmética: `__add__` (+), `__sub__` (-), `__mul__` (*), etc.
# - Colecciones: `__len__` (len()), `__getitem__` (obj[key]), `__setitem__` (obj[key] = val).

# Ejemplo 5.1.1: `__str__` y `__repr__`
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # Representación para desarrolladores
        return f"Vector2D({self.x}, {self.y})"

    def __str__(self):
        # Representación para usuarios
        return f"({self.x}, {self.y})"

    # Ejemplo 5.1.2: Sobrecarga de operadores
    def __add__(self, otro_vector):
        # Define el comportamiento del operador '+'
        if isinstance(otro_vector, Vector2D):
            return Vector2D(self.x + otro_vector.x, self.y + otro_vector.y)
        return NotImplemented

    def __eq__(self, otro_vector):
        # Define el comportamiento del operador '=='
        if isinstance(otro_vector, Vector2D):
            return self.x == otro_vector.x and self.y == otro_vector.y
        return False

v1 = Vector2D(2, 3)
v2 = Vector2D(5, 1)

print(f"Usando print (llama a __str__): {v1}")
print(f"Mostrando en consola (llama a __repr__): {[v1, v2]}")
print(f"Resultado de v1 + v2 (llama a __add__): {v1 + v2}")

v3 = Vector2D(2, 3)
print(f"¿Es v1 igual a v2? (llama a __eq__): {v1 == v2}")
print(f"¿Es v1 igual a v3? (llama a __eq__): {v1 == v3}")

# Ejemplo 5.1.3: Emulando una colección
class CarritoDeCompras:
    def __init__(self):
        self._productos = {} # {nombre: cantidad}

    def agregar(self, producto, cantidad=1):
        self._productos[producto] = self._productos.get(producto, 0) + cantidad

    def __len__(self):
        # Define el comportamiento de len()
        return sum(self._productos.values())

    def __getitem__(self, producto):
        # Define el acceso con []
        return self._productos.get(producto, 0)

carrito = CarritoDeCompras()
carrito.agregar("Manzana", 5)
carrito.agregar("Leche", 2)

print(f"\nTotal de ítems en el carrito (usa __len__): {len(carrito)}")
print(f"Cantidad de manzanas (usa __getitem__): {carrito['Manzana']}")
print(f"Cantidad de pan (usa __getitem__): {carrito['Pan']}")


# -----------------------------------------------------------------------------
# 5.2. DECORADORES EN CLASES
# -----------------------------------------------------------------------------
print("\n--- 5.2. Decoradores en Clases ---")

# Explicación 5.2.1: `@property` (Pythonic Getters/Setters)
# El decorador `@property` permite tratar un método como si fuera un atributo.
# Esto crea un "getter" de una forma más limpia y pythonica. Se puede combinar
# con `@nombre.setter` y `@nombre.deleter` para un control total, manteniendo
# la sintaxis de acceso a atributos.

# Explicación 5.2.2: `@classmethod`
# Un método de clase recibe la clase misma como primer argumento, no la instancia.
# Por convención, este argumento se llama `cls`. Son útiles para crear métodos
# "fábrica" que construyen instancias de la clase de formas alternativas.

# Explicación 5.2.3: `@staticmethod`
# Un método estático no recibe ningún primer argumento especial (ni `self` ni `cls`).
# Es esencialmente una función normal que vive dentro del namespace de la clase.
# Se usa cuando una funcionalidad está relacionada con la clase, pero no depende
# de ningún estado de la clase o de la instancia.

# Ejemplo 5.2.1: Uso de @property
class Persona:
    def __init__(self, nombre, anio_nacimiento):
        self.nombre = nombre
        self._anio_nacimiento = anio_nacimiento

    @property
    def edad(self):
        # Este método se accede como un atributo: persona.edad
        from datetime import date
        return date.today().year - self._anio_nacimiento

p = Persona("Carlos", 1990)
# Accedemos a `edad` como si fuera un atributo, no un método
print(f"{p.nombre} tiene {p.edad} años.")

# Ejemplo 5.2.2: @classmethod como método fábrica
class Fecha:
    def __init__(self, dia, mes, anio):
        self.dia = dia
        self.mes = mes
        self.anio = anio

    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.anio}"

    @classmethod
    def desde_string(cls, fecha_string): # "cls" es la clase Fecha
        # Crea una instancia de Fecha a partir de un string "dd-mm-yyyy"
        dia, mes, anio = map(int, fecha_string.split('-'))
        return cls(dia, mes, anio) # Llama al constructor de la clase

fecha_normal = Fecha(15, 9, 2023)
fecha_desde_str = Fecha.desde_string("25-12-2024")

print(f"\nFecha creada normalmente: {fecha_normal}")
print(f"Fecha creada con classmethod: {fecha_desde_str}")

# Ejemplo 5.2.3: @staticmethod para una función de utilidad
class ValidadorMatematico:
    @staticmethod
    def es_primo(n):
        # Esta función no necesita estado de clase o instancia
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

print(f"\n¿Es 7 primo? {ValidadorMatematico.es_primo(7)}")
print(f"¿Es 10 primo? {ValidadorMatematico.es_primo(10)}")


# -----------------------------------------------------------------------------
# 5.3. DATA CLASSES
# -----------------------------------------------------------------------------
print("\n--- 5.3. Data Classes ---")

# Explicación 5.3.1: Reducción de Código Repetitivo
# A menudo, creamos clases que principalmente sirven para almacenar datos.
# Para estas clases, solemos escribir manualmente `__init__`, `__repr__`, `__eq__`, etc.
# El decorador `@dataclass` (del módulo `dataclasses`) genera automáticamente
# estos métodos basándose en las anotaciones de tipo de los atributos.

# Explicación 5.3.2: Funcionalidades Automáticas
# Por defecto, `@dataclass` genera:
# - `__init__`: Un constructor que acepta todos los campos definidos.
# - `__repr__`: Una representación útil para depuración.
# - `__eq__`: Compara si dos instancias son iguales campo por campo.
# - Opcionalmente puede generar `__lt__`, `__le__`, `__gt__`, `__ge__` si se
#   especifica `order=True`.

# Explicación 5.3.3: Personalización
# Se pueden establecer valores por defecto y usar la función `field()` para
# configurar opciones avanzadas por cada atributo, como excluir un campo de
# la comparación o del `__repr__`.

from dataclasses import dataclass, field

# Ejemplo 5.3.1: Clase tradicional vs. Data Class
# Forma tradicional
class InventarioItemTradicional:
    def __init__(self, nombre: str, precio_unitario: float, cantidad: int = 0):
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.cantidad = cantidad

    def __repr__(self):
        return (f"InventarioItemTradicional(nombre='{self.nombre}', "
                f"precio_unitario={self.precio_unitario}, cantidad={self.cantidad})")

    def __eq__(self, other):
        if not isinstance(other, InventarioItemTradicional):
            return NotImplemented
        return (self.nombre == other.nombre and
                self.precio_unitario == other.precio_unitario and
                self.cantidad == other.cantidad)

# Forma moderna con @dataclass
@dataclass(order=True) # order=True genera métodos de comparación (<, >, etc.)
class InventarioItem:
    nombre: str
    precio_unitario: float
    # `field` permite configurar opciones, como un valor por defecto
    cantidad: int = field(default=0, compare=False) # No usar cantidad para ordenar

    def valor_total(self) -> float:
        return self.precio_unitario * self.cantidad

item1 = InventarioItem("Tornillo", 0.10, 100)
item2 = InventarioItem("Tornillo", 0.10, 100)
item3 = InventarioItem("Tuerca", 0.15)

print(f"\nRepresentación de Data Class: {item1}")
print(f"¿item1 == item2? {item1 == item2}") # True, gracias a __eq__ autogenerado
print(f"Valor total de item1: {item1.valor_total()}")

item4 = InventarioItem("Arandela", 0.05, 50)
# La comparación funciona porque pusimos order=True
print(f"¿item4 < item1? {item4 < item1}") # Compara por nombre, luego por precio


# -----------------------------------------------------------------------------
# 5.4. METACLASES
# -----------------------------------------------------------------------------
print("\n--- 5.4. Metaclases ---")

# Explicación 5.4.1: Clases que Crean Clases
# Este es el concepto más avanzado de la POO en Python. Una metaclass es una
# "clase de una clase". Así como una clase es una plantilla para crear objetos,
# una metaclass es una plantilla para crear clases.

# Explicación 5.4.2: `type` como Metaclass por Defecto
# En Python, las clases son objetos en sí mismas. El tipo de un objeto es su clase.
# El tipo de una clase es su metaclass. La metaclass por defecto es `type`.
# `type` puede usarse de dos formas:
# 1. `type(obj)`: Devuelve el tipo de un objeto.
# 2. `type(name, bases, attrs)`: Crea una nueva clase dinámicamente.
#    - `name`: Nombre de la clase (string).
#    - `bases`: Tupla de clases base.
#    - `attrs`: Diccionario de atributos y métodos.

# Explicación 5.4.3: Creando una Metaclass Personalizada
# Para crear una metaclass, se define una clase que hereda de `type`. Dentro de
# esta metaclass, se puede personalizar el proceso de creación de la clase
# sobrescribiendo el método `__new__` o `__init__`. Esto permite inyectar
# métodos, verificar atributos, registrar clases, etc., en el momento en que
# se define una clase.

# Ejemplo 5.4.1: `type` en acción
# Definiendo una clase de la forma tradicional
class MiClase:
    x = 10
    def mi_metodo(self):
        return "hola"

print(f"\nTipo de un objeto: {type(MiClase())}")
print(f"Tipo de una clase: {type(MiClase)}") # Es 'type', la metaclass por defecto

# Creando la misma clase dinámicamente con `type`
def mi_metodo_func(self):
    return "hola"

MiClaseDinamica = type(
    'MiClaseDinamica', # Nombre de la clase
    (),                # Clases base (ninguna)
    {'x': 10, 'mi_metodo': mi_metodo_func} # Atributos y métodos
)

obj_dinamico = MiClaseDinamica()
print(f"Clase creada dinámicamente: {obj_dinamico.x}, {obj_dinamico.mi_metodo()}")

# Ejemplo 5.4.2: Una metaclass para asegurar que las subclases tengan ciertos atributos
# Esta metaclass verificará que cualquier clase que la use defina un atributo `descripcion`.
class MetaAseguraDescripcion(type):
    def __new__(cls, name, bases, attrs):
        print(f"Creando la clase '{name}' usando MetaAseguraDescripcion...")
        if 'descripcion' not in attrs or not attrs['descripcion']:
            raise TypeError(f"La clase {name} debe definir un atributo 'descripcion'.")
        return super().__new__(cls, name, bases, attrs)

# Usamos la metaclass en una clase
class ClaseConDescripcion(metaclass=MetaAseguraDescripcion):
    descripcion = "Esta es una clase de ejemplo."

    def __init__(self):
        pass

print("Clase 'ClaseConDescripcion' creada exitosamente.")

# Esta definición fallará porque no tiene el atributo 'descripcion'
try:
    class ClaseSinDescripcion(metaclass=MetaAseguraDescripcion):
        pass
except TypeError as e:
    print(f"Error esperado al crear la clase: {e}")

# Ejemplo 5.4.3: Metaclass para registrar plugins
# Esta metaclass registrará todas las clases que la usen en un diccionario.
class MetaPlugin(type):
    _plugins = {} # Registro de plugins

    def __new__(cls, name, bases, attrs):
        nueva_clase = super().__new__(cls, name, bases, attrs)
        # No registrar la clase base del plugin
        if name != 'PluginBase':
            print(f"Registrando plugin: {name}")
            cls._plugins[name.lower()] = nueva_clase
        return nueva_clase

class PluginBase(metaclass=MetaPlugin):
    @abstractmethod
    def ejecutar(self):
        pass

class PluginSuma(PluginBase):
    def ejecutar(self, a, b):
        return a + b

class PluginResta(PluginBase):
    def ejecutar(self, a, b):
        return a - b

def ejecutar_plugin(nombre_plugin, a, b):
    if nombre_plugin in MetaPlugin._plugins:
        plugin_clase = MetaPlugin._plugins[nombre_plugin]
        plugin_instancia = plugin_clase()
        return plugin_instancia.ejecutar(a, b)
    else:
        raise ValueError(f"Plugin '{nombre_plugin}' no encontrado.")

print(f"\nResultado de 'suma': {ejecutar_plugin('suma', 10, 5)}")
print(f"Resultado de 'resta': {ejecutar_plugin('resta', 10, 5)}")

print("\n--- Fin del Tutorial de POO en Python ---")
