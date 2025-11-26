import pygame
import sys

pygame.init()
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("5. Eventos del Mouse")

color_circulo = (255, 0, 255)
radio = 20

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        
        # Evento de clic
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1: # Izquierdo
                color_circulo = (255, 0, 0)
            elif evento.button == 3: # Derecho
                color_circulo = (0, 0, 255)
        
        if evento.type == pygame.MOUSEBUTTONUP:
            color_circulo = (255, 0, 255) # Volver a original

    # Posición actual
    pos = pygame.mouse.get_pos()

    pantalla.fill((255, 255, 255))
    pygame.draw.circle(pantalla, color_circulo, pos, radio)
    
    pygame.display.flip()

pygame.quit()
sys.exit()
