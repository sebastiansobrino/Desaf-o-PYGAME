import pygame
from constantes import *
import os

def elegir_fuente(fuente:str,size:int):
    """
    Permite seleccionar la fuente que deseamos utilizar para generar nuestros textos.
    Recibe una fuente y el size.
    Retorna la fuente
    """
    fuente = pygame.font.SysFont(fuente, size)
    return fuente

def generar_texto(texto:str,color:tuple,escala:tuple):
    """
    Genera un texto a partir de un Str dandole una escala y renderizandolo.
    Recibe el texto, el color y la escala.
    Retorna el texto generado
    """
    if type(texto) == str and type(color) == tuple and type(escala) == tuple:
        fuente = elegir_fuente("Segoe_UI_Black",72)
        texto_generado = fuente.render(texto, True, (color))
        texto_generado = pygame.transform.scale(texto_generado,escala)
        return_auxiliar = texto_generado
    else:
        return_auxiliar = -1
    
    return return_auxiliar

def dibujar_texto(texto:pygame.surface.Surface,posicion:tuple,pantalla:pygame.surface.Surface):
    """
    Permite dibujar en pantalla el texto.
    Recibe el texto, la posicion de la pantalla y la pantalla en donde queremos que se dibuje
    No retorna nada
    """  
    if type(texto) == pygame.surface.Surface and type(posicion) == tuple and type(pantalla) == pygame.surface.Surface:
        pantalla.blit(texto,posicion)
    else:
        print(-1)

def generar_dibujar_score(valor_score:int,color:tuple,pantalla:pygame.surface.Surface,escala:tuple,posicion:tuple):
    """
    Genera el texto y dibuja el score final que veremos en pantalla una vez finalizado el juego.
    Recibe el valor del score, el color, la pantalla donde se dibujara, la escala y la posicion.
    No retorna nada. En caso de error, imprime en consola -1
    """
    if type(valor_score) == int and type(posicion) == tuple and type(pantalla) == pygame.surface.Surface and type(color) == tuple and type(escala) == tuple:
        score_final = generar_texto(f"Score: {str(valor_score)}", color, escala)
        dibujar_texto(score_final,posicion,pantalla) 
    else:
        print("Error")

def crear_menu(pantalla:pygame.surface.Surface):
    """
    Crea el menu de juego en la pantalla de pygame.
    Recibe la pantalal donde se hara el blit de las imagenes.
    No retorna nada.
    """
    if type(pantalla) == pygame.surface.Surface:
        imagen = pygame.image.load(r"C:\Users\Sebastian\Desktop\Facultad\Programacion_l\trabajo_pygame\Recursos\Fondos_menus\D7qC2kht38gp3vrqrGMGR6.jpg")  
        imagen = pygame.transform.scale(imagen,(1000,1000)) 
        texto = generar_texto("Space Intruders",COLOR_NEGRO,(400,250))
        inicio = generar_texto("Jugar",COLOR_NEGRO,(125,125))
        puntajes = generar_texto("Puntaje",COLOR_NEGRO,(125,125))
        salir = generar_texto("Salir",COLOR_NEGRO,(125,125))
        pantalla.blit(imagen,(0,0))
        dibujar_texto(texto,(320,160),pantalla)
        dibujar_texto(inicio,(440,500),pantalla)
        dibujar_texto(puntajes,(440,630),pantalla)
        dibujar_texto(salir,(440,770),pantalla)
    else:
        print("Error, no es una superficie.")
        


def crear_menu_derrota(pantalla:pygame.surface.Surface):
    """
    Crea el menu de derrota una vez que el personaje se queda sin vida bliteandolo en pantalla.
    Recibe la pantalla donde se hara el blit.
    No retorna nada.
    """
    if type(pantalla) == pygame.surface.Surface:
        imagen = pygame.image.load(r"C:\Users\Sebastian\Desktop\Facultad\Programacion_l\trabajo_pygame\Recursos\Fondos_menus\D7qC2kht38gp3vrqrGMGR6.jpg")  
        imagen = pygame.transform.scale(imagen,(1000,1000))
        texto_derrota = generar_texto("Perdiste",COLOR_NEGRO,(500,350))
        no_reintentar = generar_texto("Volver al menu",COLOR_NEGRO,(200,200))
        pantalla.blit(imagen,(0,0))
        dibujar_texto(texto_derrota,(255,160),pantalla)
        dibujar_texto(no_reintentar,(400,500),pantalla)
    else:
        print("Error, no es una superficie.")

