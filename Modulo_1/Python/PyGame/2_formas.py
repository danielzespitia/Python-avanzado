import pygame
import sys

pygame.init()
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("2. Dibujando Formas")

BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    pantalla.fill(BLANCO)

    # Rectángulo: (x, y, ancho, alto)
    pygame.draw.rect(pantalla, ROJO, (50, 50, 100, 50))

    # Círculo: (centro_x, centro_y), radio
    pygame.draw.circle(pantalla, VERDE, (300, 100), 40)

    # Línea: inicio, fin, grosor
    pygame.draw.line(pantalla, AZUL, (400, 50), (500, 150), 5)

    # Elipse (dentro de un rectángulo imaginario)
    pygame.draw.ellipse(pantalla, (255, 165, 0), (50, 200, 150, 100))

    pygame.display.flip()

pygame.quit()
sys.exit()
