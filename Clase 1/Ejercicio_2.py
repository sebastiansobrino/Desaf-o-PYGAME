edad = input("Ingrese su edad")

while not(edad.isnumeric()):
    edad = input("Ingrese nuevamente su edad")

edad = int(edad)

if edad >= 18:
    print("Es mayor de edad")
elif edad >= 13 and edad <= 17:
    print("Es adolescente")
else:
    print("Es un niño")

