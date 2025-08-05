import random
class Hechizo:
    def __init__(self, nombre, daño, costo_mana, tipo):
        self.__nombre = nombre
        self.__daño = daño
        self.__costo_mana = costo_mana
        self.__tipo = tipo

    def get_nombre(self):
        return self.__nombre

    def get_daño(self):
        return self.__daño

    def get_costo_mana(self):
        return self.__costo_mana

    def get_tipo(self):
        return self.__tipo

    def mostrar_info(self):
        print(f"Hechizo: {self.__nombre} (Tipo: {self.__tipo}, Daño: {self.__daño}, Costo de Mana: {self.__costo_mana})")


class Duelista:
    def __init__(self, nombre, nivel, vida, mana):
        self.__nombre = nombre
        self.__nivel = nivel
        self.__vida = vida
        self.__vida_maxima = vida
        self.__mana = mana
        self.__mana_maximo = mana
        self.__esta_vivo = True

    def get_nombre(self):
        return self.__nombre

    def get_nivel(self):
        return self.__nivel

    def get_vida(self):
        return self.__vida

    def get_mana(self):
        return self.__mana

    def esta_vivo(self):
        return self.__esta_vivo

    def recibir_daño(self, valor):
        if not self.__esta_vivo:
            return

        self.__vida -= valor
        if self.__vida <= 0:
            self.__vida = 0
            self.__esta_vivo = False
            print(f"{self.__nombre} ha sido derrotado.")
        else:
            print(f"{self.__nombre} recibe {valor} de daño. Vida restante: {self.__vida}")

    def curarse(self, valor_curacion):
        if not self.__esta_vivo:
            return

        vida_antes = self.__vida
        self.__vida += valor_curacion
        if self.__vida > self.__vida_maxima:
            self.__vida = self.__vida_maxima
        
        curacion_realizada = self.__vida - vida_antes
        if curacion_realizada > 0:
            print(f"{self.__nombre} se cura {curacion_realizada} puntos. Vida actual: {self.__vida}")

    def recargar_mana(self):
        mana_recargado = int(self.__mana_maximo * 0.2) + 5
        mana_antes = self.__mana
        self.__mana += mana_recargado
        if self.__mana > self.__mana_maximo:
            self.__mana = self.__mana_maximo
        print(f"{self.__nombre} recarga mana. Mana actual: {self.__mana}")

    def mostrar_estado(self):
        estado = "Vivo" if self.__esta_vivo else "Caido"
        print(f"  {self.__nombre} (Nivel: {self.__nivel}, Vida: {self.__vida}/{self.__vida_maxima}, Mana: {self.__mana}/{self.__mana_maximo}, Estado: {estado})")


class Estudiante(Duelista):
    def __init__(self, nombre):
        super().__init__(nombre, nivel=1, vida=100, mana=80)
        self.__hechizos_aprendidos = {}

    def aprender_hechizo(self, hechizo):
        if hechizo.get_nombre() in self.__hechizos_aprendidos:
            print(f"{self.get_nombre()} ya conoce el hechizo {hechizo.get_nombre()}.")
            return False
        self.__hechizos_aprendidos[hechizo.get_nombre()] = hechizo
        print(f"{self.get_nombre()} ha aprendido el hechizo: {hechizo.get_nombre()}.")
        return True

    def lanzar_hechizo(self, nombre_hechizo, objetivo):
        if not self.esta_vivo():
            print(f"{self.get_nombre()} esta caido y no puede lanzar hechizos.")
            return

        hechizo = self.__hechizos_aprendidos.get(nombre_hechizo)
        if not hechizo:
            print(f"{self.get_nombre()} no conoce el hechizo {nombre_hechizo}.")
            return


        if self.get_mana() < hechizo.get_costo_mana():
            print(f"{self.get_nombre()} no tiene suficiente mana para lanzar {nombre_hechizo} (Necesita {hechizo.get_costo_mana()}, tiene {self.get_mana()}).")
            return

        self._Duelista__mana -= hechizo.get_costo_mana()
        print(f"{self.get_nombre()} lanza {hechizo.get_nombre()} a {objetivo.get_nombre()}.")
        
        if hechizo.get_tipo() == "Ofensivo":
            daño_final = hechizo.get_daño() + (self.get_nivel() * 2)
            objetivo.recibir_daño(daño_final)
        elif hechizo.get_tipo() == "Curativo":
            valor_curacion = hechizo.get_daño() + (self.get_nivel() * 1.5)
            self.curarse(valor_curacion)

    def subir_nivel(self, cantidad=1):
        self._Duelista__nivel += cantidad
        self._Duelista__vida_maxima += (cantidad * 10)
        self._Duelista__mana_maximo += (cantidad * 5)
        self._Duelista__vida = self._Duelista__vida_maxima
        self._Duelista__mana = self._Duelista__mana_maximo
        print(f"{self.get_nombre()} ha subido a Nivel {self.get_nivel()}! Stats mejorados.")

    def mostrar_estado(self):
        super().mostrar_estado()
        print(f"    Hechizos conocidos: {', '.join(self.__hechizos_aprendidos.keys()) if self.__hechizos_aprendidos else 'Ninguno'}")


