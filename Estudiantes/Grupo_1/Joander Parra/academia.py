import random

class Hechizo:
    def __init__(self, nombre, daño, costo_mana, tipo):
        self.nombre = nombre
        self.daño = daño
        self.costo_mana = costo_mana
        self.tipo = tipo

    def mostrar_info(self):
        print(f"Hechizo: {self.nombre} | Daño: {self.daño} | Mana: {self.costo_mana} | Tipo: {self.tipo}")

class Duelista:
    def __init__(self, nombre, nivel=1, mana=100):
        self.nombre = nombre
        self.nivel = nivel
        self.mana = mana
        self.hechizos_aprendidos = []

    def aprender_hechizo(self, hechizo):
        if hechizo not in self.hechizos_aprendidos:
            self.hechizos_aprendidos.append(hechizo)
            print(f"{self.nombre} ha aprendido el hechizo {hechizo.nombre}.")

    def lanzar_hechizo(self, hechizo, objetivo):
        if hechizo in self.hechizos_aprendidos and self.mana >= hechizo.costo_mana:
            self.mana -= hechizo.costo_mana
            print(f"{self.nombre} lanza {hechizo.nombre} a {objetivo.nombre} causando {hechizo.daño} de daño.")
            objetivo.recibir_daño(hechizo.daño)
        else:
            print(f"{self.nombre} no puede lanzar {hechizo.nombre} (mana insuficiente o no aprendido).")

    def recargar_mana(self):
        recarga = random.randint(20, 40)
        self.mana += recarga
        print(f"{self.nombre} recarga {recarga} puntos de mana. Mana actual: {self.mana}")

    def mostrar_estado(self):
        print(f"{self.nombre} | Nivel: {self.nivel} | Mana: {self.mana} | Hechizos: {[h.nombre for h in self.hechizos_aprendidos]}")

    def recibir_daño(self, daño):
        print(f"{self.nombre} recibe {daño} de daño mágico.")

class Estudiante(Duelista):
    def subir_nivel(self):
        self.nivel += 1
        self.mana += 20
        print(f"{self.nombre} ha subido al nivel {self.nivel}.")

class Profesor(Duelista):
    def __init__(self, nombre, especialidad):
        super().__init__(nombre, nivel=5, mana=150)
        self.especialidad = especialidad
        self.hechizos_domina = []

    def enseñar_hechizo(self, estudiante, hechizo):
        if hechizo in self.hechizos_domina:
            estudiante.aprender_hechizo(hechizo)
            print(f"{self.nombre} enseña {hechizo.nombre} a {estudiante.nombre}.")
        else:
            print(f"{self.nombre} no domina el hechizo {hechizo.nombre}.")

    def evaluar(self, estudiante):
        print(f"{self.nombre} evalúa a {estudiante.nombre}.")
        if len(estudiante.hechizos_aprendidos) > 0:
            estudiante.subir_nivel()
        else:
            print(f"{estudiante.nombre} necesita aprender más hechizos.")

class Academia:
    def __init__(self):
        self.estudiantes = []
        self.profesores = []

    def matricular_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        print(f"Estudiante {estudiante.nombre} matriculado.")

    def asignar_profesor(self, profesor):
        self.profesores.append(profesor)
        print(f"Profesor {profesor.nombre} asignado.")

    def organizar_duelo(self, duelista1, duelista2):
        print(f"\n¡Duelo entre {duelista1.nombre} y {duelista2.nombre}!")
        if duelista1.hechizos_aprendidos and duelista2.hechizos_aprendidos:
            h1 = random.choice(duelista1.hechizos_aprendidos)
            h2 = random.choice(duelista2.hechizos_aprendidos)
            duelista1.lanzar_hechizo(h1, duelista2)
            duelista2.lanzar_hechizo(h2, duelista1)
        else:
            print("Ambos duelistas necesitan aprender hechizos.")

    def mostrar_academia(self):
        print("\n--- Academia de Magia ---")
        print("Estudiantes:")
        for e in self.estudiantes:
            e.mostrar_estado()
        print("Profesores:")
        for p in self.profesores:
            p.mostrar_estado()


if __name__ == "__main__":
    
    fuego = Hechizo("Bola de Fuego", 30, 25, "Fuego")
    hielo = Hechizo("Rayo de Hielo", 20, 15, "Hielo")
    rayo = Hechizo("Impacto Eléctrico", 25, 20, "Eléctrico")

   
    prof1 = Profesor("Dumbledore", "Fuego")
    prof1.hechizos_domina = [fuego, hielo]
    prof2 = Profesor("McGonagall", "Hielo")
    prof2.hechizos_domina = [hielo, rayo]

   
    est1 = Estudiante("Harry")
    est2 = Estudiante("Hermione")

   
    academia = Academia()
    academia.matricular_estudiante(est1)
    academia.matricular_estudiante(est2)
    academia.asignar_profesor(prof1)
    academia.asignar_profesor(prof2)

    
    prof1.enseñar_hechizo(est1, fuego)
    prof2.enseñar_hechizo(est2, rayo)
    prof1.evaluar(est1)
    prof2.evaluar(est2)

    
    academia.organizar_duelo(est1, est2)
    academia.mostrar_academia()