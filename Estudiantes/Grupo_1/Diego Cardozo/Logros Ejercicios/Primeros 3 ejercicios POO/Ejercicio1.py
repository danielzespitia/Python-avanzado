class Libro:
    
    __numero_paginas = 0
    __prestado = False
    __cantidad_prestamos = 0
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor
        
    def __str__(self,__numero_paginas,__prestado,__cantidad_prestamos):
        if 10>__numero_paginas:
            __numero_paginas = 10
            print("El numero de paginas debe ser minimo de 10") 
        
        return f"{self.titulo} / {self.autor} / {__numero_paginas} / {__prestado} / {__cantidad_prestamos}"
    
    def prestar(self,__prestado,__cantidad_prestamos):
        if __prestado == False:
            print("El Usuario ha prestado un libro.")
            __cantidad_prestamos += 1
            __prestado == True
        else:
            print("El libro ya esta prestado.")
            
    def devolver(self,__prestado):
        if __prestado == True:
            print("El libro ha sido devuelto.")
            __prestado == False
        else:
            print("El libro no esta prestado.")
            