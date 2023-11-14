from biblioteca import *

class Pregunta():
    def __init__(self,pregunta,respuestas,respuesta_correcta) -> None:
        self.pregunta = pregunta
        self.respuestas = respuestas
        self.respuesta_correcta = respuesta_correcta

    def mostrar_pregunta(self,color,escala,pantalla,posicion):
        texto = generar_texto(self.pregunta,color,escala)
        dibujar_texto(texto,posicion,pantalla) 

    def mostrar_respuesta(self,letra:str,color,escala,pantalla,posicion):
        if letra == "a":
            texto = generar_texto(self.respuestas[0],color,escala)
            dibujar_texto(texto,posicion,pantalla) 
        elif letra == "b":
            texto = generar_texto(self.respuestas[1],color,escala)
            dibujar_texto(texto,posicion,pantalla)                         
        elif letra == "c":
            texto = generar_texto(self.respuestas[2],color,escala)
            dibujar_texto(texto,posicion,pantalla)   