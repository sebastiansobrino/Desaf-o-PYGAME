class Calculadora ():
    def __init__(self,valor_uno,valor_dos) -> None:
        self.__valor_uno = valor_uno
        self.__valor_dos = valor_dos
        
    def sumar (self):
        return f"La suma es {self.__valor_uno + self.__valor_dos}"
    
    def resta (self):
        return f"La resta es {self.__valor_uno - self.__valor_dos}"
    
    def division (self):
        return f"La division es {self.__valor_uno / self.__valor_dos}"

    def multiplicacion (self):
        return f"La multiplicacion es {self.__valor_uno * self.__valor_dos}" 