#Ejercicio 9:
#Dadas las siguientes listas:
#edades = [25,36,18,23,45]
#nombre = ["Juan","Ana","Sol","Mario","Sonia"]
#y considerando que la posición en la lista corresponde a la misma persona,
#mostar el nombre de la persona más joven



edades = [25,36,18,23,45,18]
nombre = ["Juan","Ana","Sol","Mario","Sonia","sebas"]

# bandera = True

# for i in edades: 
#     if bandera:
#         mas_joven = i
#         indice = edades.index(mas_joven)        
#         bandera = False
#     elif i < mas_joven:
#         mas_joven = i
#         indice = edades.index(mas_joven)

# persona_mas_joven = nombre[indice]

# print(f"La personas mas joven es {persona_mas_joven}")

minima_edad = edades[0]

for edad in edades:
    if minima_edad > edad:
        minima_edad = edad

for i in range(len(nombre)):
    if edades[i] == minima_edad:
        indice_minima_edad = i
        print(nombre[indice_minima_edad])
 
 