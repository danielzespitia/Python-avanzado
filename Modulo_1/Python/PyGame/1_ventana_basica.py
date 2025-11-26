import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("1. Ventana Básica")

# Colores
NEGRO = (0, 0, 0)

# Bucle principal
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    pantalla.fill(NEGRO)
    pygame.display.flip()

pygame.quit()
sys.exit()
