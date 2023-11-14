class Libro():
    def __init__(self,titulo,autor,año_de_publicacion) -> None:
        self.__titulo = titulo
        self.__autor = autor
        self.__año_de_publicacion = año_de_publicacion

    def publicarse(self):
        return f"El titulo de la obra es {self.__titulo}, escrito por {self.__autor} y publicado en el año {self.__año_de_publicacion}"