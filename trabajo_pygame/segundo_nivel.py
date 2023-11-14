import pygame
from personaje import *
from enemigos import *
from disparos import *
from constantes import *
from biblioteca import *
import random

def segundo_nivel(nave,timer,fin_tiempo):
    """
    Inicia un pygame nuevo donde se desarrolla el segundo nivel del juego.
    Recibe el objeto nave que usaremos para representar nuestra nave, un timer que sera el tiempo que tiene el usuario para terminar el nivel y una bandera.
    Retorna el objeto nave si finaliza el nivel, "cerrar el juego" si se cierra la pestaña o false en caso de perder el nivel.
    """
    pygame.init()

    pantalla = pygame.display.set_mode([1000, 1000]) #Se crea una ventana.
    pygame.display.set_caption("Space Intruders")

    clock = pygame.time.Clock()

    timer_segundos = pygame.USEREVENT
    pygame.time.set_timer(timer_segundos,1000)
    
    disparos = pygame.sprite.Group()
    disparos_enemigo = pygame.sprite.Group()
    enemigos = pygame.sprite.Group()

    personaje = nave

    bandera = False

    running = True

    bandera_continuar = True

    return_auxiliar = None

    bandera_derrota = False

    imagen = pygame.image.load(r"C:\Users\Sebastian\Desktop\Facultad\Programacion_l\trabajo_pygame\Recursos\mapas\nivel_dos.png")  
    imagen = pygame.transform.scale(imagen,(1000,1000)) 

    tiempo = pygame.USEREVENT
    pygame.time.set_timer(tiempo, 1000)

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
                        bandera_continuar = False
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
                    if len(enemigos) >= 5:
                        enemigos_que_disparan = random.sample(list(enemigos), 5)
                    else:
                        enemigos_que_disparan = random.sample(list(enemigos), len(enemigos))
                    for enemigo in enemigos_que_disparan:
                        enemigo.disparar(disparos_enemigo)
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

        if bandera_continuar:
            bandera = crear_enemigos(8,enemigos,bandera,125,100,200,r"C:\Users\Sebastian\Desktop\Facultad\Programacion_l\trabajo_pygame\Recursos\Enemigos\images.png")

            personaje.colisionar(disparos,enemigos)
            personaje.recibir_daño(disparos_enemigo,personaje.rect)

            pantalla.blit(imagen,(0,0))#Se superpone la imagen cargada por sobre la ventana.
            
            personaje.dibujar_nave(pantalla)
            disparos.draw(pantalla)
            personaje.dibujar_vida(pantalla)
            disparos.update(True)

            enemigos.draw(pantalla)
            disparos_enemigo.update(False)
            disparos_enemigo.draw(pantalla)
            
            generar_dibujar_score(personaje.score,COLOR_BLANCO,pantalla,(100,100),(0,0))

            dibujar_texto(texto,(900,20),pantalla)

            if len(enemigos) == 0:
                running = False
                return_auxiliar = personaje
        
        if personaje.vida_restante <= 0:
            crear_menu_derrota(pantalla)
            bandera_derrota = True

        pygame.display.flip()#Actualiza los cambios hechos a cada vuelta que hace.

    return return_auxiliar
    