import pygame
from biblioteca import *
from constantes import *
from datos import *

pygame.init() #Se inicializa pygame.


pantalla = pygame.display.set_mode([1000, 1000]) #Se crea una ventana.

running = True

font = pygame.font.Font(None, 36)
input_box = pygame.Rect(400, 650, 200, 32)
color_active = COLOR_NEGRO
color = pygame.Color('lightskyblue3')
text = ''

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                color = color_active
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                text = ''
                print(2)
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            elif len(text) < 10:
                text += event.unicode
    
    imagen = pygame.image.load("D7qC2kht38gp3vrqrGMGR6.jpg")  
    imagen = pygame.transform.scale(imagen,(1000,1000))
    texto_victoria = generar_texto("Ganaste",COLOR_NEGRO,(500,350))
    volver_al_menu = generar_texto("Volver al menu",COLOR_NEGRO,(150,100))
    ingrese_su_nombre = generar_texto("Ingrese su nombre",COLOR_NEGRO,(300,100))
    pantalla.blit(imagen,(0,0))
    dibujar_texto(texto_victoria,(255,160),pantalla)
    dibujar_texto(volver_al_menu,(420,700),pantalla)
    dibujar_texto(ingrese_su_nombre,(350,500),pantalla)

    txt_surface = font.render(text, True, color)
    width = max(200, txt_surface.get_width()+10)
    input_box.w = width
    pantalla.blit(txt_surface, (input_box.x+5, input_box.y+5))
    pygame.draw.rect(pantalla, color, input_box, 2)

    pygame.display.flip()#Actualiza los cambios hechos a cada vuelta que hace.