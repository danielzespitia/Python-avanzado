# Polimorfismo
#
# La palabra polimorfismo significa "muchas formas". En POO, se refiere a la capacidad 
# de objetos de diferentes clases
# de responder a la misma llamada de método de manera específica para su clase. En el ejemplo 
# anterior, tanto Gerente
# como Programador tienen un método calcular_salario_mensual(), pero cada uno lo ejecuta de forma diferente.
#
# El polimorfismo permite escribir código más genérico y desacoplado. Puedes tener una función que 
# trabaje con objetos
# de la clase padre, y funcionará correctamente con cualquier objeto de sus clases hijas sin necesidad 
# de saber de qué tipo específico son.
#
# Ejemplo Extendido:
# Usando las clases del ejemplo anterior, podemos crear una función que procese la nómina de todos 
# los empleados, sin importar su cargo.

# (Continuación del código de Empleado, Gerente, Programador)

# Lista de empleados de diferentes tipos (diferentes formas)
class Empleado:
    def __init__(self, nombre, id_empleado, salario_base):
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.salario_base = salario_base

    def calcular_salario_mensual(self):
        return self.salario_base

    def mostrar_ficha(self):
        print(f"--- Ficha de Empleado ---")
        print(f"Nombre: {self.nombre} (ID: {self.id_empleado})")
        print(f"Salario Mensual: ${self.calcular_salario_mensual():,.2f}")

    def mostrar_responsabilidades(self):
        """Método polimórfico: cada clase lo implementará de manera específica"""
        print(f"{self.nombre} - Responsabilidades generales de empleado")


class Gerente(Empleado):
    def __init__(self, nombre, id_empleado, salario_base, bono_gestion):
        super().__init__(nombre, id_empleado, salario_base)
        self.bono_gestion = bono_gestion

    def calcular_salario_mensual(self):
        return super().calcular_salario_mensual() + self.bono_gestion

    def mostrar_responsabilidades(self):
        """Implementación específica para Gerente"""
        print(f"{self.nombre} - Responsabilidades de Gerente:")
        print("  • Supervisar equipos de trabajo")
        print("  • Tomar decisiones estratégicas")
        print("  • Gestionar presupuestos y recursos")


class Programador(Empleado):
    def __init__(self, nombre, id_empleado, salario_base, horas_extra, pago_por_hora):
        super().__init__(nombre, id_empleado, salario_base)
        self.horas_extra = horas_extra
        self.pago_por_hora = pago_por_hora

    def calcular_salario_mensual(self):
        return super().calcular_salario_mensual() + (self.horas_extra * self.pago_por_hora)

    def mostrar_responsabilidades(self):
        """Implementación específica para Programador"""
        print(f"{self.nombre} - Responsabilidades de Programador:")
        print("  • Desarrollar y mantener código")
        print("  • Realizar pruebas de software")
        print("  • Documentar soluciones técnicas")


def procesar_nomina_anual(empleados):
    print("--- PROCESANDO NÓMINA ANUAL ---")
    costo_total_anual = 0
    for emp in empleados:
        salario_anual = emp.calcular_salario_mensual() * 12
        costo_total_anual += salario_anual
        print(f"Empleado: {emp.nombre}, Salario Anual: ${salario_anual:,.2f}")
    print("-" * 30)
    print(f"COSTO TOTAL ANUAL DE LA NÓMINA: ${costo_total_anual:,.2f}")


def mostrar_organigrama(empleados):
    """
    Esta función demuestra el polimorfismo de manera específica para cada clase.
    Llama al método mostrar_responsabilidades() que está implementado de forma
    diferente en cada clase, mostrando el comportamiento específico de cada tipo.
    """
    print("\n--- ORGANIGRAMA Y RESPONSABILIDADES ---")
    for emp in empleados:
        emp.mostrar_responsabilidades()
        print()


empleado_base = Empleado("Carlos Ruiz", "E101", 2000)
gerente_ana = Gerente("Ana López", "G202", 3500, 800)
programador_luis = Programador("Luis Torres", "P303", 2800, 20, 25)

empleado_base.mostrar_ficha()
print()
gerente_ana.mostrar_ficha()
print()
programador_luis.mostrar_ficha()
print()

lista_empleados = [
    empleado_base,
    gerente_ana,
    programador_luis,
    Programador("Maria Sol", "P304", 2800, 10, 25)
]

procesar_nomina_anual(lista_empleados)

# Demostración adicional del polimorfismo: cada objeto responde de manera específica
mostrar_organigrama(lista_empleados)