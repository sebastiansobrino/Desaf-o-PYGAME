class CuentaBancaria():
    def __init__(self,titular,saldo) -> None:
        self.titular = titular
        self.__saldo = saldo

    @property
    def saldo (self):
        return self.__saldo


    def depositar(self,deposito):
        self.__saldo = self.__saldo + deposito
        return f"Deposito {deposito} y su saldo actual es {self.__saldo}"
    
    def retiro (self,retiro):
        self.__saldo = self.__saldo - retiro
        return f"retiro {retiro} y su saldo actual es {self.__saldo}"