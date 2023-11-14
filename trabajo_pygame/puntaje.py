from constantes import *
from biblioteca import *
import os
 

def crear_puntaje(puntaje:dict,path:str,clave:str):
    """
    Se encarga de crear el puntaje de mayor a menor generando un csv o, si este existe, agrega el puntaje al archivo.
    Recibe el puntaje nuevo, el path del archivo y la clave a ordenar.
    Retorna la lista de puntajes.
    """
    if type(puntaje) == dict and type(path) == str and type(clave) == str:
        if not(os.path.exists(path)):
            lista_puntajes = []

            lista_puntajes.append(puntaje)

            generar_csv(path,lista_puntajes)
        else:
            lista_puntajes = leer_csv(path)
            lista_puntajes.append(puntaje)
            ordenar_puntajes(lista_puntajes,clave)
            if len(lista_puntajes) > 5:
                lista_puntajes.pop(-1)
            generar_csv(path,lista_puntajes)
    
        return_auxiliar = lista_puntajes

    else:

        return_auxiliar = False

    return return_auxiliar


def blitear_puntajes(lista_puntajes:list,pantalla:pygame.surface.Surface):
    """
    Muestra en pantalla el menu de puntajes si es que existen, sino muestra el mensaje de que no se han cargado puntajes aun.
    Recibe una lista con los puntajes y la pantalla donde se blitea.
    No retorna nada.
    """
    if (type(lista_puntajes) == list or type(lista_puntajes) == bool) and type(pantalla) == pygame.surface.Surface:
        imagen = pygame.image.load(r"C:\Users\Sebastian\Desktop\Facultad\Programacion_l\trabajo_pygame\Recursos\Fondos_menus\fondo_puntaje.jpg")  
        imagen = pygame.transform.scale(imagen,(1000,1000)) 
        texto_puntaje = generar_texto("Puntajes", COLOR_BLANCO, (300,100))
        texto_menu = generar_texto("Volver al menu", COLOR_BLANCO, (300,100))
        pantalla.blit(imagen,(0,0))

        dibujar_texto(texto_menu,(330,900),pantalla)
        if type(lista_puntajes) == list and len(lista_puntajes) > 0:
            pantalla.blit(texto_puntaje,(330,200))
            y = 400  
            contador = 1
            for puntaje in lista_puntajes:
                texto = generar_texto(f"{contador}. {puntaje['nombre']}: {puntaje['score']}", COLOR_BLANCO, (150,73))
                dibujar_texto(texto,(410,y),pantalla)
                y += 80  
                contador = contador + 1
        else:
            texto = generar_texto(f"No se ingresaron puntajes", COLOR_BLANCO, (280,150))
            dibujar_texto(texto,(350,400),pantalla)
    else:
        print("No se pudo blitear el puntaje")






