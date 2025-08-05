class Libro:
    def __init__(self, titulo, autor, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.__prestado = False
        self.__cantidad_prestamos = 10

        if numero_paginas < 10:
            print("Advertencia: El libro tiene menos de 10 páginas. Se ajustará a 10.")
            self.__numero_paginas = 10
        else:
            self.__numero_paginas = numero_paginas

    def prestar(self):
        if not self.__prestado:
            self.__prestado = True
            self.__cantidad_prestamos += 1
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print("El libro ya ha sido prestado.")

    def devolver(self):
        if self.__prestado:
            self.__prestado = False
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print("El libro no estaba prestado.")

    def mostrar_detalles(self):
        print("Detalles del Libro:")
        print(f"  Título: {self.titulo}")
        print(f"  Autor: {self.autor}")
        print(f"  Número de páginas: {self.__numero_paginas}")
        print(f"  Prestado: {'Sí' if self.__prestado else 'No'}")
        print(f"  Veces prestado: {self.__cantidad_prestamos}")

# Ejemplo de uso
libro1 = Libro("Hechizos Antiguos", "Merlín", 8)
libro1.mostrar_detalles()
libro1.prestar()
libro1.prestar()
libro1.devolver()
libro1.devolver()
libro1.mostrar_detalles()
