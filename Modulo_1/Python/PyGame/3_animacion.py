import pygame
import sys

pygame.init()
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("3. Animación y Rebote")
reloj = pygame.time.Clock()

x = 400
y = 300
velocidad_x = 5
velocidad_y = 5
radio = 30

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Actualizar posición
    x += velocidad_x
    y += velocidad_y

    # Rebotar en bordes horizontales
    if x + radio > 800 or x - radio < 0:
        velocidad_x *= -1
    
    # Rebotar en bordes verticales
    if y + radio > 600 or y - radio < 0:
        velocidad_y *= -1

    # Dibujar
    pantalla.fill((0, 0, 0))
    pygame.draw.circle(pantalla, (255, 255, 0), (x, y), radio)
    
    pygame.display.flip()
    reloj.tick(60) # 60 FPS

pygame.quit()
sys.exit()
