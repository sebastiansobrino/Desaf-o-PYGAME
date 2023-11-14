from data_stark import * 
from decimal import Decimal

def mostrar_dato(dato):
    """ 
    Imprime en pantalla el dato que queremos mostrar.
    Recibe un dato, sea int, float, string, lista o diccioanario.
    No retorna nada.
    """

    print(dato)

def validar_entero(dato):
    """ 
    Valida que el string ingresado sea un numero y lo castea a Int.
    Recibe un Str.
    Retorna el Str casteado a Int.
    """

    if dato.isnumeric():
        dato = int(dato)
        return_auxiliar = dato
    else:
        return_auxiliar = False
    
    return return_auxiliar
    
def es_flotante(dato):
    """ 
    Valida que el string no contenga comas y verificar que sea un float.
    Recibe un Str.
    Retorna un booleano.
    """
    dato_cambiado = dato.replace(",","")

    if Decimal(dato_cambiado):
        return True
    else:
        mostrar_dato("Error")


def castear_a_flotante(dato):
    """ 
    Valida que el string ingresado sea un numero y lo castea a FLotante.
    Recibe un Str.
    Retorna el Str casteado a Float.
    """

    if es_flotante(dato):
        dato = dato.replace(",","")
        dato = float(dato)
        return dato
    else:
        mostrar_dato("El dato ingresado no puede ser casteado a int")    

def stark_normalizar_datos(lista:list):
    """ 
    Normaliza los datos de una lista para pasar los valores de Str a int/float segun corresponda.
    Recibe una lista.
    Retorna la lista normalizada.
    """

    return_auxiliar = False

    if type(lista) == list or len(lista) == 0:
        
        for heroes in lista:
            if type(heroes["altura"]) == str or type(heroes["peso"]) == str or type(heroes["fuerza"]) == str:
                heroes["altura"] = castear_a_flotante(heroes["altura"])
                heroes["peso"] = castear_a_flotante(heroes["peso"])
                heroes["fuerza"] = validar_entero(heroes["fuerza"])
                return_auxiliar = True

    if return_auxiliar:
        mostrar_dato("Datos normalizados")
    else: 
        mostrar_dato("Hubo un error al normalizar los datos. Verifique que la lista no este vacia"
                    "o que los datos ya no se hayan normalizado anteriormente")
    
    return return_auxiliar

def obtener_dato(diccionario:dict,clave:str):
    """ 
    Obtiene el valor de una clave dentro de un diccionario.
    Recibe un diccionario y una clave.
    Retorna el valor.
    """

    return_auxiliar = False

    if bool(diccionario) and clave in diccionario:
        return_auxiliar = diccionario[clave]
    
    return return_auxiliar

def obtener_nombre (diccionario:dict):
    """ 
    Obtiene el nombre del personaje dentro del diccionario.
    Recibe un diccionario .
    Retorna el nombre.
    """

    if bool(diccionario) and "nombre" in diccionario:
        nombre = obtener_dato(diccionario,"nombre")
        return_auxiliar = f"Nombre: {nombre}"
    else:
        return_auxiliar = False
    
    return return_auxiliar

def obtener_nombre_y_dato(diccionario:dict,clave:str):
    """ 
    Obtiene el nombre del personaje y el valor de la clave dentro del diccionario.
    Recibe un diccionario y la clave.
    Retorna el nombre con el valor de la clave.
    """

    if bool(diccionario) and clave in diccionario:
        return_auxiliar = f"{obtener_nombre(diccionario)} | {clave}: {diccionario[clave]}"
    else:
        return_auxiliar = False
    
    return return_auxiliar

def mostrar_nombre_y_dato_por_lista(lista:list,clave:str):
    """
    Se ingresa una lista de diccionarios y muestra en pantalla el nombre y el dato referido a una clave de los personajes de la lista.
    Se toma como parametro una lista de diccionarios y una clave.
    No retorna nada, muestra en pantalla
    """
    if len(lista) != 0:
        for heroes in lista:
            mostrar_dato(obtener_nombre_y_dato(heroes,clave))
    else:
        mostrar_dato(-1)


