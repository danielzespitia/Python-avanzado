# programacion orientada a objetos
class janna:
    edad = 20
    altura = 1.55
    pelo = "negro"
    color_de_piel = "morena"
    ocupacion = "estudiante"
    trabajo = "profesora"
    mascota = "gato"
    hermanos = 5
    vehiculo = "moto"
    pasatiempo = "jugar cod"

# invocar las cosas
    def comer(self):
        print(f"mi edad es {self.edad}, mi altura es {self.altura}, el color de mi pelo es {self.pelo}, mi color de piel es {self.color_de_piel}, yo soy {self.ocupacion}, trabajo de {self.trabajo}.")

    def hacer_ejercicio(self):
        print("Janna hace ejercicio.")

    def bailar(self):
        print("Janna está bailando.")

# para imprimir
janna_persona = janna()
janna_persona.comer()
janna_persona.hacer_ejercicio()
janna_persona.bailar()