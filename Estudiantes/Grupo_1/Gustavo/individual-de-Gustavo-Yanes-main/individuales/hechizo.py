class Libro:
    def __init__(self, titulo, autor, numero_paginas):
        self.titulo = titulo  
        self.autor = autor    
        self.__prestado = False  
        self.__cantidad_prestamos = 0  
        if numero_paginas < 10:
            self.__numero_paginas = 10
            print(" Advertencia: El número de páginas era menor a 10. Se ajustó automáticamente a 10.")
        else:
            self.__numero_paginas = numero_paginas

    def prestar(self):
        if not self.__prestado:
            self.__prestado = True
            self.__cantidad_prestamos += 1
            print(" El libro ha sido prestado exitosamente.")
        else:
            print(" El libro ya ha sido prestado.")

    def devolver(self):
        if self.__prestado:
            self.__prestado = False
            print(" El libro ha sido devuelto correctamente.")
        else:
            print(" El libro no estaba prestado.")

    def mostrar_detalles(self):
        estado = "Prestado" if self.__prestado else "Disponible"
        print("\n Detalles del Libro:")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Número de páginas: {self.__numero_paginas}")
        print(f"Estado: {estado}")
        print(f"Cantidad de veces prestado: {self.__cantidad_prestamos}")


#  Ejemplo de uso
libro_magico = Libro("La Enciclopedia Arcana", "Merlín el Sabio", 8)
libro_magico.mostrar_detalles()
libro_magico.prestar()
libro_magico.prestar()
libro_magico.devolver()
libro_magico.devolver()
libro_magico.mostrar_detalles()


