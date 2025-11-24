# ===-----------------------------------------------------------------------===##
#
#  3.4 Metaclases en Python
#
#  Las metaclases son uno de los conceptos más avanzados y poderosos de Python.
#  Para entenderlas, primero debemos recordar un principio fundamental en Python:
#  "Todo es un objeto".
#
#  Esto incluye números, strings, funciones y... clases.
#
#===-----------------------------------------------------------------------===#


# --- Parte 1: Las clases son objetos ---

# En Python, una clase no es solo una plantilla para crear objetos. La clase
# en sí misma es un objeto. Y si es un objeto, significa que fue creada a partir
# de una clase.
#
# ¿Cuál es la "clase" de una clase? Es una METACLASE.

# La metaclase por defecto en Python es `type`.

class MiClase:
    pass

# Creamos una instancia de MiClase
mi_instancia = MiClase()

# Usemos la función `type()` para ver de qué "clase" son estos objetos.
print(f"El tipo de mi_instancia es: {type(mi_instancia)}")
print(f"El tipo de la clase MiClase es: {type(MiClase)}")

# Como puedes ver, el tipo de `mi_instancia` es `MiClase`.
# Pero el tipo de `MiClase` es `type`. ¡`type` es una metaclase!


# --- Parte 2: Creando clases dinámicamente con `type` ---

# La función `type()` tiene una segunda funcionalidad: puede crear clases
# sobre la marcha. La sintaxis es:
#
#   type('NombreDeLaClase', (ClasesBase,), {'atributo': valor})
#
# 1. NombreDeLaClase: Un string con el nombre que tendrá la nueva clase.
# 2. ClasesBase: Una tupla de las clases de las que heredará (puede estar vacía).
# 3. Atributos: Un diccionario que contiene los atributos y métodos de la clase.

def mi_metodo_dinamico(self):
    print(f"Hola, soy un método en una clase creada dinámicamente. Mi atributo es {self.atributo}")

# Usamos `type` para crear una clase llamada `MiClaseDinamica`
MiClaseDinamica = type(
    'MiClaseDinamica',
    (),  # No hereda de ninguna otra clase
    {
        'atributo': 100,
        'mi_metodo': mi_metodo_dinamico
    }
)

# Ahora podemos usar esta clase como cualquier otra
instancia_dinamica = MiClaseDinamica()
print(f"\nAtributo de la clase dinámica: {instancia_dinamica.atributo}")
instancia_dinamica.mi_metodo()

print(f"El tipo de MiClaseDinamica es: {type(MiClaseDinamica)}")


# --- Parte 3: Creando una Metaclase Personalizada ---

# Si podemos crear clases con `type`, podemos personalizar CÓMO se crean las clases.
# Para ello, creamos una clase que herede de `type` y sobreescribimos sus métodos,
# principalmente `__new__`.
#
# El método `__new__` de una metaclase se ejecuta ANTES de que la clase sea creada.
# Recibe los mismos argumentos que `type()`:
#   - cls: La propia metaclase.
#   - name: El nombre de la clase que se está creando.
#   - bases: La tupla de clases base.
#   - attrs: El diccionario de atributos y métodos.

# **Ejemplo 1: Una metaclase que convierte todos los nombres de atributos a mayúsculas.**

class MetaclaseMayusculas(type):
    def __new__(cls, name, bases, attrs):
        print("\n--- Ejecutando __new__ de MetaclaseMayusculas ---")
        print(f"Creando la clase: {name}")

        # Creamos un nuevo diccionario de atributos con claves en mayúsculas
        nuevos_attrs = {}
        for attr_name, attr_value in attrs.items():
            # No convertimos los métodos especiales (dunder)
            if not attr_name.startswith('__'):
                nuevos_attrs[attr_name.upper()] = attr_value
            else:
                nuevos_attrs[attr_name] = attr_value
        
        print(f"Atributos originales: {attrs.keys()}")
        print(f"Nuevos atributos: {nuevos_attrs.keys()}")

        # Llamamos al `__new__` de la clase `type` para que realmente cree la clase
        # con los atributos modificados.
        return super().__new__(cls, name, bases, nuevos_attrs)

# Ahora, para usar nuestra metaclase, usamos el argumento `metaclass` en la definición
# de nuestra clase.

