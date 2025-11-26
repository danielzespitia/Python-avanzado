import pygame
import sys

pygame.init()
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("4. Control con Teclado")
reloj = pygame.time.Clock()

# Jugador (cuadrado)
jugador_rect = pygame.Rect(375, 275, 50, 50)
velocidad = 5

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Detectar teclas presionadas (movimiento continuo)
    teclas = pygame.key.get_pressed()
    
    if teclas[pygame.K_LEFT]:
        jugador_rect.x -= velocidad
    if teclas[pygame.K_RIGHT]:
        jugador_rect.x += velocidad
    if teclas[pygame.K_UP]:
        jugador_rect.y -= velocidad
    if teclas[pygame.K_DOWN]:
        jugador_rect.y += velocidad

    # Limitar a la pantalla
    if jugador_rect.left < 0: jugador_rect.left = 0
    if jugador_rect.right > 800: jugador_rect.right = 800
    if jugador_rect.top < 0: jugador_rect.top = 0
    if jugador_rect.bottom > 600: jugador_rect.bottom = 600

    pantalla.fill((30, 30, 30))
    pygame.draw.rect(pantalla, (0, 255, 255), jugador_rect)
    
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
sys.exit()
