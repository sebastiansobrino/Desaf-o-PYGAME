class Animal():
    def __init__(self,nombre) -> None:
        self.__nombre = nombre


class Perro(Animal):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)
        self.__ladrido = "Guau"

    def sonido(self):
        return self.__ladrido


class Gato(Animal):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)
        self.__maullido = "miau"
    
    def sonido(self):
        return self.__maullido