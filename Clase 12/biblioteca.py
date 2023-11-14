from data_stark import *
import os 
import json
import re
from decimal import Decimal

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
        print("Error")


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
        print("El dato ingresado no puede ser casteado a int")    

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
        print("Datos normalizados")
    else: 
        print("Hubo un error al normalizar los datos. Verifique que la lista no este vacia"
                    "o que los datos ya no se hayan normalizado anteriormente")
    
    return return_auxiliar

def leer_archivo(documento:str):
    """ 
    Permite abrir un archivo en modo lectura y retornar la informacion del mismo.
    Recibe un str que indica el nombre y extension del archivo a leer.
    Retorna un str con los datos del archivo
    """
    if os.path.exists(documento):
        
        with open(documento,"r",encoding="UTF-8") as archivo:
            datos = ""
            for lineas in archivo:
                datos = datos + lineas
            
            return_auxiliar = datos

    else:

        print("El path seleccionado no existe")
        return_auxiliar = False

    return return_auxiliar


def guardar_archivo(nombre_archivo:str,contenido:str):
    """
    Crea un archivo del tipo CSV si no existe y escribe el contenido o lo sobreescribe en caso que exista.
    Recibe el nombre del archivo que queremos crear o sobreescribir y el contenido a escribir.
    Retorna True si no hay errores e imprime un mensaje para avisar que se creo el archivo.
    """
    if len(nombre_archivo) != 0 and contenido != 0 and type(nombre_archivo) == str and type(contenido) == str:
        
        with open(nombre_archivo,"w",encoding="UTF-8") as archivo:
            archivo.write(f"{contenido}")
            return_auxiliar = True
            print(f"Se creó el archivo: {nombre_archivo}")

    else:

        print(f"Error al crear el archivo: {nombre_archivo}")
        return_auxiliar = False
    
    return return_auxiliar


def generar_csv(nombre_archivo:str,lista:list):
    """
    Crea un csv a traves de la informacion subtraida de una lista.
    Recibe el nombre del csv que queremos crear y la lista que usaremos para tomar la informacion.
    Retorna False en caso de que la lista este vacia.
    """
    if len(lista) != 0:

        lista_claves = lista[0].keys()
        cabecera = ",".join(lista_claves)
        valores = ""
        for elemento in lista: 
            lista_valores = []
            for valor in elemento.values():
                lista_valores.append(str(valor))
            valores = f"{valores}\n" + ",".join(lista_valores)
        
        guardar_archivo(nombre_archivo,cabecera + valores)
    
    else: 

        return False

def leer_csv(path:str):
    """
    Permite leer la informacion de un csv y retornarlo a lista para poder manejar la informacion.
    Recibe la ruta absoluta o relativa del archivo.
    Retorna la lista con la informacion.
    """
    if os.path.exists(path):

        with open (path,"r",encoding= "UTF-8") as archivo: 
            encabezado = archivo.readline()
            lista_claves = (encabezado.replace("\n","")).split(",")
            
            lista = []
            for linea in archivo:
                elemento = {}
                elemento_aux = (linea.replace("\n","")).split(",")
                for i in range(len(lista_claves)):
                    clave = lista_claves[i]
                    elemento[clave] = elemento_aux[i]
                lista.append(elemento)

            return_auxiliar = lista
    
    else: 
        return_auxiliar = False
    
    return return_auxiliar



def generar_json(nombre_archivo:str,lista:list,nombre_lista:str):
    """
    Crea un json a traves de la informacion subtraida de una lista.
    Recibe el nombre del json que queremos crear y la lista que usaremos para tomar la informacion asi como un nombre que se usara como key.
    No retorna nada.
    """
    if len(lista) != 0:

        diccionario = {}
        diccionario[nombre_lista] = lista
        with open(nombre_archivo,"w") as archivo:
            json.dump(diccionario,archivo,indent=4)
    
    else:
        
        print("La lista se encuentra vacia")

def leer_json(path:str,nombre_lista:str):
    """
    Permite leer la informacion de un json y retornarlo a lista para poder manejar la informacion.
    Recibe la ruta absoluta o relativa del archivo asi como la key para acceder a la lista.
    Retorna la lista.
    """ 
    if os.path.exists(path) and re.search("json",path) != None and type(nombre_lista) == str:
        with open(path,"r") as archivo:
            diccionario_auxiliar = json.load(archivo)
            lista = diccionario_auxiliar[f"{nombre_lista}"]
        
        return_auxiliar = lista
    else:
        return_auxiliar = False

    return return_auxiliar

def ordenar_ascendentemente(lista:list,clave:str):
    """
    Ordena una lista de diccionarios ascendente en función de la clave especificada.
    Recibe como parametro la lista a ordenar y la clave por la cual se va a realizar el orden.
    No retorna nada, imprime un mensaje para confirmar que se ordeno correctamente o si hubo un error.
    """
    if len(lista) != 0 and clave in lista[0]:

        bandera = True
        while bandera:
            bandera = False
            for i in range(len(lista) - 1):
                if lista[i][clave] > lista[i+1][clave]:
                    aux = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = aux
                    bandera = True
        
        print("lista ordenada correctamente")
    
    else:
        print("Error al ordenar los datos")


