import pygame

pygame.init()
pantalla = pygame.display.set_mode([550, 550]) #Se crea una ventana.
imagen_rana = pygame.image.load("Agrega un sprite")
#Cambiar el tamaño de imagen
imagen_rana = pygame.transform.scale("imagen",(100,100))
rect_rana = pygame.Rect(30,100,101,101)

running = True
while running:
# Se verifica si el usuario cerro la ventana.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            lista_posicion = list(event.pos)
            rect_rana[0] = lista_posicion[0]
            rect_rana[1] = lista_posicion[1]

    #pantalla.fill(colores.COLOR_CELESTE)
    #pygame.draw.rect(pantalla,colores.RED1,rect_rana)
    #pantalla.blit(imagen_rana,rect_rana)(funde la imagen en la superficie)

    #pygame.display.flip()

pygame.quit()
        