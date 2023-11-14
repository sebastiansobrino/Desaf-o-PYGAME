import pygame
from personaje import *
from enemigos import *
from constantes import *
from biblioteca import *



def primer_nivel(nave,timer,fin_tiempo):
    """
    Inicia un pygame nuevo donde se desarrolla el primer nivel del juego.
    Recibe el objeto nave que usaremos para representar nuestra nave, un timer que sera el tiempo que tiene el usuario para terminar el nivel y una bandera.
    Retorna el objeto nave si finaliza el nivel o "cerrar el juego" si se cierra la pestaña.
    """
    pygame.init()

    pantalla = pygame.display.set_mode([1000, 1000]) #Se crea una ventana.
    pygame.display.set_caption("Space Intruders")
    clock = pygame.time.Clock()

    disparos_nave = pygame.sprite.Group()
    enemigos = pygame.sprite.Group()

    personaje = nave

    bandera = False

    running = True

    imagen = pygame.image.load(r"C:\Users\Sebastian\Desktop\Facultad\Programacion_l\trabajo_pygame\Recursos\mapas\nivel_uno.png")  
    imagen = pygame.transform.scale(imagen,(1000,1000)) 

    tiempo = pygame.USEREVENT
    pygame.time.set_timer(tiempo, 1000)

    while running:
        clock.tick(100)
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
                return_auxiliar = "cerrar juego"
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    personaje.moverse(True,False)
                elif event.key == pygame.K_LEFT:
                    personaje.moverse(False,True)
                elif event.key == pygame.K_SPACE:
                    personaje.disparar(disparos_nave)
            
            if event.type == pygame.USEREVENT:
                if event.type == tiempo:
                    if fin_tiempo == False:
                        timer = int(timer) - 1 
                        if int(timer) == 0:
                            nave.score = nave.score - 100
                            fin_tiempo = True

        if int(timer) >= 1:
            texto = generar_texto ("00:" + str(timer) if int(timer) > 9 else "00:0" + str(timer),(COLOR_BLANCO),(80,80))
        else:
            texto = generar_texto ("00:0" + str(timer),(COLOR_BLANCO),(80,80))
            
        bandera = crear_enemigos(8,enemigos,bandera,125,100,200,r"C:\Users\Sebastian\Desktop\Facultad\Programacion_l\trabajo_pygame\Recursos\Enemigos\8bef5062bcbd04329ab604fe41ad9f74.png")

        personaje.colisionar(disparos_nave,enemigos)

        pantalla.blit(imagen,(0,0))#Se superpone la imagen cargada por sobre la ventana.

        personaje.dibujar_nave(pantalla)

        disparos_nave.update(True)
        disparos_nave.draw(pantalla)
        personaje.dibujar_vida(pantalla)
        
        enemigos.draw(pantalla)
        
        generar_dibujar_score(personaje.score,COLOR_BLANCO,pantalla,(100,100),(0,0))

        dibujar_texto(texto,(900,20),pantalla)

        if len(enemigos) == 0:
            return_auxiliar = personaje
            running = False

        pygame.display.flip()#Actualiza los cambios hechos a cada vuelta que hace.
    
    return return_auxiliar