def obtener_maximo(lista:list,clave:str):
    """ 
    Obtiene el maximo de una lista.
    Recibe una lista y la clave.
    Retorna el maximo.
    """

    if len(lista) != 0:
        valor_maximo = lista[0][clave]
        for heroes in lista:
            if clave != str:
                if heroes[clave] > valor_maximo:
                    valor_maximo = heroes[clave]
            else:
                valor_maximo = False
    else: 
        valor_maximo = False
    
    return valor_maximo

def obtener_minimo(lista:list,clave:str):
    """ 
    Obtiene el minimo de una lista.
    Recibe una lista y la clave.
    Retorna el minimo.
    """
    if len(lista) != 0:
        valor_minimo = lista[0][clave]
        for heroes in lista:
            if clave != str:
                if heroes[clave] < valor_minimo:
                    valor_minimo = heroes[clave]
            else:
                valor_minimo = False
    else: 
        valor_minimo = False
    
    return valor_minimo

def obtener_dato_cantidad(lista:list,valor_max_min,clave:str):
    """ 
    Obtiene el dato que cumpla con el valor asignado.
    Recibe una lista, la clave y el valor a comparar.
    Retorna el elemento de la lista que cumpla con el valor asignado.
    """    
    if len(lista) != 0:

        lista_heroes = []

        for heroes in lista:
            if heroes[clave] == valor_max_min:
                lista_heroes.append(heroes)
        return_auxiliar = lista_heroes
    else:
        return_auxiliar = False
    
    return return_auxiliar


def stark_imprimir_heroes(lista:list):
    """ 
    Imprime la lista.
    Recibe una lista.
    Imprime la lista pero retorna False en caso de que este vacia.
    """   
    if len(lista) != 0:
        mostrar_dato(lista)
    else:
        return False

def sumar_dato_heroe(lista:list,clave:str):
    """ 
    Suma los datos de una lista.
    Recibe una lista y la clave.
    Retorna la suma.
    """   
    return_auxiliar = False

    if len(lista) != 0:
        suma = 0
        for heroes in lista:
            if type(heroes) == dict and clave in heroes and bool(heroes):
                suma = suma + heroes[clave]
                return_auxiliar = suma
            else:
                mostrar_dato(-2)
    else:
        mostrar_dato(-1)   
    
    return return_auxiliar    

def dividir(divisor:int, dividendo:float):
    """ 
    Divide dos numeros.
    Recibe un divisor y un dividendo.
    Retorna el resultado de la division.
    """   
    if divisor != 0:
        calculo = dividendo/divisor
        return_auxiliar = calculo
    else:
        return_auxiliar = False
    
    return return_auxiliar

def calcular_promedio (lista:list,clave:str):
    """ 
    Calcula el promedio de una lista usando una clave.
    Recibe una lista y una clave.
    Retorna el promedio.
    """   
    suma = sumar_dato_heroe(lista,clave)
    numero_de_heroes = len(lista)
    promedio = dividir(numero_de_heroes,suma)
    
    return promedio

def mostrar_promedio_dato(lista:list,clave:str):
    """ 
    Muestra el promedio.
    Recibe una lista y la clave.
    Retorna False en caso de que la lista este vacia o la clave de la lista sea distinto a str.
    """   

    if len(lista) != 0 and type(lista[0][clave] != str):
        mostrar_dato(f"El promedio de {clave} es: {round(calcular_promedio(lista,clave),2)}")
    else:
        return False

