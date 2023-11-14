from data_stark import *



def sanitizar_datos(lista:list):
    '''
    Recorre la lista y convierte al tipo de dato correcto de las keys.
    Recibe una lista.
    Retornara la lista con los tipos de datos correcto. En caso de estar vacia la lista, retorna un error.
    '''
    if len(lista) != 0:
        lista_nueva = []
        for elementos in lista:
            elementos["altura"] = float(elementos["altura"])
            elementos["peso"] = float(elementos["peso"])
            elementos["fuerza"] = float(elementos["fuerza"])
            lista_nueva.append(elementos)
    
        return_auxiliar = lista_nueva
    else:
        return_auxiliar = -1 
    
    return return_auxiliar


def imprimir_dato(dato):
    '''
    Imprime un dato por consola.
    Recibe un string. No retorna nada.
    '''
    print(dato)

def mostrar_personajes(lista:list):
    '''
    Recorre la lista y muestra en pantalla el diccionario del personaje.
    Recibe una lista.
    No retorna nada.
    '''
    if len(lista) != 0:
        for personaje in lista:
            imprimir_dato(personaje)
    else:
        imprimir_dato(-1)       

def obtener_personaje_maximo_minimo(lista:list,parametro_a_comparar:str,max_o_min):
    '''
    Recorre la lista buscando maximo o minimo teniendo en cuenta la key a comparar.
    Recibe una lista, el max o min dependiendo que queramos hallar, la key que queremos comparar.
    Retorna Max o Min.
    '''    
    if len(lista) != 0:
        personaje_max_min = lista[0]
        if max_o_min == "maximo":
            for i in range(len(lista)):
                if personaje_max_min[parametro_a_comparar] < lista[i][parametro_a_comparar]:
                    personaje_max_min = lista[i]
        elif max_o_min == "minimo":
            for i in range(len(lista)):
                if personaje_max_min[parametro_a_comparar] > lista[i][parametro_a_comparar]:
                    personaje_max_min = lista[i]
        
        return_auxiliar = personaje_max_min
        
    else:
        return_auxiliar = -1

    return return_auxiliar
    

def mostrar_personaje_maximo_por_fuerza(lista:list,parametro = "fuerza"):
    '''
    Recorre la lista comparando los personajes por la fuerza maxima.
    Recibe una lista.
    No retorna nada. Imprime en pantalla la identidad y peso del personaje mas fuerte.
    '''    
    if len(lista) != 0:
        personaje_maximo = obtener_personaje_maximo_minimo(lista,parametro,"maximo")
        for i in range(len(lista)):
            if personaje_maximo[parametro] == lista[i][parametro]:
                personaje_maximo = lista[i]
                imprimir_dato("La identidad y el peso del personaje mas fuerte es {0} y {1} respectivamente".
                format(personaje_maximo["identidad"],personaje_maximo["peso"]))
    else:
        imprimir_dato(-1)

def mostrar_personaje_minimo_por_altura(lista:list,parametro = "altura"):
    '''
    Recorre la lista comparando los personajes por la altura minima.
    Recibe una lista.
    No retorna nada. Imprime en pantalla el nombre y la identidad del personaje mas bajo.
    '''      
    if len(lista) != 0: 
        personaje_minimo = obtener_personaje_maximo_minimo(lista,parametro,"minimo")
        for i in range(len(lista)):
            if personaje_minimo[parametro] == lista[i][parametro]:
                personaje_minimo = lista[i]
                imprimir_dato("El nombre y la identidad del personaje mas bajo es {0} y {1} respectivamente".
                format(personaje_minimo["nombre"],personaje_minimo["identidad"]))
    else:
        imprimir_dato(-1)

def sacar_promedio_masculino_femenino(lista:list,parametro:str,genero:str):
    '''
    Recorre la lista para hallar un promedio de acuerdo a un parametro y al genero especificado.
    Recibe una lista
    No retorna nada. Imprime en pantalla el nombre y la identidad del personaje mas bajo.
    ''' 
    if len(lista) != 0:         
        acumulador = 0
        acumulador_de_personajes = 0
        for personajes in lista:
            if personajes["genero"].lower() == genero:
                parametro_a_sumar = personajes[parametro]
                acumulador = acumulador + parametro_a_sumar
                acumulador_de_personajes = acumulador_de_personajes + 1
        
        if acumulador_de_personajes != 0:
            return_auxiliar = acumulador / acumulador_de_personajes
        else:
            return_auxiliar = -2
    else:
        return_auxiliar = -1
    
    return return_auxiliar

def mostrar_peso_promedio_hombres(lista:list,parametro = "peso",genero = "m"):
    '''
    Muestra el peso promedio de los hombres.
    Recibe una lista
    No retorna nada. Imprime en pantalla el peso promedio.
    '''     
    if len(lista) != 0: 
        promedio = sacar_promedio_masculino_femenino(lista,parametro,genero)
        imprimir_dato(f"El peso promedio de los hombres es {round(promedio,2)} Mts")
    else:
        imprimir_dato(-1)  

def mostrar_personajes_que_superen_promedio(lista:list,parametro,genero):
    '''
    Muestra el nombre y peso de los personajes que superen el promedio hallado.
    Recibe una lista, parametro a comparar y el genero utilizado para hayar el promedio
    No retorna nada.  
    '''   
    if len(lista) != 0:    
        promedio = sacar_promedio_masculino_femenino(lista,parametro,genero)
        for personajes in lista:
            if personajes[parametro] > promedio:
                imprimir_dato("El nombre y el peso de los superheroes es {0} y {1} respectivamente".format(personajes["nombre"],personajes["peso"]))
    else:
        imprimir_dato(-1)