class Persona(metaclass=MetaclaseMayusculas):
    nombre = "Juan"
    edad = 30

    def saludar(self):
        # Nótese que dentro de la clase, accedemos a los atributos en mayúsculas
        print(f"Hola, mi nombre es {self.NOMBRE} y tengo {self.EDAD} años.")

# Al crear la clase `Persona`, Python vio `metaclass=MetaclaseMayusculas` y usó
# nuestra metaclase para construirla. El método `__new__` se ejecutó y cambió
# 'nombre' por 'NOMBRE' y 'edad' por 'EDAD'.

p = Persona()

# Si intentamos acceder a `p.nombre` (en minúsculas), dará un error.
try:
    print(p.nombre)
except AttributeError as e:
    print(f"Error esperado: {e}")

# Debemos usar los nombres en mayúsculas.
print(f"Atributo NOMBRE: {p.NOMBRE}")
print(f"Atributo EDAD: {p.EDAD}")
p.saludar()


# --- Parte 4: Casos de Uso Prácticos para Metaclases ---

# Las metaclases son útiles para realizar acciones automáticas en la creación de clases.
# Son la base de muchos frameworks como Django (para sus modelos ORM) o SQLAlchemy.

# **Ejemplo 2: Metaclase para registrar clases (Patrón de Registro)**
# Imaginemos que queremos mantener un registro de todas las clases de "plugins"
# que se crean en nuestro programa.

class RegistroPlugins(type):
    # Usaremos un diccionario en la metaclase para guardar las clases creadas
    plugins_registrados = {}

    def __new__(cls, name, bases, attrs):
        # Creamos la nueva clase usando el método de la superclase `type`
        nueva_clase = super().__new__(cls, name, bases, attrs)
        
        # Si la clase tiene un atributo `plugin_id`, la registramos
        if 'plugin_id' in attrs:
            plugin_id = attrs['plugin_id']
            print(f"\nRegistrando plugin: '{name}' con ID: '{plugin_id}'")
            cls.plugins_registrados[plugin_id] = nueva_clase
        
        return nueva_clase

# Creamos una clase base que usará nuestra metaclase
class PluginBase(metaclass=RegistroPlugins):
    pass

# Ahora, cualquier clase que herede de `PluginBase` será procesada por `RegistroPlugins`.

class PluginEmail(PluginBase):
    plugin_id = "email_sender"
    def ejecutar(self, mensaje):
        print(f"Enviando email: {mensaje}")

class PluginSMS(PluginBase):
    plugin_id = "sms_sender"
    def ejecutar(self, mensaje):
        print(f"Enviando SMS: {mensaje}")

class ClaseCualquiera: # Esta no hereda de PluginBase, por lo que no se registrará
    pass

# Ahora podemos ver nuestro registro de plugins
print("\nPlugins disponibles en el registro:")
print(RegistroPlugins.plugins_registrados)

# Y podemos usarlo para instanciar plugins dinámicamente
plugin_id_a_usar = "email_sender"
plugin_clase = RegistroPlugins.plugins_registrados[plugin_id_a_usar]
plugin_instancia = plugin_clase()
plugin_instancia.ejecutar("¡Hola desde el registro de plugins!")


# **Conclusión:**
#
# - **¿Qué son?** Las metaclases son las "clases de las clases". Definen cómo se
#   comportan y cómo se crean las clases.
# - **¿Para qué sirven?** Permiten modificar o inspeccionar una clase en el momento
#   de su creación. Esto es útil para:
#     - Registrar clases automáticamente (como en el ejemplo de plugins).
#     - Validar que una clase cumpla ciertas reglas (p.ej., que todos sus métodos
#       tengan docstrings).
#     - Inyectar atributos o métodos automáticamente.
#     - Implementar APIs complejas como los ORM (Object-Relational Mapping).
#
# Son una herramienta muy poderosa, pero también compleja. En la mayoría de los casos,
# no necesitarás escribir tus propias metaclases. A menudo, los decoradores de clase
# o la herencia simple pueden resolver el problema de una manera más sencilla.
# Sin embargo, entenderlas te da una visión mucho más profunda de cómo funciona
# la POO en Python.
