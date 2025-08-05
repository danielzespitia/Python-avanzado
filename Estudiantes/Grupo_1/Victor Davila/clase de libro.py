class Libro:
    def __init__(self, titulo, autor, __numero_paginas,__prestado= False, __cantidad_prestamo= 10):
     self.titulo = "Titulo"
     self.autor = "Autor"
     self.__numero_paginas = 10

     if __numero_paginas < 10:
        print("Advertencia: El libro tiene menos de 10 paginas. Se ajustara a 10.")
    
    def prestar(self):
        if not self.__prestado:
            self.__prestado=True
            self.__cantidad_prestamo += 1
            print(f"El libro '{self.titulo}' ya ha sido prestado.")

    def devolver(self):
       if self.__prestado:
          self.__prestado=False
          print(f"El libro'{self.titulo}' ya ha sido devuelto.")
       else:
          print("El libro no estaba prestado")

    def mostrar_detalles(self):
       print("Detalles del libro:")
       print(f"Titulo: {self.titulo}")
       print(f"Autor: {self.autor}")
       print(f"Número de paginas: {self.__numero_paginas}")
       print(f"Prestado: {'Si' if self.__prestado else 'No'}")
       print(f"Numero de páginas: {self.__numero_paginas}")
       print(f"Veces prestado: {self.__cantidad_prestamo}")

Libro1 = Libro("Las Gatas programadoras", "El profe", 3)
Libro1.mostrar_detalles()
Libro1.prestar()
Libro1.prestar()
Libro1.devolver()
Libro1.devolver()
Libro1.mostrar_detalles()