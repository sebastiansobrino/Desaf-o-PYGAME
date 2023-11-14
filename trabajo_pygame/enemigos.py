import pygame
from disparos import *
import random

def crear_enemigos(cantidad,grupo,bandera,x,y,y_dos,path):
    """
    Crea los enemigos y los agrega a un grupo para manejarlos en conjunto.
    Recibe la cantidad de enemigos a crear, el grupo donde se guardaran, la bandera, su posicion y la imagen de los enemigos.
    Retorna la bandera en True en caso de haber creado correctamente a los enemigos.
    """
    if bandera == False:     
        for i in range(cantidad):
            nuevo_enemigo_x = Enemigo(0 + i* x,y,100,100,path)  
            nuevo_enemigo_y = Enemigo(0+i*x,y_dos,100,100,path)
            grupo.add(nuevo_enemigo_x,nuevo_enemigo_y)
        bandera = True
        
        return bandera
    

class Enemigo(pygame.sprite.Sprite):
    def __init__(self,x,y,escala_uno,escala_dos,path) -> None:
        super().__init__()
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image,(escala_uno,escala_dos))
        self.rect = pygame.Rect(x,y,escala_uno,escala_dos) #De esta forma se obtiene el rec sin darle los valores

    def disparar(self,disparos_enemigo):
        nuevo_disparo = Disparo(self.rect.centerx, self.rect.bottom)
        disparos_enemigo.add(nuevo_disparo)








    
    



    




        

