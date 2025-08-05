class Libro:
    def __init__(self, titulo, autor, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        if numero_paginas < 10:
            print("🚨 Advertencia: El número de páginas era menor que 10. Se ajusta a 10.")
            self.__numero_paginas = 10
        else:
            self.__numero_paginas = numero_paginas
        self.__prestado = False
        self.__cantidad_prestamos = 0

    def prestar(self):
        if not self.__prestado:
            self.__prestado = True
            self.__cantidad_prestamos += 1
            print("El libro ha sido prestado.")
        else:
            print("El libro ya ha sido prestado.")

    def devolver(self):
        if self.__prestado:
            self.__prestado = False
            print("El libro ha sido devuelto.")
        else:
            print("El libro no estaba prestado.")

    def mostrar_detalles(self):
        estado = "Prestado" if self.__prestado else "Disponible"
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Número de páginas: {self.__numero_paginas}")
        print(f"Estado: {estado}")
        print(f"Cantidad de préstamos: {self.__cantidad_prestamos}")


if __name__ == "__main__":
    libro1 = Libro("El Castillo Ambulante", "Diana Wynne Jones", 8)
    while True:
        print("\nOpciones:")
        print("1. Mostrar detalles")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            libro1.mostrar_detalles()
        elif opcion == "2":
            libro1.prestar()
        elif opcion == "3":
            libro1.devolver()
        elif opcion == "4":
            print("¡Hasta luego!")
            break