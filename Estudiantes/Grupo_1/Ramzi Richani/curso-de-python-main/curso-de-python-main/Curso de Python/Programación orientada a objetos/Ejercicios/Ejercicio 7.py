import random

class Hechizo:
    def __init__(self, nombre, danio, costo_mana, tipo):
        self.nombre = nombre
        self.danio = danio
        self.costo_mana = costo_mana
        self.tipo = tipo

    def mostrar_info(self):
        print(f"Hechizo: {self.nombre} | Daño: {self.danio} | Costo de maná: {self.costo_mana} | Tipo: {self.tipo}")

class Duelista:
    def __init__(self, nombre, nivel=1, mana=100):
        self.nombre = nombre
        self.nivel = nivel
        self.mana = mana
        self.mana_max = mana
        self.hechizos_aprendidos = {}

    def lanzar_hechizo(self, hechizo_nombre, objetivo):
        if hechizo_nombre in self.hechizos_aprendidos:
            hechizo = self.hechizos_aprendidos[hechizo_nombre]
            if self.mana >= hechizo.costo_mana:
                print(f"{self.nombre} lanza {hechizo.nombre} a {objetivo.nombre}!")
                self.mana -= hechizo.costo_mana
                objetivo.recibir_danio(hechizo.danio)
            else:
                print(f"{self.nombre} no tiene suficiente maná para lanzar {hechizo.nombre}.")
        else:
            print(f"{self.nombre} no conoce el hechizo {hechizo_nombre}.")

    def recargar_mana(self):
        recupera = random.randint(15, 30)
        self.mana = min(self.mana_max, self.mana + recupera)
        print(f"{self.nombre} recarga {recupera} de maná. Maná actual: {self.mana}/{self.mana_max}")

    def mostrar_estado(self):
        print(f"{self.nombre} - Nivel: {self.nivel}, Maná: {self.mana}/{self.mana_max}, Hechizos: {list(self.hechizos_aprendidos.keys())}")

    def recibir_danio(self, danio):
        self.mana -= danio//2
        print(f"{self.nombre} recibe {danio} de daño mágico (se resta {danio//2} de maná). Maná: {self.mana}/{self.mana_max}")

    def esta_consciente(self):
        return self.mana > 0

class Estudiante(Duelista):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.experiencia = 0

    def aprender_hechizo(self, hechizo):
        if hechizo.nombre in self.hechizos_aprendidos:
            print(f"{self.nombre} ya conoce el hechizo {hechizo.nombre}.")
        else:
            self.hechizos_aprendidos[hechizo.nombre] = hechizo
            print(f"{self.nombre} ha aprendido el hechizo {hechizo.nombre}.")

    def subir_nivel(self):
        self.nivel += 1
        self.mana_max += 20
        self.mana = self.mana_max
        print(f"{self.nombre} ha subido a nivel {self.nivel}. ¡Maná máximo aumentado a {self.mana_max}!")

class Profesor(Duelista):
    def __init__(self, nombre, especialidad):
        super().__init__(nombre, nivel=5, mana=150)
        self.especialidad = especialidad
        self.hechizos_domina = {}

    def enseñar_hechizo(self, estudiante, hechizo):
        if hechizo.nombre not in self.hechizos_domina:
            print(f"{self.nombre} no domina el hechizo {hechizo.nombre}, así que no puede enseñarlo.")
        else:
            estudiante.aprender_hechizo(hechizo)
            print(f"{self.nombre} enseña {hechizo.nombre} a {estudiante.nombre}.")

    def evaluar(self, estudiante):
        print(f"{self.nombre} evalúa a {estudiante.nombre}...")
        if len(estudiante.hechizos_aprendidos) >= 2 and estudiante.nivel >= 2:
            print(f"{estudiante.nombre} ha aprobado la evaluación mágica.")
            estudiante.subir_nivel()
        else:
            print(f"{estudiante.nombre} necesita aprender más hechizos y subir de nivel.")

