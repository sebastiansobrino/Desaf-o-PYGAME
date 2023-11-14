lista = [82, 3, 49, 38, 94, 85, 97, 92, 64, 
         8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]

numeros_pares = []

for i in lista:
    if i % 2 == 0:
        numeros_pares.append(i)

print(f"Los numeros pares son: {numeros_pares}")