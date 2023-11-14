from biblioteca import *
import pygame 

class Pregunta():
    def __init__(self,pregunta,respuestas,respuesta_correcta) -> None:
        self.pregunta = pregunta
        self.respuestas = respuestas
        self.respuesta_correcta = respuesta_correcta

    def mostrar_pregunta(self,color,escala,pantalla,posicion):
        texto = generar_texto(self.pregunta,color,escala)
        dibujar_texto 

        