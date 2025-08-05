class Libro:
    def __init__(self, titulo, autor, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.__prestado = False
        self.__cantidad_prestamos = 0

        if numero_paginas < 10:
            self.__numero_paginas = 10
            print(f"🚨 Advertencia: El número de páginas para '{self.titulo}' se ha ajustado a 10, ya que era menor que 10.")
        else:
            self.__numero_paginas = numero_paginas

    def prestar(self):
        if not self.__prestado:
            self.__prestado = True
            self.__cantidad_prestamos += 1
            print(f"'{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' ya ha sido prestado.")

    def devolver(self):
        if self.__prestado:
            self.__prestado = False
            print(f"'{self.titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' no estaba prestado.")

    def mostrar_detalles(self):
        estado_prestamo = "Sí" if self.__prestado else "No"
        print("\n--- Detalles del Libro ---")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Número de páginas: {self.__numero_paginas}")
        print(f"Prestado: {estado_prestamo}")
        print(f"Cantidad de préstamos realizados: {self.__cantidad_prestamos}")
        print("--------------------------")

# --- Ejemplo de Uso ---
if __name__ == "__main__":
    # Creamos algunos libros
    libro1 = Libro("El Legado del Hechicero", "Elara Vancroft", 280)
    libro2 = Libro("Secretos Olvidados de la Alquimia", "Magnus Corvus", 7) # Activa la advertencia
    libro3 = Libro("Conjuros para el Viajero Novato", "Lyra Estrellada", 150)

    print("--- Estado Inicial ---")
    libro1.mostrar_detalles()
    libro2.mostrar_detalles()

    print("\n--- Operaciones de Préstamo y Devolución ---")
    libro1.prestar()
    libro1.mostrar_detalles()
    libro1.prestar() # Intentamos prestarlo de nuevo

    libro2.devolver() # Intentamos devolver un libro no prestado

    libro3.prestar()
    libro3.prestar() # Prestamos el mismo libro varias veces
    libro3.devolver()
    libro3.mostrar_detalles()

    print("\n--- Estado Final ---")
    libro1.mostrar_detalles()
    libro2.mostrar_detalles()
    libro3.mostrar_detalles()