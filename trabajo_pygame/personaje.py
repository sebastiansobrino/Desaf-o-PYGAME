import pygame
from disparos import *
from constantes import *

class Nave():
    def __init__(self,x,y,escala_uno,escala_dos,score,vida,sonido) -> None:
        self.imagen = pygame.image.load(r"C:\Users\Sebastian\Desktop\Facultad\Programacion_l\trabajo_pygame\Recursos\Nave\nave.png")
        self.imagen = pygame.transform.scale(self.imagen,(100,100))
        self.rect = pygame.Rect(x,y,100,100)
        self.score = score
        self.vida = vida
        self.vida_restante = vida
        self.sonido_disparo = sonido
        
    def obtener_rect(self):
        return self.rect
    
    def moverse(self,movimiento_derecha,movimiento_izquierda):
        if movimiento_derecha:
            if self.rect.x < 900:
                self.rect.x += 30
        if movimiento_izquierda:
            if self.rect.x > 0:
                self.rect.x -= 30

    def colisionar(self,disparos,enemigos):
        if len(disparos) > 0:
            for enemigo in enemigos:
                for disparo in disparos:
                    if disparo.rect.colliderect(enemigo.rect):
                        enemigos.remove(enemigo)
                        disparos.remove(disparo)
                        self.score = self.score + 100

    def dibujar_nave(self,pantalla):
        pantalla.blit(self.imagen,self.rect)
    
    def dibujar_vida(self,pantalla):
        pygame.draw.rect(pantalla,COLOR_ROJO,(self.rect.x,(self.rect.bottom + 10),self.rect.width, 15))
        if self.vida > 0:
            pygame.draw.rect(pantalla,COLOR_VERDE,(self.rect.x,(self.rect.bottom + 10),int(self.rect.width *(self.vida_restante / self.vida)), 15))

    def disparar(self,grupo):
        nuevo_disparo = Disparo(self.rect.centerx, self.rect.y)
        grupo.add(nuevo_disparo)
        self.sonido_disparo.play()
            
    def recibir_daño(self,disparos,rect_nave_aliada):
        if len(disparos) > 0:
            for disparo in disparos:
                if disparo.rect.colliderect(rect_nave_aliada):
                    self.vida_restante = self.vida_restante - 10
                    disparos.remove(disparo)
                    if self.score > 0:
                        self.score = self.score - 50


    

