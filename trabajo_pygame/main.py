import pygame
from personaje import *
from enemigos import *
from disparos import *
from constantes import *
from biblioteca import *
from primer_nivel import *
from segundo_nivel import *
from tercer_nivel import *
from puntaje import *

pygame.init()

pantalla = pygame.display.set_mode([1000, 1000]) 
pygame.display.set_caption("Space Intruders")


disparos_nave = pygame.sprite.Group() #Grupo disparos de la nave.
enemigos = pygame.sprite.Group() #Grupo enemigos.

#Declaramos la bandera.
bandera_primer_nivel = False
bandera_segundo_nivel = False
bandera_tercer_nivel = False
bandera_continuar_jugando = None #Esta bandera se usa para retornar la nave de los niveles o como parametro para saber si se sigue jugando.
menu_puntaje = False
menu = True

running = True

#Son dos variables que se usan para determinar el temporizador de los 3 niveles.
segundos = "15"
segundos_dos = "30"
fin_tiempo = False

lista_puntajes = leer_csv("puntaje")

#Se inicia el mixer de musica y se declara el sonido de los disparos de la nave.
sonido_disparo = pygame.mixer.Sound(r"C:\Users\Sebastian\Desktop\Facultad\Programacion_l\trabajo_pygame\Recursos\musica\Sonido-de-disparo.wav")
pygame.mixer.init()
pygame.mixer.music.set_volume(0.03)
pygame.mixer.music.load(r"C:\Users\Sebastian\Desktop\Facultad\Programacion_l\trabajo_pygame\Recursos\musica\F-777 - Space Battle.mp3")
pygame.mixer.music.play(-1)

while running: #Comienza el bucle

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            posicion_mouse = list(event.pos)

            if menu_puntaje == False:

                if(posicion_mouse[0] > 420 and posicion_mouse[0] < 583) and (posicion_mouse[1] > 655 and posicion_mouse[1] < 742): #Puntaje
                    menu_puntaje = True

                elif (posicion_mouse[0] > 418 and posicion_mouse[0] < 577) and (posicion_mouse[1] > 523 and posicion_mouse[1] < 633):#Jugar
                    bandera_primer_nivel = True
                    nave = Nave(300,800,100,100,0,100,sonido_disparo)

                elif (posicion_mouse[0] > 413 and posicion_mouse[0] < 595) and (posicion_mouse[1] > 790 and posicion_mouse[1] < 885):#Salir
                    running = False
            else:
                if(posicion_mouse[0] > 312 and posicion_mouse[0] < 648) and (posicion_mouse[1] > 911 and posicion_mouse[1] < 987): #Volver al menu desde puntaje.
                    menu_puntaje = False
                    menu = True

    if menu_puntaje == True:
        blitear_puntajes(lista_puntajes,pantalla)
        menu = False

    elif bandera_primer_nivel == True: #Arranca el primer nivel una vez que se selecciona jugar
        bandera_continuar_jugando = primer_nivel(nave,segundos,fin_tiempo) #Devuelve el objeto nave o el str "cerrar juego"
        bandera_primer_nivel = False
        menu = False

        if bandera_continuar_jugando != "cerrar juego": #Caso donde el jugador gana el nivel
            bandera_segundo_nivel = True
            transicionar_nivel(pantalla,1)
        else:
            running = False

    elif bandera_segundo_nivel == True:
        bandera_continuar_jugando = segundo_nivel(nave,segundos_dos,fin_tiempo)#Devuelve el objeto nave, el str "cerrar juego" o False si pierde el usuario y devuelve al menu
        bandera_segundo_nivel = False
        
        if bandera_continuar_jugando == "cerrar juego":
            running = False
        elif bandera_continuar_jugando != False:
            transicionar_nivel(pantalla,2)
            bandera_tercer_nivel = True
            nave = bandera_continuar_jugando

    elif bandera_tercer_nivel == True:
        bandera_continuar_jugando = tercer_nivel(nave,segundos,fin_tiempo)#Devuelve un dict si gano el usuario el juego, el str "cerrar juego" o False si pierde el usuario y devuelve al menu
        bandera_tercer_nivel = False

        if bandera_continuar_jugando == "cerrar juego":
            running = False
        elif type(bandera_continuar_jugando) == dict:
            menu = True
            lista_puntajes = crear_puntaje(bandera_continuar_jugando,"puntaje","score")

    elif menu == True or bandera_continuar_jugando == False:
        crear_menu(pantalla)


    pygame.display.flip()#Actualiza los cambios hechos a cada vuelta que hace.