def leer_csv(path:str):
    """
    Lee el archivo csv y devuelve una lista de diccionarios con la informacion.
    Recibe el path.
    Retorna una lista de diccionarios.
    """
    if os.path.exists(path):
        with open(path,"r",encoding="utf-8") as archivo:
            claves = archivo.readline()
            lista_claves = claves.replace("\n","")
            lista_claves = lista_claves.strip().split(",")
            lista = []

            for linea in archivo:
                elemento = {}
                elemento_aux = linea.strip().split(",")
                for i in range(len(lista_claves)):
                    clave = lista_claves[i]
                    elemento[clave] = elemento_aux[i]
                lista.append(elemento)
            return_auxiliar = lista
    else:
        return_auxiliar = False

    return return_auxiliar

def generar_csv(nombre_archivo:str,lista:list):
    """
    Genera un archivo csv a traves de la informacion de una lista.
    Recibe el nombre del archivo y la lista de diccionarios que usaremos para crear el archivo csv.
    No retorna nada.
    """
    if len(lista) != 0 and type(nombre_archivo) == str:
        lista_claves = list(lista[0].keys())
        cabecera = ",".join(lista_claves)
        with open (nombre_archivo,"w",encoding="utf-8") as archivo:
            archivo.write(f"{cabecera}\n")
            for elemento in lista: 
                lista_valores_str = []
                lista_valores = list((elemento.values()))
                for value in lista_valores:
                    valor_a_str = str(value)
                    lista_valores_str.append(valor_a_str)
                valores = ",".join(lista_valores_str)
                archivo.write(f"{valores}\n")
    else:
        print("Error al generar csv")

def agregar_puntaje_nuevo(diccionario:dict,csv:str):
    """
    Agrega al archivo csv un nuevo puntaje junto con el nombre del jugador, guardado dentro de un diccionario.
    Recibe el csv y el diccionario que guardaremos en el.
    No retorna nada.
    """
    if type(diccionario) == dict and os.path.exists(csv):
        lista_valores_str = []
        valores = list(diccionario.values())
        for value in valores:
            valor_a_str = str(value)
            lista_valores_str.append(valor_a_str)
            valores = ",".join(lista_valores_str)
        archivo = open(csv,"a",encoding="utf-8")

        archivo.write(f"{valores}")

        archivo.close()
    else:
        print("Error al agregar puntaje")

def ordenar_puntajes(lista:list,clave:str):
    """
    Ordena los puntajes de mayor a menor usando el concepto de burbujeo.
    Recibe la lista a ordenar y la clave que sera ordenada.
    No retorna nada.
    """
    if len(lista) != 0 and clave in lista[0]:
        bandera = True
        for elementos in lista:
            elementos[clave] = int(elementos[clave])
        while bandera:
            bandera = False
            for i in range(len(lista) - 1):
                if lista[i][clave] < lista[i+1][clave]:
                    aux = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = aux
                    bandera = True
    else:
        print("Error al ordenar puntaje")

def transicionar_nivel(pantalla:pygame.surface.Surface, nivel:int):
    """
    Es una funcion dedicada a transicionar entre los niveles para saltar de uno a otro una vez que se completa.
    Recibe la pantalla donde se muestra y un int que representa el nivel superado.
    No retorna nada.
    """
    if type(pantalla) == pygame.surface.Surface and type(nivel) == int:
        imagen = pygame.image.load(r"C:\Users\Sebastian\Desktop\Facultad\Programacion_l\trabajo_pygame\Recursos\Fondos_menus\fdc6217db7c49818e985b51a09319dc5.jpg")  
        imagen = pygame.transform.scale(imagen,(1000,1000))
        fuente = elegir_fuente("Segoe_UI_Black", 72)
        texto = fuente.render(f"NIVEL {nivel} PASADO", True, (255, 255, 255))
        texto_rect = texto.get_rect()
        texto_rect.center = (pantalla.get_width() // 2, pantalla.get_height() // 2)

        pantalla.blit(imagen,(0,0))
        pantalla.blit(texto, texto_rect)

        pygame.display.flip()

        pygame.time.delay(2000)  
    else:
        print("Error al transicionar de nivel")
