estacion_año = input("Ingrese estacion del año")
localidad = input("Ingrese localidad")
estacion_año = estacion_año.lower()
localidad = localidad.lower()
precio_base = 15000
precio_total = 0


if estacion_año == "invierno" or estacion_año == "otoño" or estacion_año == "primavera" or estacion_año == "verano":
    if localidad == "bariloche" or localidad == "cataratas" or localidad == "mar del plata" or localidad == "cordoba":

        if localidad == "bariloche":
            if estacion_año == "invierno":
                precio_total = int(precio_base * 1.20)
            elif estacion_año == "verano":
                precio_total = int(precio_base - (precio_base * 0.20))
            elif estacion_año == "otoño" or estacion_año == "primavera":
                precio_total = int(precio_base * 1.10)

        elif localidad == "cataratas":
            if estacion_año == "invierno":
                precio_total = int(precio_base - (precio_base * 0.10))
            elif estacion_año == "verano":
                precio_total = int(precio_base * 1.10)
            elif estacion_año == "otoño" or estacion_año == "primavera":
                precio_total = int(precio_base * 1.10)

        elif localidad == "mar del plata":
            if estacion_año == "invierno":
                precio_total = int(precio_base - (precio_base * 0.20))
            elif estacion_año == "verano":
                precio_total = int(precio_base * 1.20)
            elif estacion_año == "otoño" or estacion_año == "primavera":
                precio_total = int(precio_base * 1.10)

        else:
            if estacion_año == "invierno":
                precio_total = int(precio_base - (precio_base * 0.10))
            elif estacion_año == "verano":
                precio_total = int(precio_base * 1.10)
            elif estacion_año == "otoño" or estacion_año == "primavera":
                precio_total = precio_base  
        
        print(f"El precio del viaje seria ${precio_total}")
    
    else:
        print("Ingreso incorrectamente la localidad")

else:
    print("Ingreso incorrectamente la estacion del año") 




