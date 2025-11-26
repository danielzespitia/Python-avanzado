import pygame
import sys

pygame.init()
pygame.mixer.init()

pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("6. Sonido (Simulado)")

fuente = pygame.font.SysFont("Arial", 24)

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                print("¡SONIDO DE DISPARO!")
                # pygame.mixer.Sound("disparo.wav").play()

    pantalla.fill((0, 0, 0))
    
    texto = fuente.render("Presiona ESPACIO para 'reproducir' sonido", True, (255, 255, 255))
    pantalla.blit(texto, (50, 180))
    
    pygame.display.flip()

pygame.quit()
sys.exit()
