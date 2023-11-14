import pygame


class Disparo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Sebastian\Desktop\Facultad\Programacion_l\trabajo_pygame\Recursos\Nave\disparo_nave.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        

    def update(self,aliado):
        if aliado == True:
            self.rect.y -= 5
        else:
            self.rect.y += 5        