def imprimir_menu():
    """ 
    Imprime en consola el menu de opciones que tiene el usuario para elegir.
    No retorna ni recibe nada
    """   
    mostrar_dato("Seleccione la opcion:\n" 
                    "1.Normalizar datos.\n"
                    "2.Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB.\n"
                    "3-Recorrer la lista y determinar cuál es el superhéroe más alto de género F.\n"
                    "4-Recorrer la lista y determinar cuál es el superhéroe más alto de género M.\n"
                    "5-Recorrer la lista y determinar cuál es el superhéroe más débil de género M.\n" 
                    "6-Recorrer la lista y determinar cuál es el superhéroe más débil de género NB.\n"
                    "7-Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB.\n" 
                    "8-Determinar cuántos superhéroes tienen cada tipo de color de ojos.\n"
                    "9-Determinar cuántos superhéroes tienen cada tipo de color de pelo.\n"
                    "10-Listar todos los superhéroes agrupados por color de ojos.\n"
                    "11-Listar todos los superhéroes agrupados por tipo de inteligencia.\n"
                    "12-Salir")

def stark_menu_principal():
    """ 
    Imprime el menu y solicita al usuario que ingrese un numero correspondiente a la opcion que desea seleccionar.
    No recibe ningun parametro.
    Retorna la respuesta del usuario.
    """     
    imprimir_menu()

    numero_ingresado = input("Ingrese su respuesta")

    if numero_ingresado.isnumeric():

        if int(numero_ingresado) > 0 and int(numero_ingresado) <= 12:
            return_auxiliar = numero_ingresado
        else:
            return_auxiliar = False

    else:
        return_auxiliar = False
    
    return return_auxiliar

def listar_por_genero(lista:list,genero:str):
    """ 
    Obtiene una lista de diccionarios correspondientes a un genero especifico.
    Recibe una lista y el genero buscado
    Retorna la lista con los diccionarios que cumplan con el genero solicitado
    """   
    if len(lista) != 0:
        
        lista_genero = []
        for heroes in lista:
            if heroes["genero"] == genero:
                lista_genero.append(heroes)
        
        return_auxiliar = lista_genero
    else:
        return_auxiliar = -1
    
    return return_auxiliar

def determinar_heroe_heroina_maxima(lista:list,genero:str,clave:str):
    """ 
    Determina el heroe o heroina maximo dependiendo el parametro a comparar.
    Recibe una lista de diccionarios, el genero y la clave que se usara para determinar el maximo.
    Retorna el heroe o heroina maximo.
    """   
    if len(lista) != 0 and clave in lista[0]:    
        lista_por_genero = listar_por_genero(lista,genero)
        maximo = obtener_maximo(lista_por_genero,clave)
        return_auxiliar = obtener_dato_cantidad(lista_por_genero,maximo,clave)
    
    else:
        return_auxiliar = -1
    
    return return_auxiliar

def determinar_heroe_heroina_minimo(lista:list,genero:str,clave:str):
    """ 
    Determina el heroe o heroina minimo dependiendo el parametro a comparar.
    Recibe una lista de diccionarios, el genero y la clave que se usara para determinar el minimo.
    Retorna el heroe o heroina minimo.
    """   
    if len(lista) != 0 and clave in lista[0]:    
        lista_por_genero = listar_por_genero(lista,genero)
        minimo = obtener_minimo(lista_por_genero,clave)
        return_auxiliar = obtener_dato_cantidad(lista_por_genero,minimo,clave)
        
    else:
        return_auxiliar = -1
    
    return return_auxiliar

def mostrar_promedio_por_genero(lista:list, clave:str, genero:str):
    """ 
    Muestra el promedio el promedio por genero asociado a la clave dada.
    Recibe una lista de diccionarios, el genero y la clave que se usara para determinar el promedio.
    No retorna nada, muestra el promedio seleccionado.
    """   
    if len(lista) != 0 and clave in lista[0]: 
        lista_por_genero = listar_por_genero(lista,genero)
        mostrar_promedio_dato(lista_por_genero,clave)
    else:
        mostrar_dato(-1)

