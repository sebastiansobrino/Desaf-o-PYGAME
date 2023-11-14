#Paso por valor: Se crea una copia local de la variable dentro de la funcion

def nombre(numero:int):
    pass
    numero = 2
    return "hola1"

num = 1
saludo = nombre(num)
print(saludo)

#Paso por referencia:Manejo directamente la variable

def doblar_valor(numero:int):
    numero *= 2
    return numero

num = 10
num = doblar_valor(num)
print(num)

lista = [1,2,3,4]

def copiar_lista(lista_recibida:list):
    lista_duplicada = list(lista_recibida) # lista_duplicada = lista_recibida[:] o lista_duplicada = lista_recibida.copy
    lista_duplicada[0] = 99
    return lista_duplicada

print(lista)
lista_copiada = copiar_lista(lista)
print(lista)
print(lista_copiada)


menor = 56
mayor = 23

var_aux = mayor
mayor = menor
menor = var_aux
print(mayor,menor)
