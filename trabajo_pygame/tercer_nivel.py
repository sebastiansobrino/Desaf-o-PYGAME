import pygame
from personaje import *
from jefe import *
from enemigos import *
from disparos import *
from constantes import *
from biblioteca import *
from menu_victoria import *
from puntaje import *

def tercer_nivel(nave,timer,fin_tiempo):
    """
    Inicia un pygame nuevo donde se desarrolla el tercer nivel del juego, si lo supera, se muestra en pantalla el menu de victoria sino el menu de derrota.
    Recibe el objeto nave, un timer que sera el tiempo que tiene el usuario para terminar el nivel y una bandera.
    Retorna el diccionario con el puntaje si gana el usuario, "cerrar juego" en caso de que se cierre la pestaña o False si pierde el nivel.
    """
    pygame.init()

    pantalla = pygame.display.set_mode([1000, 1000]) #Se crea una ventana.
    pygame.display.set_caption("Space Intruders")

    clock = pygame.time.Clock()

    timer_segundos = pygame.USEREVENT
    pygame.time.set_timer(timer_segundos,1000)

    disparos = pygame.sprite.Group()
    disparos_jefe = pygame.sprite.Group()

    personaje = nave

    jefe = Jefe(350,150,250,200,r"C:\Users\Sebastian\Desktop\Facultad\Programacion_l\trabajo_pygame\Recursos\Enemigos\png-clipart-sprite-spaceshiptwo-spaceshipone-spacecraft-game-space-craft-fictional-character-transport.png",100)

    running = True
    return_auxiliar = True
    bandera_derrota = False

    imagen = pygame.image.load(r"C:\Users\Sebastian\Desktop\Facultad\Programacion_l\trabajo_pygame\Recursos\mapas\nivel_tres.png")  
    imagen = pygame.transform.scale(imagen,(1000,1000)) 

    while running:    
        clock.tick(100)    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return_auxiliar = "cerrar juego"
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
            
                posicion_mouse = list(event.pos)

                if bandera_derrota == True:
                    if(posicion_mouse[0] > 340 and posicion_mouse[0] < 622) and (posicion_mouse[1] > 531 and posicion_mouse[1] < 676):
                        return_auxiliar = False
                        running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    personaje.moverse(True,False)
                elif event.key == pygame.K_LEFT:
                    personaje.moverse(False,True)
                elif event.key == pygame.K_SPACE:
                    personaje.disparar(disparos)

            elif event.type == pygame.USEREVENT:
                if event.type == timer_segundos:
                    jefe.disparar(disparos_jefe,[-130,0,130])
                    jefe.moverse()
                if fin_tiempo == False:
                        timer = int(timer) - 1 
                        if int(timer) == 0:
                            nave.score = nave.score - 100
                            fin_tiempo = True
                            timer = "00"

        if int(timer) >= 1:
            texto = generar_texto ("00:" + str(timer) if int(timer) > 9 else "00:0" + str(timer),(COLOR_BLANCO),(80,80))
        else:
            texto = generar_texto ("00:" + str(timer),(COLOR_BLANCO),(80,80))
        
        if return_auxiliar == True:
            pantalla.blit(imagen,(0,0))#Se superpone la imagen cargada por sobre la ventana.
        
            personaje.dibujar_nave(pantalla)
            personaje.dibujar_vida(pantalla) 
            disparos.draw(pantalla)
            disparos.update(True)
            personaje.recibir_daño(disparos_jefe,personaje.rect)
            
            jefe.dibujar_nave(pantalla)
            jefe.dibujar_vida(pantalla)
            disparos_jefe.draw(pantalla)
            disparos_jefe.update(False)
            jefe.recibir_daño(disparos,jefe.rect)

            generar_dibujar_score(personaje.score,COLOR_BLANCO,pantalla,(100,100),(0,0))

            dibujar_texto(texto,(900,20),pantalla)

            if personaje.vida_restante <= 0:
                crear_menu_derrota(pantalla)
                bandera_derrota = True
            elif jefe.vida_restante <= 0:
                personaje.score = personaje.score + 1000
                return_auxiliar = mostrar_menu_victoria(personaje.score)
                running = False

        pygame.display.flip()#Actualiza los cambios hechos a cada vuelta que hace.
    
    return return_auxiliar