lista = [82, 3, 49, 38, 94, 85, 97, 92, 64, 
         8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]

numero_mayor = lista[0]

for i in lista: 
    
    if numero_mayor < i:
        numero_mayor = i

print(f"El numero mas alto de la lista es {numero_mayor}")