contador = 0
bandera = True
bandera_dos = True
precio_mas_caro = 0
fabricante_mas_caro = str 
unidades_mas_caras = 0
unidades_maximas = 0
fabricante_unidades_maximas = str
contador_jabon = 0

while (contador < 5):
    
    tipo_de_producto = (input("Ingresar tipo de producto.")).lower()
    while tipo_de_producto != "barbijo" and tipo_de_producto != "jabon" and tipo_de_producto != "alcohol":
        tipo_de_producto = (input("Error. Ingresar nuevamente tipo de producto.")).lower()

    precio = input("Ingrese precio del producto.")
    while float(precio) < 100 or float(precio) > 300:
        precio = input("Error. Ingrese nuevamente el precio del producto.")
    
    precio = float(precio)

    cantidad_de_unidades = input("Ingrese cantidad de unidades.")
    while not(cantidad_de_unidades.isdigit() and int(cantidad_de_unidades) > 0 and int(cantidad_de_unidades) <= 1000):
        cantidad_de_unidades = input("Error. Ingrese nuevamente la cantidad de unidades.")
    
    cantidad_de_unidades = int(cantidad_de_unidades)

    fabricante = input("Ingrese el fabricante")

    if tipo_de_producto == "barbijo":    
        if bandera:
            bandera = False
            precio_mas_caro = precio
            unidades_mas_caras = cantidad_de_unidades
            fabricante_mas_caro = fabricante
        elif precio_mas_caro < precio:
            precio_mas_caro = precio
            unidades_mas_caras = cantidad_de_unidades
            fabricante_mas_caro = fabricante

    if bandera_dos:
        bandera_dos = False
        unidades_maximas = cantidad_de_unidades
        fabricante_unidades_maximas = fabricante
    elif unidades_maximas < cantidad_de_unidades:
        unidades_maximas = cantidad_de_unidades
        fabricante_unidades_maximas = fabricante
        
    if tipo_de_producto == "jabon":
        contador_jabon = contador_jabon + cantidad_de_unidades
    
    contador = contador + 1

if contador_jabon == 0:
    mensaje = "No se ingresaron jabones"
else:
    mensaje = f"La cantidad de jabones ingresados fueron {contador_jabon}"

if precio_mas_caro == 0:
    mensaje_dos = "No se ingresaron barbijos"
else:
    mensaje_dos = f"El mas caro de los barbijos tiene una cantidad de : {unidades_mas_caras} y es fabricado por {fabricante_mas_caro}"


print(f"{mensaje_dos}\n"
      f"El item con mas unidades es: {fabricante_unidades_maximas} y es: {unidades_maximas}\n" 
      f"{mensaje}") 