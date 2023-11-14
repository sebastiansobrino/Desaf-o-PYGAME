def sanitizar_datos(lista:list):
    '''
    Recorre la lista y convierte al tipo de dato correcto de las keys.
    Recibe una lista.
    Retornara la lista con los tipos de datos correcto. En caso de estar vacia la lista, retorna un error.
    '''
    if len(lista) != 0:
        for personajes in lista:
            personajes["altura"] = float(personajes["altura"])
            personajes["peso"] = float(personajes["peso"])
            personajes["fuerza"] = int(personajes["fuerza"])
            personajes["genero"] = (personajes["genero"]).lower()
            personajes["color_ojos"] = (personajes["color_ojos"]).lower()
        return_auxiliar = lista
    else:
        return_auxiliar = -1
    
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

def obtener_valor_key(diccionario:dict,clave:str):
    '''
    Obtiene el nombre del heroe que represente el diccionario.
    Recibe un diccionario.
    Retorna el valor de una key.
    '''
    if bool(diccionario) and clave in diccionario:
        valor_key = diccionario[clave]
        return_auxiliar = valor_key
    else:
        return_auxiliar = -1

    return return_auxiliar  

def imprimir_dato(valor):
    '''
    Imprime un dato por consola.
    Recibe un valor que puede ser un int,flotante o str. No retorna nada
    '''
    print(valor)