class Profesor:
    def __init__(self, nombre, especialidad, hechizos_domina):
        self.__nombre = nombre
        self.__especialidad = especialidad
        self.__hechizos_domina = hechizos_domina

    def get_nombre(self):
        return self.__nombre

    def get_especialidad(self):
        return self.__especialidad

    def enseñar_hechizo(self, estudiante, nombre_hechizo):
        hechizo_a_enseñar = next((h for h in self.__hechizos_domina if h.get_nombre() == nombre_hechizo), None)
        
        if hechizo_a_enseñar:
            print(f"{self.__nombre} (Profesor de {self.__especialidad}) intenta enseñar {nombre_hechizo} a {estudiante.get_nombre()}.")
            estudiante.aprender_hechizo(hechizo_a_enseñar)
        else:
            print(f"{self.__nombre} no domina el hechizo {nombre_hechizo} para enseñarlo.")

    def evaluar(self, estudiante):
        print(f"{self.__nombre} esta evaluando a {estudiante.get_nombre()} en su habilidad magica.")
        if len(estudiante._Estudiante__hechizos_aprendidos) >= 2 and estudiante.get_nivel() >= 1:
            print(f"{estudiante.get_nombre()} pasa la evaluacion y sube de nivel!")
            estudiante.subir_nivel()
        else:
            print(f"{estudiante.get_nombre()} aun necesita practicar mas.")

    def mostrar_info(self):
        hechizos = ", ".join([h.get_nombre() for h in self.__hechizos_domina])
        print(f"Profesor: {self.__nombre} (Especialidad: {self.__especialidad}, Domina: {hechizos})")


class Academia:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__estudiantes = []
        self.__profesores = []
        self.__hechizos_maestros = []

    def agregar_hechizo_maestro(self, hechizo):
        self.__hechizos_maestros.append(hechizo)

    def matricular_estudiante(self, estudiante):
        self.__estudiantes.append(estudiante)
        print(f"{estudiante.get_nombre()} ha sido matriculado en la Academia {self.__nombre}.")

    def contratar_profesor(self, profesor):
        self.__profesores.append(profesor)
        print(f"{profesor.get_nombre()} ha sido contratado como profesor en la Academia {self.__nombre}.")

    def mostrar_academia(self):
        print(f"\n--- Academia {self.__nombre} ---")
        print("Estudiantes:")
        if self.__estudiantes:
            for est in self.__estudiantes:
                est.mostrar_estado()
        else:
            print("  No hay estudiantes matriculados.")
        
        print("\nProfesores:")
        if self.__profesores:
            for prof in self.__profesores:
                prof.mostrar_info()
        else:
            print("  No hay profesores contratados.")

        print("\nHechizos Maestros Disponibles:")
        if self.__hechizos_maestros:
            for hechizo in self.__hechizos_maestros:
                hechizo.mostrar_info()
        else:
            print("  No hay hechizos maestros registrados.")


    def organizar_duelo(self, duelista1, duelista2):
        if not isinstance(duelista1, Duelista) or not isinstance(duelista2, Duelista):
            print("Error: Ambos participantes deben ser Duelistas (Estudiantes o futuros Profesores con habilidad de duelo).")
            return

        print(f"\n--- INICIO DE DUELO: {duelista1.get_nombre()} vs {duelista2.get_nombre()} ---")
        turno = 0
        while duelista1.esta_vivo() and duelista2.esta_vivo():
            turno += 1
            print(f"\nTurno {turno}:")
            
         
            if duelista1.esta_vivo():
                if isinstance(duelista1, Estudiante):
                    hechizos_ofensivos = [h.get_nombre() for h in duelista1._Estudiante__hechizos_aprendidos.values() if h.get_tipo() == "Ofensivo"]
                    hechizos_curativos = [h.get_nombre() for h in duelista1._Estudiante__hechizos_aprendidos.values() if h.get_tipo() == "Curativo"]
                    
                    if duelista1.get_vida() < duelista1._Duelista__vida_maxima * 0.4 and hechizos_curativos and random.random() < 0.6:
                        duelista1.lanzar_hechizo(random.choice(hechizos_curativos), duelista1)
                    elif hechizos_ofensivos and random.random() < 0.8:
                        duelista1.lanzar_hechizo(random.choice(hechizos_ofensivos), duelista2)
                    else:
                        duelista1.recargar_mana()
                else:
                    duelista1.recargar_mana()
            
            if not duelista2.esta_vivo():
                break

          
            if duelista2.esta_vivo():
                if isinstance(duelista2, Estudiante):
                    hechizos_ofensivos = [h.get_nombre() for h in duelista2._Estudiante__hechizos_aprendidos.values() if h.get_tipo() == "Ofensivo"]
                    hechizos_curativos = [h.get_nombre() for h in duelista2._Estudiante__hechizos_aprendidos.values() if h.get_tipo() == "Curativo"]

                    if duelista2.get_vida() < duelista2._Duelista__vida_maxima * 0.4 and hechizos_curativos and random.random() < 0.6:
                        duelista2.lanzar_hechizo(random.choice(hechizos_curativos), duelista2)
                    elif hechizos_ofensivos and random.random() < 0.8:
                        duelista2.lanzar_hechizo(random.choice(hechizos_ofensivos), duelista1)
                    else:
                        duelista2.recargar_mana()
                else:
                    duelista2.recargar_mana()
            
            duelista1.mostrar_estado()
            duelista2.mostrar_estado()
            input("Presiona Enter para el siguiente turno del duelo...")

        print("\n--- DUELO TERMINADO ---")
        if duelista1.esta_vivo():
            print(f"Ganador del duelo: {duelista1.get_nombre()}")
            duelista1.subir_nivel()
        elif duelista2.esta_vivo():
            print(f"Ganador del duelo: {duelista2.get_nombre()}")
            duelista2.subir_nivel()
        else:
            print("El duelo termino en un empate devastador.")


