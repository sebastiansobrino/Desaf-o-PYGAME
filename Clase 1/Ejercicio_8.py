lista = [82, 3, 49, 38, 94, 85, 95, 92, 64, 
         8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]
elementos_lista = (len(lista))
contador = 0
numero_repetido = None

for i in lista:
    contador = contador + 1
    for elemento in lista[contador:elementos_lista]:
        if i == elemento:
            numero_repetido = i
            break


if numero_repetido != None:
    print(f"El numero repetido es {numero_repetido}")
else:
    print("No se repitieron numeros")