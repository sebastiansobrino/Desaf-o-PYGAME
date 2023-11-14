from enemigos import *
import random
from constantes import *

class Jefe ():
    def __init__(self,x,y,escala_uno,escala_dos,path,vida) -> None:
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image,(escala_uno,escala_dos))
        self.rect = pygame.Rect(x,y,escala_uno,escala_dos) #De esta forma se obtiene el rec sin darle los valores
        self.vida = vida
        self.vida_restante = vida

    def dibujar_nave(self,pantalla):
        pantalla.blit(self.image,self.rect)

    def disparar(self,grupo,lista_posiciones):
        for posiciones in lista_posiciones:
            nuevo_disparo = Disparo((self.rect.centerx + posiciones), self.rect.bottom)
            grupo.add(nuevo_disparo)

    def moverse(self):
        bandera = random.randint(0,1)
        if bandera == 0 and self.rect.x < 710:
            self.rect.x = self.rect.x + 30
        elif bandera == 1 and self.rect.x > 50:
            self.rect.x = self.rect.x - 30
    
    def dibujar_vida(self,pantalla):
        pygame.draw.rect(pantalla,COLOR_ROJO,(self.rect.x,(self.rect.top - 10),self.rect.width, 15))
        if self.vida > 0:
            pygame.draw.rect(pantalla,COLOR_VERDE,(self.rect.x,(self.rect.top - 10),int(self.rect.width *(self.vida_restante / self.vida)), 15))

    def recibir_daño(self,disparos,rect_nave_aliada):
        if len(disparos) > 0:
            for disparo in disparos:
                if disparo.rect.colliderect(rect_nave_aliada):
                    self.vida_restante = self.vida_restante - 10
                    disparos.remove(disparo)

