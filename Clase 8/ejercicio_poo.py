from persona import * 
from libro import *  
from rectangulo import *  
from calculadora import *   
from animal import *
from cuenta_bancaria import *  
 


persona_a = Persona("Jorge","12")
libro_a = Libro("El universo en una cáscara de nuez","Stephen Hawking","2001")
rectangulo_a = Rectangulo(2,3)
calculadora = Calculadora(int(input("ingrese numero 1")), int(input("Ingrese numero 2")))
gato = Gato("Rufus")
perro = Perro("Manchi")
cuenta_bancaria = CuentaBancaria("Karl",100)

print(f"{persona_a.presentarse()}\n{libro_a.publicarse()}\n{rectangulo_a.calcular_area()}\n{rectangulo_a.calcular_perimetro()}\n"
f"{calculadora.sumar()}\n{gato.sonido()}\n{perro.sonido()}\n{cuenta_bancaria.saldo}")


