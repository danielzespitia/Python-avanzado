import pygame
import time
import random

pygame.init()

# Colores
BLANCO = (255, 255, 255)
AMARILLO = (255, 255, 102)
NEGRO = (0, 0, 0)
ROJO = (213, 50, 80)
VERDE = (0, 255, 0)
AZUL = (50, 153, 213)

# Dimensiones de la pantalla
ANCHO_PANTALLA = 600
ALTO_PANTALLA = 400

pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption('Juego de la Serpiente')

reloj = pygame.time.Clock()

# Parámetros de la serpiente
BLOQUE_SERPIENTE = 10
VELOCIDAD_SERPIENTE = 15

# Fuentes
fuente_estilo = pygame.font.SysFont("bahnschrift", 25)
fuente_puntuacion = pygame.font.SysFont("comicsansms", 35)

def mostrar_puntuacion(puntuacion):
    valor = fuente_puntuacion.render("Puntuación: " + str(puntuacion), True, AMARILLO)
    pantalla.blit(valor, [0, 0])

def dibujar_serpiente(bloque_serpiente, lista_serpiente):
    for x in lista_serpiente:
        pygame.draw.rect(pantalla, NEGRO, [x[0], x[1], bloque_serpiente, bloque_serpiente])

def mensaje(msg, color):
    mesg = fuente_estilo.render(msg, True, color)
    # Centrar el mensaje
    rect_texto = mesg.get_rect(center=(ANCHO_PANTALLA/2, ALTO_PANTALLA/2))
    pantalla.blit(mesg, rect_texto)

def bucle_juego():
    game_over = False
    game_close = False

    x1 = ANCHO_PANTALLA / 2
    y1 = ALTO_PANTALLA / 2

    x1_cambio = 0
    y1_cambio = 0

    lista_serpiente = []
    longitud_serpiente = 1

    # Posición inicial de la comida
    comida_x = round(random.randrange(0, ANCHO_PANTALLA - BLOQUE_SERPIENTE) / 10.0) * 10.0
    comida_y = round(random.randrange(0, ALTO_PANTALLA - BLOQUE_SERPIENTE) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            pantalla.fill(AZUL)
            mensaje("Perdiste! Presiona C-Continuar o Q-Salir", ROJO)
            mostrar_puntuacion(longitud_serpiente - 1)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        bucle_juego()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_cambio = -BLOQUE_SERPIENTE
                    y1_cambio = 0
                elif event.key == pygame.K_RIGHT:
                    x1_cambio = BLOQUE_SERPIENTE
                    y1_cambio = 0
                elif event.key == pygame.K_UP:
                    y1_cambio = -BLOQUE_SERPIENTE
                    x1_cambio = 0
                elif event.key == pygame.K_DOWN:
                    y1_cambio = BLOQUE_SERPIENTE
                    x1_cambio = 0

        # Comprobar colisión con bordes
        if x1 >= ANCHO_PANTALLA or x1 < 0 or y1 >= ALTO_PANTALLA or y1 < 0:
            game_close = True
        
        x1 += x1_cambio
        y1 += y1_cambio
        pantalla.fill(AZUL)
        
        # Dibujar comida
        pygame.draw.rect(pantalla, VERDE, [comida_x, comida_y, BLOQUE_SERPIENTE, BLOQUE_SERPIENTE])
        
        # Lógica de la serpiente
        cabeza_serpiente = []
        cabeza_serpiente.append(x1)
        cabeza_serpiente.append(y1)
        lista_serpiente.append(cabeza_serpiente)
        
        if len(lista_serpiente) > longitud_serpiente:
            del lista_serpiente[0]

        # Comprobar colisión con uno mismo
        for x in lista_serpiente[:-1]:
            if x == cabeza_serpiente:
                game_close = True

        dibujar_serpiente(BLOQUE_SERPIENTE, lista_serpiente)
        mostrar_puntuacion(longitud_serpiente - 1)

        pygame.display.flip()

        # Comer comida
        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, ANCHO_PANTALLA - BLOQUE_SERPIENTE) / 10.0) * 10.0
            comida_y = round(random.randrange(0, ALTO_PANTALLA - BLOQUE_SERPIENTE) / 10.0) * 10.0
            longitud_serpiente += 1

        reloj.tick(VELOCIDAD_SERPIENTE)

    pygame.quit()
    quit()

if __name__ == "__main__":
    bucle_juego()