class Academia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []
        self.profesores = []
        self.clases = {}

    def matricular_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        print(f"{estudiante.nombre} ha sido matriculado/a en la academia {self.nombre}.")

    def asignar_profesor(self, profesor, estudiantes):
        self.profesores.append(profesor)
        self.clases[profesor] = estudiantes
        print(f"{profesor.nombre} ha sido asignado/a como profesor/a de {', '.join(e.nombre for e in estudiantes)}.")

    def organizar_duelo(self, duelista1, duelista2):
        print(f"\n¡Duelo mágico entre {duelista1.nombre} y {duelista2.nombre}!")
        turno = 0
        while duelista1.esta_consciente() and duelista2.esta_consciente():
            atacante, defensor = (duelista1, duelista2) if turno % 2 == 0 else (duelista2, duelista1)
            if atacante.hechizos_aprendidos:
                hechizo = random.choice(list(atacante.hechizos_aprendidos.values()))
                atacante.lanzar_hechizo(hechizo.nombre, defensor)
            else:
                atacante.recargar_mana()
            turno += 1
            if not defensor.esta_consciente():
                print(f"¡{defensor.nombre} queda fuera de combate!\n")
                break
        ganador = duelista1 if duelista1.esta_consciente() else duelista2
        print(f"Ganador del duelo: {ganador.nombre}")
        if isinstance(ganador, Estudiante):
            ganador.experiencia += 15
            if ganador.experiencia >= 20 * ganador.nivel:
                ganador.subir_nivel()

    def mostrar_academia(self):
        print(f"\nAcademia: {self.nombre}\nProfesores:")
        for p in self.profesores:
            print(f"- {p.nombre} (Especialidad: {p.especialidad})")
        print("Estudiantes:")
        for e in self.estudiantes:
            e.mostrar_estado()
        print()

if __name__ == "__main__":
    bola_fuego = Hechizo("Bola de Fuego", 30, 25, "Ofensivo")
    escudo_magico = Hechizo("Escudo Mágico", 0, 15, "Defensivo")
    rayo = Hechizo("Rayo", 40, 35, "Ofensivo")
    curacion = Hechizo("Curación", -20, 20, "Sanador")

    prof_ignis = Profesor("Ignis", "Fuego")
    prof_ignis.hechizos_domina = {
        bola_fuego.nombre: bola_fuego,
        rayo.nombre: rayo
    }
    prof_aegis = Profesor("Aegis", "Defensa")
    prof_aegis.hechizos_domina = {
        escudo_magico.nombre: escudo_magico,
        curacion.nombre: curacion
    }

    est_ana = Estudiante("Ana")
    est_beto = Estudiante("Beto")
    est_carmen = Estudiante("Carmen")

    academia = Academia("Hogmagic")
    academia.matricular_estudiante(est_ana)
    academia.matricular_estudiante(est_beto)
    academia.matricular_estudiante(est_carmen)

    academia.asignar_profesor(prof_ignis, [est_ana, est_beto])
    academia.asignar_profesor(prof_aegis, [est_carmen])

    prof_ignis.enseñar_hechizo(est_ana, bola_fuego)
    prof_ignis.enseñar_hechizo(est_beto, rayo)
    prof_aegis.enseñar_hechizo(est_carmen, escudo_magico)
    prof_aegis.enseñar_hechizo(est_carmen, curacion)

    prof_ignis.enseñar_hechizo(est_ana, rayo)
    prof_aegis.enseñar_hechizo(est_beto, curacion)

    prof_ignis.evaluar(est_ana)
    prof_aegis.evaluar(est_carmen)

    academia.organizar_duelo(est_ana, est_beto)
    academia.organizar_duelo(est_carmen, est_beto)

    estudiantes = academia.estudiantes
    for i in range(len(estudiantes)):
        for j in range(i+1, len(estudiantes)):
            academia.organizar_duelo(estudiantes[i], estudiantes[j])

    academia.mostrar_academia()