def listar_mostrar_personajes_por_parametro(lista:list,parametro_a_comparar:str,booleano =True):
    '''
    Recorre la lista para listar o mostrar personajes por parametro de color de pelo, inteligencia, color de ojos.
    Recibe una lista, parametro a comparar y un booleano seteado como True para mostrar los personajes o listarlos si se selecciona False
    No retorna nada
    '''  
    if len(lista) != 0 and parametro_a_comparar in lista[0]: 
        
        lista_parametro = []
        
        for personajes in lista:
            if parametro_a_comparar == "inteligencia":
                if personajes[parametro_a_comparar] == "":
                    personajes[parametro_a_comparar] = "Nula"
           
            if parametro_a_comparar == "color_pelo":
                if personajes[parametro_a_comparar] == "":
                    personajes[parametro_a_comparar] = "No Hair"
            
            parametro_comparado = personajes[parametro_a_comparar]
            
            lista_parametro.append(parametro_comparado)

        set_parametro = set(lista_parametro)

        for parametro in set_parametro:  
            contador = 0
            lista_personajes = []  
            
            for personajes in lista:
                if personajes[parametro_a_comparar] == parametro:
                    lista_personajes.append(personajes["nombre"])
                    contador = contador + 1
            
            if parametro_a_comparar == "color_pelo":
                if booleano:
                    mostrar_dato(f"hay {contador} personaje/s con este color de pelo: {parametro}")
                else:
                    mostrar_dato(f"Los que tienen color de pelo {parametro} es/son: {lista_personajes}")
           
            elif parametro_a_comparar == "color_ojos":
                if booleano:
                    mostrar_dato(f"hay {contador} personaje/s con este color de ojos: {parametro}")
                else:
                    mostrar_dato(f"Los que tienen color de ojos {parametro} es/son: {lista_personajes}")
            
            elif parametro_a_comparar == "inteligencia":
                if booleano:
                    mostrar_dato(f"hay {contador} personaje/s con esta inteligencia: {parametro}")
                else:
                    mostrar_dato(f"Los que tienen inteligencia {parametro} es/son: {lista_personajes}")    
    else:
        mostrar_dato(-1)


def stark_marvel_app(lista:list):
    """ 
    Funciona como menu de nuestra app. Llama a las funciones Stark para 
    Recibe una lista de diccionarios.
    No retorna nada. Imprime en pantalla dependiendo la opcion elegida por el usuario.
    """   
    if len(lista) != 0:
        bandera_normalizacion_de_datos = False
        while True:
            respuesta = stark_menu_principal()
            if respuesta == "1":
                stark_normalizar_datos(lista_personajes)
                bandera_normalizacion_de_datos = True
            elif bandera_normalizacion_de_datos == True:
                if respuesta == "2":
                    mostrar_nombre_y_dato_por_lista(listar_por_genero(lista_personajes,"NB"),"genero")
                elif respuesta == "3":
                    mostrar_nombre_y_dato_por_lista(determinar_heroe_heroina_maxima(lista_personajes,"F","altura"),"altura")
                elif respuesta == "4":
                    mostrar_nombre_y_dato_por_lista(determinar_heroe_heroina_maxima(lista_personajes,"M","altura"),"altura")
                elif respuesta == "5":
                    mostrar_nombre_y_dato_por_lista(determinar_heroe_heroina_minimo(lista_personajes,"M","fuerza"),"fuerza")
                elif respuesta == "6":
                    mostrar_nombre_y_dato_por_lista(determinar_heroe_heroina_minimo(lista_personajes,"NB","fuerza"),"fuerza")
                elif respuesta == "7":
                    mostrar_promedio_por_genero(lista_personajes,"fuerza","NB") 
                elif respuesta == "8":
                    listar_mostrar_personajes_por_parametro(lista_personajes,"color_ojos")
                elif respuesta == "9":
                    listar_mostrar_personajes_por_parametro(lista_personajes,"color_pelo")
                elif respuesta == "10":
                    listar_mostrar_personajes_por_parametro(lista_personajes,"color_ojos",False)
                elif respuesta == "11":
                    listar_mostrar_personajes_por_parametro(lista_personajes,"inteligencia",False)
                elif respuesta == "12":
                    break
                else:
                    mostrar_dato("Ingrese un dato que corresponda a alguna de las opciones dadas.")
            else:
                mostrar_dato("Debe normalizar los datos antes de seleccionar otra opción.")
    else:
        mostrar_dato(-1)

