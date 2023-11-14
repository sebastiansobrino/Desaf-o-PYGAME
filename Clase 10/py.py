import pygame
from constantes_copy import * 
segundos = "12"
fin_tiempo = False

pygame.init()

timer_segundos = pygame.USEREVENT
pygame.time.set_timer(timer_segundos,1000)

pygame.mixer.init()
sonido_fondo = pygame.mixer.Sound("musiquita.wav")
volumen = 0.12
sonido_fondo.set_volume(volumen)

pantalla = pygame.display.set_mode((500,500))

pygame.display.set_caption("Pygame")
fuente = pygame.font.SysFont("Arial",80)

flag_correr = True
while flag_correr:
    sonido_fondo.play()
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.quit:
            flag_correr = False
        if evento.type == pygame.USEREVENT:
            if evento.type == timer_segundos:
                if fin_tiempo == False:
                    segundos = int(segundos) - 1
                    volumen = volumen - 0.01
                    sonido_fondo.set_volume(volumen)
                if int(segundos) == 0:
                    fin_tiempo = True
                    segundos = "Tiempo"
                    sonido_fondo.stop()
    pantalla.fill(COLOR_ROJO)
    segundos_texto = fuente.render(str(segundos),True, COLOR_BLANCO)
    pantalla.blit(segundos_texto, (100,100))
    pygame.display.flip
sonido_fondo.stop()
pygame.quit()