def mostrar_personajes_por_genero(lista:list,genero:str):
    '''
    Recorre la lista y muestra en pantalla el nombre de aquellos personajes con genero NB.
    Recibe una lista.
    No retorna nada
    '''
    if len(lista) != 0:
        for personaje in lista:
            if personaje["genero"] == genero:
                imprimir_dato("El nombre del personaje con genero {0} es: {1}".format(genero, obtener_valor_key(personaje,"nombre")))
    else:
        imprimir_dato(-1)


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
    Obtiene el/los elementos que cumplan con el valor asignado.
    Recibe una lista, la clave y el valor a comparar.
    Retorna una lista con el/los elementos de la lista ingresada que cumplan con el valor asignado.
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
    Determina los maximos que se encuentren en la lista.
    Recibe una lista de diccionarios, el genero y la clave que se usara para determinar el/los maximos.
    Retorna una lista con todos los heroes que cumplan con ese maximo.
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
    Determina los minimos que se encuentren en la lista.
    Recibe una lista de diccionarios, el genero y la clave que se usara para determinar el/los minimos.
    Retorna una lista con todos los heroes que cumplan con ese minimo.
    """    
    if len(lista) != 0 and clave in lista[0]:    
        lista_por_genero = listar_por_genero(lista,genero)
        minimo = obtener_minimo(lista_por_genero,clave)
        return_auxiliar = obtener_dato_cantidad(lista_por_genero,minimo,clave)
        
    else:
        return_auxiliar = -1
    
    return return_auxiliar

def mostrar_heroe_heroina_minimo(lista:list,genero:str,clave:str):
    """
    Esta funcion mostrara aquellos heroes que se consideren los minimos de la lista dependiendo la clave asignada y el genero.
    Recibe una lista, el genero y la clave a comparar.
    No retorna nada, imprime en pantalla el nombre y el valor que posee dicho personaje.
    """
    if len(lista) != 0 and clave in lista[0]:
        lista_min = determinar_heroe_heroina_minimo(lista,genero,clave)
        mostrar_nombre_y_dato_por_lista(lista_min,clave)
    else:
        imprimir_dato(-1)


def mostrar_heroe_heroina_maxima(lista:list,genero:str,clave:str):
    """
    Esta funcion mostrara aquellos heroes que se consideren los maximos de la lista dependiendo la clave asignada y el genero.
    Recibe una lista, el genero y la clave a comparar.
    No retorna nada, imprime en pantalla el nombre y el valor que posee dicho personaje.
    """
    if len(lista) != 0 and clave in lista[0]:
        lista_max = determinar_heroe_heroina_maxima(lista,genero,clave)
        mostrar_nombre_y_dato_por_lista(lista_max,clave)
    else:
        imprimir_dato(-1)
    
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
                imprimir_dato(-2)
    else:
        imprimir_dato(-1)   
    
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
    
    return round(promedio,2)

def mostrar_nombre_y_dato_por_lista(lista:list,clave:str):
    """
    Se ingresa una lista de diccionarios y muestra en pantalla el nombre y el dato referido a una clave de los personajes de la lista.
    Se toma como parametro una lista de diccionarios y una clave.
    No retorna nada, muestra en pantalla
    """
    if len(lista) != 0:
        for heroes in lista:
            imprimir_dato(obtener_nombre_y_dato(heroes,clave))
    else:
        imprimir_dato(-1)

def mostrar_promedio_dato(lista:list,clave:str):
    """ 
    Muestra el promedio.
    Recibe una lista y la clave.
    Retorna False en caso de que la lista este vacia o la clave de la lista sea str.
    """   
    if len(lista) != 0 and type(lista[0][clave] != str):
        imprimir_dato(f"El promedio de {clave} es: {calcular_promedio(lista,clave)}")
    else:
        return False

def mostrar_promedio_por_genero(lista:list,clave:str,genero:str):
    """ 
    Es una funcion que muestra el promedio separado por genero dependiendo la clave ingresada.
    Recibe una lista, el genero y la clave.
    Retorna False en caso de que la lista este vacia o la clave de la lista sea str.
    """  
    if len(lista) != 0 and type(lista[0][clave] != str):
        lista_genero = listar_por_genero(lista,genero)
        mostrar_promedio_dato(lista_genero,clave)
    else:
        imprimir_dato(-1)

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
                    imprimir_dato(f"hay {contador} personaje/s con este color de pelo: {parametro}")
                else:
                    imprimir_dato(f"Los que tienen color de pelo {parametro} es/son: {lista_personajes}")
            elif parametro_a_comparar == "color_ojos":
                if booleano:
                    imprimir_dato(f"hay {contador} personaje/s con este color de ojos: {parametro}")
                else:
                    imprimir_dato(f"Los que tienen color de ojos {parametro} es/son: {lista_personajes}")
            elif parametro_a_comparar == "inteligencia":
                if booleano:
                    imprimir_dato(f"hay {contador} personaje/s con esta inteligencia: {parametro}")
                else:
                    imprimir_dato(f"Los que tienen inteligencia {parametro} es/son: {lista_personajes}")  
    else:
        print(-1)

def mostrar_opciones():
    """
    Muestra el menu de opciones.
    No recibe ni retorna nada.
    """
    imprimir_dato(("Seleccione la opcion:\n" 
                    "1.Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB\n"
                    "2-Recorrer la lista y determinar cuál es el superhéroe más alto de género F\n"
                    "3-Recorrer la lista y determinar cuál es el superhéroe más alto de género M\n"
                    "4-Recorrer la lista y determinar cuál es el superhéroe más débil de género M\n" 
                    "5-Recorrer la lista y determinar cuál es el superhéroe más débil de género NB\n"
                    "6-Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB\n" 
                    "7-Determinar cuántos superhéroes tienen cada tipo de color de ojos.\n"
                    "8-Determinar cuántos superhéroes tienen cada tipo de color de pelo.\n"
                    "9-Listar todos los superhéroes agrupados por color de ojos.\n"
                    "10-Listar todos los superhéroes agrupados por tipo de inteligencia\n"
                    "11-Salir"))

def menu (lista:list):
    """
    Funciona como el menu principal del programa, solicitando al usuario la opcion que desea ver.
    Recibe una lista.
    No retorna nada, muestra en pantalla la opcion que el usuario solicito.
    """
    if len(lista) != 0:
        sanitizar_datos(lista)
        while True:
            mostrar_opciones()
            respuesta = input("Seleccione la opcion que desea ver: ")
            if respuesta == "1":
                mostrar_personajes_por_genero(lista,"nb")
            elif respuesta == "2":
                mostrar_heroe_heroina_maxima(lista,"f","altura")
            elif respuesta == "3":
                mostrar_heroe_heroina_maxima(lista,"m","altura")
            elif respuesta == "4":
                mostrar_heroe_heroina_minimo(lista,"m","fuerza")
            elif respuesta == "5":
                mostrar_heroe_heroina_minimo(lista,"nb","fuerza")
            elif respuesta == "6":
                mostrar_promedio_por_genero(lista,"fuerza", "nb",)
            elif respuesta == "7":
                listar_mostrar_personajes_por_parametro(lista,"color_ojos")
            elif respuesta == "8":
                listar_mostrar_personajes_por_parametro(lista,"color_pelo")
            elif respuesta == "9":
                listar_mostrar_personajes_por_parametro(lista,"color_ojos",False)
            elif respuesta == "10":
                listar_mostrar_personajes_por_parametro(lista,"inteligencia",False)
            elif respuesta == "11":
                break   
            else:
                imprimir_dato("Ingrese un dato que corresponda a alguna de las opciones dadas.")       
    else:
        imprimir_dato(-1)