import pygame
from constantes_copy import *
segundos = "12"
fin_tiempo = False

pygame.init()

tiempo_segundos = pygame.USEREVENT
pygame.time.set_timer(tiempo_segundos,1000)
pygame.mixer.init()
sonido = pygame.mixer.Sound("musiquita.wav")
volumen = 0.12
sonido.set_volume(volumen)

pantalla = pygame.display.set_mode((500,500))
pygame.display.set_caption("Pygame")
fuente = pygame.font.SysFont("Arial",80)

correr = True

while correr:
    sonido.play()
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.quit():
            correr = False
        elif evento.type == pygame.USEREVENT:
            if evento.type == tiempo_segundos:
                if fin_tiempo == False:
                    segundos = int(segundos) - 1
                    volumen = volumen - 0.01
                    sonido.set_volume(volumen)
                    if int(segundos) == 0:
                        fin_tiempo = True
                        segundos = "tiempo"
                        sonido.stop()

    pantalla.fill((COLOR_BLANCO))# Se pinta el fondo de la ventana.
    print(2)
    segundos_texto = fuente.render(str(segundos),True)
    pantalla.blit(segundos,(100,100))
    pygame.display.flip()

sonido.fondo.stop()
pygame.quit()

