contador = 0
lista_nombres = []
lista_nota = []
lista_sexo = []
bandera = True
contador_dos = 0
contador_mujeres = 0
contador_hombres = 0
suma_notas_mujeres = 0

while (contador < 6): 
    nombre = input("Ingrese su nombre")
    sexo = (input("Ingrese su sexo(f o m)")).lower()
    nota = input("Ingrese su nota")

    if nombre.isalpha():
        if sexo == "f" or sexo == "m":
            if nota.isnumeric() and int(nota) <= 10:
                nota = int(nota)
                lista_nombres.append(nombre)
                lista_sexo.append(sexo)
                lista_nota.append(nota)
                contador = contador + 1
            else:
                print("No se ingreso correctamente la nota")
        else:
            print("Error. Ingreso mal el sexo")
    else:
        print("ingreso incorrectamente el nombre")

for nota in lista_nota:
    if lista_sexo[contador_dos] == "m":
        contador_hombres = contador_hombres + 1
        if bandera:
            nota_mas_baja = nota
            bandera = False
            indice = lista_nota.index(nota)            
        elif nota_mas_baja > nota:
            nota_mas_baja = nota
            indice = lista_nota.index(nota)
    else:
        suma_notas_mujeres = suma_notas_mujeres + nota
        contador_mujeres = contador_mujeres + 1
    contador_dos = contador_dos + 1

if contador_mujeres > 0:
    promedio_nota_mujeres = suma_notas_mujeres / contador_mujeres
    print(f"El promedio de nota de mujeres es: {promedio_nota_mujeres}")
else:
    print("No se ingresaron notas de mujeres")
    
if contador_hombres > 0:
    print(f"El hombre con la nota mas baja es {lista_nombres[indice]}")
else:
    print("No se ingresaron dato de hombres")

