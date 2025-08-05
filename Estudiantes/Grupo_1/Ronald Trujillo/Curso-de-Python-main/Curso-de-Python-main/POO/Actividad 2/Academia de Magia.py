import random

# Clase base para combate
class Duelista:
    def __init__(self, nombre, nivel=1, mana=100):
        self.nombre = nombre
        self.nivel = nivel
        self.mana = mana
        self.vida = 100

    def esta_vivo(self):
        return self.vida > 0

    def recibir_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nombre} recibe {dano} de daño. Vida restante: {self.vida}")

    def recargar_mana(self):
        recarga = random.randint(10, 30)
        self.mana += recarga
        if self.mana > 100:
            self.mana = 100
        print(f"{self.nombre} recarga {recarga} de mana. Mana actual: {self.mana}")

# Clase Hechizo
class Hechizo:
    def __init__(self, nombre, dano, costo_mana, tipo):
        self.nombre = nombre
        self.dano = dano
        self.costo_mana = costo_mana
        self.tipo = tipo

    def mostrar_info(self):
        print(f"Hechizo: {self.nombre} | Daño: {self.dano} | Mana: {self.costo_mana} | Tipo: {self.tipo}")

# Estudiante
class Estudiante(Duelista):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.hechizos_aprendidos = []

    def aprender_hechizo(self, hechizo):
        self.hechizos_aprendidos.append(hechizo)
        print(f"{self.nombre} ha aprendido el hechizo: {hechizo.nombre}")

    def lanzar_hechizo(self, objetivo):
        if not self.hechizos_aprendidos:
            print(f"{self.nombre} no conoce ningún hechizo.")
            return

        hechizo = random.choice(self.hechizos_aprendidos)
        if self.mana < hechizo.costo_mana:
            print(f"{self.nombre} no tiene suficiente mana para lanzar {hechizo.nombre}.")
            self.recargar_mana()
            return

        print(f"{self.nombre} lanza {hechizo.nombre} a {objetivo.nombre}.")
        self.mana -= hechizo.costo_mana
        objetivo.recibir_dano(hechizo.dano)

    def mostrar_estado(self):
        print(f"{self.nombre} - Nivel: {self.nivel} | Vida: {self.vida} | Mana: {self.mana}")
        if self.hechizos_aprendidos:
            print("Hechizos conocidos:")
            for h in self.hechizos_aprendidos:
                print(f" - {h.nombre}")
        else:
            print("No ha aprendido ningún hechizo.")

# Profesor
class Profesor(Duelista):
    def __init__(self, nombre, especialidad):
        super().__init__(nombre, nivel=5, mana=150)
        self.especialidad = especialidad
        self.hechizos_domina = []

    def agregar_hechizo(self, hechizo):
        self.hechizos_domina.append(hechizo)

    def enseñar_hechizo(self, estudiante, hechizo):
        if hechizo in self.hechizos_domina:
            estudiante.aprender_hechizo(hechizo)
            print(f"{self.nombre} ha enseñado {hechizo.nombre} a {estudiante.nombre}.")
        else:
            print(f"{self.nombre} no domina el hechizo {hechizo.nombre}.")

    def evaluar(self, estudiante):
        print(f"{self.nombre} evalúa a {estudiante.nombre}.")
        if estudiante.hechizos_aprendidos:
            print("Resultado: Aprobado")
        else:
            print("Resultado: Reprobado")

# Academia de Magia
class Academia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []
        self.profesores = []

    def matricular_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        print(f"{estudiante.nombre} se ha matriculado en la academia.")

    def asignar_profesor(self, profesor):
        self.profesores.append(profesor)
        print(f"{profesor.nombre} ha sido asignado como profesor.")

    def organizar_duelo(self, est1, est2):
        print(f"\nDuelo entre {est1.nombre} y {est2.nombre}!")
        turno = 0
        while est1.esta_vivo() and est2.esta_vivo():
            atacante = est1 if turno % 2 == 0 else est2
            defensor = est2 if turno % 2 == 0 else est1
            atacante.lanzar_hechizo(defensor)
            turno += 1
        ganador = est1 if est1.esta_vivo() else est2
        print(f"\nGanador del duelo: {ganador.nombre}")

    def mostrar_academia(self):
        print(f"\nAcademia de Magia: {self.nombre}")
        print("\nProfesores:")
        for p in self.profesores:
            print(f" - {p.nombre} (Especialidad: {p.especialidad})")
        print("\nEstudiantes:")
        for e in self.estudiantes:
            print(f" - {e.nombre}, Nivel {e.nivel}")

# --- Simulación ---

if __name__ == "__main__":
    # Crear academia
    academia = Academia("Instituto Arcano")

    # Hechizos
    fuego = Hechizo("Bola de Fuego", dano=30, costo_mana=25, tipo="Fuego")
    hielo = Hechizo("Lanza de Hielo", dano=20, costo_mana=20, tipo="Hielo")
    rayo = Hechizo("Impacto Eléctrico", dano=40, costo_mana=35, tipo="Rayo")

    # Crear profesores
    prof_ignis = Profesor("Ignis", "Fuego")
    prof_ignis.agregar_hechizo(fuego)

    prof_cryo = Profesor("Cryo", "Hielo")
    prof_cryo.agregar_hechizo(hielo)

    academia.asignar_profesor(prof_ignis)
    academia.asignar_profesor(prof_cryo)

    # Crear estudiantes
    est_1 = Estudiante("Ariana")
    est_2 = Estudiante("Leo")

    academia.matricular_estudiante(est_1)
    academia.matricular_estudiante(est_2)

    # Profesores enseñan hechizos
    prof_ignis.enseñar_hechizo(est_1, fuego)
    prof_cryo.enseñar_hechizo(est_2, hielo)

    # Evaluaciones
    prof_ignis.evaluar(est_1)
    prof_cryo.evaluar(est_2)

    # Mostrar estado
    est_1.mostrar_estado()
    est_2.mostrar_estado()

    # Duelo entre estudiantes
    academia.organizar_duelo(est_1, est_2)

    # Mostrar resumen
    academia.mostrar_academia()
