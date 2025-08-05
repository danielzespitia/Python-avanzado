import random

class Hechizo:
    def __init__(self, nombre, dano, costo_mana, tipo):
        self.nombre = nombre
        self.dano = dano
        self.costo_mana = costo_mana
        self.tipo = tipo 

    def mostrar_info(self):
        return f"Hechizo: {self.nombre} (Daño: {self.dano}, Costo: {self.costo_mana} Mana, Tipo: {self.tipo})"


class Duelista:
    def __init__(self, nombre, nivel, mana):
        self.nombre = nombre
        self.nivel = nivel
        self.mana = mana
        self.vida = 100 + (nivel * 10) 
        self.hechizos_aprendidos = {} 
    
    def recibir_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nombre} recibe {dano} de daño. Vida restante: {self.vida}")

    def mostrar_estado(self):
        return f"{self.nombre} (Nivel: {self.nivel}) - Vida: {self.vida}, Mana: {self.mana}"


class Estudiante(Duelista):
    def __init__(self, nombre, nivel=1, mana=50):
        super().__init__(nombre, nivel, mana)
        self.experiencia = 0
        self.experiencia_para_subir = 100

    def aprender_hechizo(self, hechizo):
        if hechizo.nombre not in self.hechizos_aprendidos:
            self.hechizos_aprendidos[hechizo.nombre] = hechizo
            print(f"{self.nombre} ha aprendido el hechizo '{hechizo.nombre}'.")
        else:
            print(f"{self.nombre} ya conoce el hechizo '{hechizo.nombre}'.")

    def lanzar_hechizo(self, hechizo_nombre, objetivo):
        if hechizo_nombre in self.hechizos_aprendidos:
            hechizo = self.hechizos_aprendidos[hechizo_nombre]
            if self.mana >= hechizo.costo_mana:
                print(f"{self.nombre} lanza {hechizo.nombre} a {objetivo.nombre}.")
                self.mana -= hechizo.costo_mana
                objetivo.recibir_dano(hechizo.dano)
                return True
            else:
                print(f"{self.nombre} no tiene suficiente maná para lanzar {hechizo.nombre}.")
        else:
            print(f"{self.nombre} no conoce el hechizo '{hechizo_nombre}'.")
        return False

    def recargar_mana(self):
        recarga = self.nivel * 15
        self.mana += recarga
        print(f"{self.nombre} recarga {recarga} de maná. Maná actual: {self.mana}")

    def subir_nivel(self):
        self.nivel += 1
        self.vida = 100 + (self.nivel * 10) 
        self.mana += 20 
        self.experiencia = 0
        self.experiencia_para_subir = 100 + (self.nivel * 50)
        print(f"¡{self.nombre} ha subido al nivel {self.nivel}!")

    def ganar_experiencia(self, puntos):
        self.experiencia += puntos
        print(f"{self.nombre} gana {puntos} de experiencia. Total: {self.experiencia}/{self.experiencia_para_subir}")
        if self.experiencia >= self.experiencia_para_subir:
            self.subir_nivel()


class Profesor(Duelista):
    def __init__(self, nombre, especialidad, nivel=10, mana=150):
        super().__init__(nombre, nivel, mana)
        self.especialidad = especialidad
        self.hechizos_domina = {}

    def ensenar_hechizo(self, estudiante, hechizo):
        print(f"El profesor {self.nombre} le enseña el hechizo '{hechizo.nombre}' a {estudiante.nombre}.")
        estudiante.aprender_hechizo(hechizo)

    def evaluar(self, estudiante):
        if len(estudiante.hechizos_aprendidos) > 0:
            puntos_ganados = 50 * estudiante.nivel
            estudiante.ganar_experiencia(puntos_ganados)
            print(f"{self.nombre} evalúa a {estudiante.nombre} y le otorga {puntos_ganados} puntos de experiencia.")
        else:
            print(f"{estudiante.nombre} no ha aprendido hechizos, no puede ser evaluado.")


class Academia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = {} 
        self.profesores = {} 
    
    def matricular_estudiante(self, estudiante):
        self.estudiantes[estudiante.nombre] = estudiante
        print(f"{estudiante.nombre} se ha matriculado en la academia {self.nombre}.")

    def asignar_profesor(self, profesor):
        self.profesores[profesor.nombre] = profesor
        print(f"El profesor {profesor.nombre} ha sido asignado a la academia {self.nombre}.")

    def organizar_duelo(self, est1, est2):
        print(f"\n--- ¡Duelo Mágico entre {est1.nombre} y {est2.nombre} ha comenzado! ---")
        turno = 1
        while est1.vida > 0 and est2.vida > 0:
            print(f"\n----- Turno {turno} -----")
            
            hechizos_est1 = list(est1.hechizos_aprendidos.keys())
            hechizos_est2 = list(est2.hechizos_aprendidos.keys())

            if hechizos_est1:
                hechizo_est1 = random.choice(hechizos_est1)
                est1.lanzar_hechizo(hechizo_est1, est2)
            
            if est2.vida > 0 and hechizos_est2:
                hechizo_est2 = random.choice(hechizos_est2)
                est2.lanzar_hechizo(hechizo_est2, est1)
            
            if est1.vida <= 0:
                print(f"¡{est2.nombre} ha ganado el duelo!")
                est2.ganar_experiencia(100)
                break
            elif est2.vida <= 0:
                print(f"¡{est1.nombre} ha ganado el duelo!")
                est1.ganar_experiencia(100)
                break

            turno += 1

    def mostrar_academia(self):
        print(f"\n=== Academia Mágica {self.nombre} ===")
        print("--- Estudiantes ---")
        for estudiante in self.estudiantes.values():
            print(estudiante.mostrar_estado())
        
        print("\n--- Profesores ---")
        for profesor in self.profesores.values():
            print(profesor.mostrar_estado())


if __name__ == "__main__":
    academia_magica = Academia("Arcanum")

    estudiante1 = Estudiante("Alex")
    estudiante2 = Estudiante("Maya")
    profesor1 = Profesor("Albus", "Hechizos de Fuego")

    academia_magica.matricular_estudiante(estudiante1)
    academia_magica.matricular_estudiante(estudiante2)
    academia_magica.asignar_profesor(profesor1)

    hechizo_fuego = Hechizo("Bola de Fuego", 20, 15, "Fuego")
    hechizo_hielo = Hechizo("Rayo de Hielo", 18, 12, "Agua")

    profesor1.ensenar_hechizo(estudiante1, hechizo_fuego)
    profesor1.ensenar_hechizo(estudiante2, hechizo_hielo)

    estudiante1.ganar_experiencia(80) 
    estudiante2.ganar_experiencia(95)
    
    academia_magica.organizar_duelo(estudiante1, estudiante2)
    
    academia_magica.mostrar_academia()
