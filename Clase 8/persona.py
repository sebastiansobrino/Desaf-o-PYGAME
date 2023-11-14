class Persona():
    def __init__(self,nombre,edad) -> None:
        self.__nombre = nombre
        self.__edad = edad
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    
    def presentarse(self):
        return f"Soy {self.__nombre} y tengo {self.__edad} años"