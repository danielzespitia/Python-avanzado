class Libro:
    def __init__(self, titulo, autor, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.__prestado = False
        self.__cantidad_prestamos = 0

        if numero_paginas < 10:
            self.__numero_paginas = 10
            print(f"Advertencia: El número de páginas era menor que 10, se ajusta automáticamente a 10.")
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
        estado = "Prestado" if self.__prestado else "Disponible"
        print("Detalles del libro")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Número de páginas: {self.__numero_paginas}")
        print(f"Estado: {estado}")
        print(f"Cantidad de préstamos: {self.__cantidad_prestamos}")