def ordenar_descendentemente(lista:list,clave:str):
    """
    Ordena una lista de diccionarios descendente en función de la clave especificada.
    Recibe como parametro la lista a ordenar y la clave por la cual se va a realizar el orden.
    No retorna nada, imprime un mensaje para confirmar que se ordeno correctamente o si hubo un error.
    """
    if len(lista) != 0 and clave in lista[0]:

        bandera = True
        while bandera:
            bandera = False
            for i in range(len(lista) - 1):
                if lista[i][clave] < lista[i+1][clave]:
                    aux = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = aux
                    bandera = True

        print("lista ordenada correctamente")
    
    else:
        print("Error al ordenar los datos")


def ordenar_lista(lista:list,clave:str):
    """
    Ordena una lista de diccionarios ascendente o descendente en función de la clave especificada y de lo que solicite el usuario.
    Recibe como parametro la lista a ordenar, la clave por la cual se va a realizar el orden y el orden que desea el usuario.
    No retorna nada, imprime un mensaje si hubo un error.
    """
    respuesta = input("Ingrese de que forma desea ordenar la lista: asc o desc").lower()
    if respuesta == "asc":
        ordenar_ascendentemente(lista,clave)
    elif respuesta == "desc":
        ordenar_descendentemente(lista,clave)
    else:
        print("Error al ingresar respuesta")


def ordenar_csv(path:str,clave:str,orden:str):
    """
    Ordena un archivo csv de forma ascendente o descendente en función de la clave especificada y de lo que solicite el usuario.
    Recibe como parametro el archivo, la clave por la cual se va a realizar el orden y el orden que desea el usuario.
    Retorna una lista con la informacion del csv ordenada.
    """
    if os.path.exists(path):
        lista = leer_csv(path)
        stark_normalizar_datos(lista)
        if orden == "asc":
            ordenar_ascendentemente(lista,clave)
        else:
            ordenar_descendentemente(lista,clave)
        return_auxiliar = lista
    else:
        return_auxiliar = "El archivo no existe"
    
    return return_auxiliar

def ordenar_json(path:str,clave:str,orden:str,nombre_lista:str):
    """
    Ordena un archivo json de forma ascendente o descendente en función de la clave especificada y de lo que solicite el usuario.
    Recibe como parametro el archivo, la clave por la cual se va a realizar el orden y el orden que desea el usuario.
    Retorna una lista con la informacion del json ordenada.
    """
    if os.path.exists(path):
        lista = leer_json(path,nombre_lista)
        if orden == "asc":
            ordenar_ascendentemente(lista,clave)
        else:
            ordenar_descendentemente(lista,clave)
        return_auxiliar = lista
    else:
        return_auxiliar = "El archivo no existe"
    
    return return_auxiliar


def imprimir_menu():
    '''
    Imprime el menu con las funciones disponibles.
    No recibe ni retorna nada
    '''
    print("Seleccione la opcion que desee saber:\n1.Normalizar datos.\n2.Generar CSV" 
            "\n3.Listar heroes del archivo CSV ordenados por altura ASC \n4.Generar JSON\n" 
            "5.Listar heroes del archivo JSON ordenados por peso DESC. \n6.Ordenar Lista por fuerza ordenar de manera ASC o DESC\n" 
            "7. Salir>")

def menu_principal():
    '''
    Imprime el menu de opciones y pide que el usuario ingrese la opcion deseada y valida la respuesta.
    Retorna la respuesta del usuario casteada a entero. En caso contrario, retorna un -1 
    '''
    imprimir_menu()
    respuesta = input()
    return respuesta

def menu(lista):
    '''
    Se encarga de ejecutar el programa.
    Recibe una lista como parametro.
    Imprime por consola la opcion elegida.
    '''
    if len(lista) != 0:
        bandera_normalizacion_de_datos = False
        while True:
            respuesta = menu_principal()
            if respuesta == "1":
                stark_normalizar_datos(lista_personajes)
                bandera_normalizacion_de_datos = True
            elif bandera_normalizacion_de_datos:
                if respuesta == "2":
                   generar_csv("heroes.csv",lista)
                elif respuesta == "3": 
                    print(ordenar_csv("heroes.csv","altura","asc"))
                elif respuesta == "4":
                    generar_json("heroes.json",lista,"heroes")
                elif respuesta == "5":
                    print(ordenar_json("heroes.json","peso","desc","heroes"))
                elif respuesta == "6":
                    ordenar_lista(lista,"fuerza")
                elif respuesta == "7":
                    break
                else:
                    print("Ingrese correc")
            else:
                print("Normalizar datos antes de seleccionar otra opcion")