if __name__ == "__main__":

    hechizo_fuego = Hechizo("Bola de Fuego", 30, 20, "Ofensivo")
    hechizo_escudo = Hechizo("Escudo Arcano", 0, 15, "Defensivo")
    hechizo_curacion = Hechizo("Aliento Vital", 25, 20, "Curativo")

    
    academia_arcana = Academia("Arcana Logros")
    academia_arcana.agregar_hechizo_maestro(hechizo_fuego)
    academia_arcana.agregar_hechizo_maestro(hechizo_escudo)
    academia_arcana.agregar_hechizo_maestro(hechizo_curacion)

   
    estudiante1 = Estudiante("Victor")
    estudiante2 = Estudiante("Diego")
    estudiante3 = Estudiante("Misael")

    profesor1 = Profesor("Maestro Daniel", "Pirotecnia", [hechizo_fuego, hechizo_escudo])
    profesor2 = Profesor("Profesora Serena", "Sanacion", [hechizo_curacion])


    academia_arcana.matricular_estudiante(estudiante1)
    academia_arcana.matricular_estudiante(estudiante2)
    academia_arcana.matricular_estudiante(estudiante3)
    academia_arcana.contratar_profesor(profesor1)
    academia_arcana.contratar_profesor(profesor2)

    academia_arcana.mostrar_academia()
    input("\nPresiona Enter para continuar con el dia en la academia...")


    print("\n--- Dia de Clases ---")
    profesor1.enseñar_hechizo(estudiante1, "Bola de Fuego")
    profesor1.enseñar_hechizo(estudiante2, "Bola de Fuego")
    profesor2.enseñar_hechizo(estudiante2, "Aliento Vital")
    profesor2.enseñar_hechizo(estudiante3, "Aliento Vital")
    profesor1.enseñar_hechizo(estudiante1, "Escudo Arcano")

    estudiante1.mostrar_estado()
    estudiante2.mostrar_estado()
    estudiante3.mostrar_estado()
    input("\nPresiona Enter para las evaluaciones...")

    print("\n--- Dia de Evaluaciones ---")
    profesor1.evaluar(estudiante1)
    profesor2.evaluar(estudiante2)
    profesor1.evaluar(estudiante3)

    estudiante1.mostrar_estado()
    estudiante2.mostrar_estado()
    estudiante3.mostrar_estado()
    input("\nPresiona Enter para el torneo de duelos...")

    print("\n--- Torneo de Duelos ---")
    academia_arcana.organizar_duelo(estudiante1, estudiante2)

    print("\n--- Estado final de los participantes del duelo ---")
    estudiante1.mostrar_estado()
    estudiante2.mostrar_estado()

    print("\nFin de la simulacion de la Academia de Magia.")