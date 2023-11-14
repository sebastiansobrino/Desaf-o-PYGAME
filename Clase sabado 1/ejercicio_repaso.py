votantes_apple = 0
contador_mujeres = 0
contador_hombres = 0
contador_otros = 0
no_votantes_apple = 0
respuesta = None
promedio_edades = 100
suma_edades = 0
bandera = False
lista_nombres = []
lista_edades = []
lista_generos = []
lista_votos = []
bandera_dos = True

while True:
    respuesta = input("Seleccione la opcion:\n" 
                        "1.Cargar voto.\n"
                        "2-Cantidad de encuestados que votaron por APPLE, cuya edad no supere los 35 años.\n"
                        "3-Género que predomina en la empresa.\n"
                        "4-Porcentaje de empleados que no votaron por APPLE , siempre y cuando su género no sea Femenino o su edad se encuentre entre los 18 y 30. \n" 
                        "5-Nombre y edad de los empleados que votaron IKEA o TACO, cuya edad supere la edad promedio de todos los empleados \n"
                        "6-Salir")
    
    if respuesta == "1":
        nombre_encuestado = input("Ingrese nombre")

        edad = input("Ingrese edad")
        while int(edad) < 18 or edad.isnumeric() == False:
            edad = input("Error. Ingrese nuevamente su edad")
        edad = int(edad)

        genero = input("Ingrese genero").lower()
        while genero != "femenino" and genero != "masculino" and genero != "otro":
            genero = input("Error. Ingrese nuevamente genero").lower()

        voto = input("Ingrese voto").lower()
        while voto != "apple" and voto != "dunkin" and voto != "ikea" and voto != "taco":
            voto = input("Error. Ingrese nuevamente voto").lower()

        lista_nombres.append(nombre_encuestado)
        lista_edades.append(edad)
        lista_generos.append(genero)
        lista_votos.append(voto)
        
        bandera = True

    if bandera:

        if respuesta == "2":
            for i in range(len(lista_nombres)):
                if lista_edades[i] <= 35:
                    if lista_votos[i] == "apple": 
                        votantes_apple = votantes_apple + 1
            if votantes_apple != 0:
                print(f"{votantes_apple} encuestados votaron por apple")
            else:
                print("No hubo votos para apple")

        elif respuesta == "3":
            for i in range(len(lista_generos)):
                if lista_generos[i] == "masculino":
                    contador_hombres = contador_hombres + 1
                elif lista_generos[i] == "femenino":
                    contador_mujeres = contador_mujeres + 1
                else:
                    contador_otros = contador_otros + 1

            if contador_hombres > contador_mujeres and contador_hombres > contador_otros:
                mensaje = "Predominan los hombres"
            elif contador_mujeres > contador_hombres and contador_mujeres > contador_otros:
                mensaje = "Predominan las mujeres"
            elif contador_otros > contador_hombres and contador_otros > contador_mujeres:
                mensaje = "Predominan los otros"
            else:
                mensaje = "Ningun genero predomina sobre otro"
            print(mensaje)

        elif respuesta == "4":
            for i in range(len(lista_votos)):
                if lista_generos[i] != "femenino" or lista_edades[i] > 30:
                    if lista_votos[i] != "apple":
                        no_votantes_apple = no_votantes_apple + 1

            porcentaje_no_votantes_apple = (no_votantes_apple / len(lista_votos)) * 100

            print(f"El porcentaje de empleados que no votaron apple es: {porcentaje_no_votantes_apple}%")
        
        elif respuesta == "5":
            for i in range(len(lista_edades)):
                suma_edades = suma_edades + lista_edades[i]

            promedio_edades = suma_edades / len(lista_edades)

            for i in range(len(lista_edades)):
                if lista_edades[i] > promedio_edades:
                    if lista_votos[i] == "ikea" or lista_votos[i] == "taco":
                        print("Nombre: {0}, Edad: {1}".format(lista_nombres[i],lista_edades[i]))
                        bandera_dos = False
            if bandera_dos:
                print(f"No se ingresaron votantes de IKEA o TACO que superen el promedio: {promedio_edades} años")
        
        elif respuesta == "6":
            break
    elif bandera == False:
        print("Cargue el voto antes de solicitar otra opcion")