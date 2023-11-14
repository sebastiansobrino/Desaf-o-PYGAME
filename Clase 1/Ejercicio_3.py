i = 0
numeros_pares = 0
numeros_impares = 0
menor_numero_ingresado = 0
mayor_numero_par = "No se ingreso numeros pares"
suma_positivos = 0
producto_negativos = 1

while i < 5:
    a = int(input("ingrese un numero"))

    if a != 0:
        
        if a % 2 == 0:
            numeros_pares = numeros_pares + 1
            if mayor_numero_par == "No se ingreso numeros pares":
                mayor_numero_par = a
            elif mayor_numero_par < a:
                mayor_numero_par = a
        else:
            numeros_impares = numeros_impares + 1
        i = i + 1 

        if menor_numero_ingresado == 0:
            menor_numero_ingresado = a
        elif menor_numero_ingresado > a:
            menor_numero_ingresado = a

        if a > 0:
            suma_positivos = suma_positivos + a
        else:
            producto_negativos = producto_negativos * a

    else:
        print("No puede ingresar 0 ni letras")

if producto_negativos == 1:
    producto_negativos = "No se ingresaron numeros negativos"


print(f"A. La cantidad de pares e impares es: {numeros_pares} y {numeros_impares}\n"
      f"B. El menor numero ingresado es: {menor_numero_ingresado}\n"
      f"C. El mayor de los numeros pares es: {mayor_numero_par}\n"
      f"D. La suma de los positivos es {suma_positivos}\n"
      f"E. El producto de los numeros negativos: {producto_negativos}")
    


    