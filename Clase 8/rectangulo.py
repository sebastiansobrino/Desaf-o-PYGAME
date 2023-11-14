class Rectangulo():
    def __init__(self,base,altura) -> None:
        self.__base = base
        self.__altura = altura

    
    
    def calcular_area(self):
        return f"El area es igual a {self.__base * self.__altura}"
    
    def calcular_perimetro(self):
        return f"El perimetro es igual a {2*self.__base + 2*self.__altura}"