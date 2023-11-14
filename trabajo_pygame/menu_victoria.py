import pygame
from biblioteca import *
from constantes import *



def mostrar_menu_victoria (score):
    """
    Se encarga de iniciar un nuevo pygame para mostrar el menu de victoria.
    Recibe el score del jugador para guardarlo en el diccionario que posteriormente se usara para blitearlo en pantalla.
    Retorna el diccionario en caso que ganemos o retorna "cerrar juego" en caso de que cerremos la pestaña.
    """
    pygame.init() #Se inicializa pygame.

    pantalla = pygame.display.set_mode([1000, 1000]) #Se crea una ventana.

    running = True

    fuente = elegir_fuente(None, 36)
    rect_puntaje = pygame.Rect(400, 650, 200, 32)
    color_actual = COLOR_NEGRO
    color = COLOR_BLANCO
    texto = ''
    diccionario = {}

    contador = 0
    running = True
    while running:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
                return_auxiliar = "cerrar juego"
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if rect_puntaje.collidepoint(event.pos):
                    color = color_actual
                elif contador != 0: #Volver al menu
                    posicion_mouse = list(event.pos)
                    if(posicion_mouse[0] > 393 and posicion_mouse[0] < 599) and (posicion_mouse[1] > 712 and posicion_mouse[1] < 807):
                        return_auxiliar = diccionario
                        running = False
            
            if contador == 0:
                
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_RETURN:
                            if contador == 0:
                                jugador = texto
                                texto = ''
                                contador = contador + 1       
                    elif event.key == pygame.K_BACKSPACE:
                        texto = texto[:-1]
                    elif len(texto) < 10:
                        texto += event.unicode

        if contador != 0:
            diccionario["nombre"] = jugador.replace(" ","")
            diccionario["score"] = score

        imagen = pygame.image.load(r"C:\Users\Sebastian\Desktop\Facultad\Programacion_l\trabajo_pygame\Recursos\Fondos_menus\D7qC2kht38gp3vrqrGMGR6.jpg")  
        imagen = pygame.transform.scale(imagen,(1000,1000))
        texto_victoria = generar_texto("Ganaste",COLOR_NEGRO,(500,350))
        volver_al_menu = generar_texto("Volver al menu",COLOR_NEGRO,(150,100))
        ingrese_su_nombre = generar_texto("Ingrese su nombre",COLOR_NEGRO,(300,100))
        pantalla.blit(imagen,(0,0))
        dibujar_texto(texto_victoria,(255,160),pantalla)
        dibujar_texto(volver_al_menu,(420,700),pantalla)
        dibujar_texto(ingrese_su_nombre,(350,500),pantalla)

        nombre_usuario = fuente.render(texto, True, color)
        pantalla.blit(nombre_usuario, (rect_puntaje.x+5, rect_puntaje.y+5))
        pygame.draw.rect(pantalla, color, rect_puntaje, 2)

        pygame.display.flip()#Actualiza los cambios hechos a cada vuelta que hace.
    
    return return_auxiliar