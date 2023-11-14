edad = int(input("Ingrese edad"))
estado_civil = (input("Ingrese estado civil"))
estado_civil = estado_civil.lower()

if edad < 18 and estado_civil != "soltero":
    print("Es muy pequeño para NO ser soltero")
else:
    print ("Todo OK")