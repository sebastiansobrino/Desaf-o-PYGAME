import re
from data_stark import *

def extraer_iniciales(nombre:str):
    """
    Toma las iniciales de las palabras que integren el nombre del personaje.
    Recibe un string que representa el nombre del personaje.
    Retorna las iniciales. En caso de error, retorna N/A.
    """
    if len(nombre) != 0 and type(nombre) == str:
        if re.search("[the -]",nombre) != None:
            nombre = nombre.replace("the ", "")
            nombre = nombre.replace("-", " ")
        nombre = nombre.split()
        iniciales = ""
        for inicial in nombre:
            inicial = inicial.capitalize()
            iniciales += inicial[0] + "."
        
        return_auxiliar = iniciales
    else:
        return_auxiliar = "N/A"
    
    return return_auxiliar

def obtener_dato_formato(nombre:str):
    """
    Toma el nombre del personaje y lo formatea reemplazando los "-" por espacios y los espacios por "_".
    Recibe un string que representa el nombre del personaje.
    Retorna el nombre formateado.
    """
    if type(nombre) == str and len(nombre) != 0:
        nombre = nombre.replace("-", " ")
        nombre = re.sub(" ","_",nombre)
        nombre = nombre.lower()
        return_auxiliar = nombre
    else:
        return_auxiliar = False
    
    return return_auxiliar

def obtener_nombre_con_iniciales(heroe:dict):
    """
    Esta funcion te permite juntar el nombre del personaje formateado junto con sus iniciales.
    Recibe el diccionario del heroe.
    Retorna el nombre con las iniciales.
    """
    if type(heroe) == dict and "nombre" in heroe:
        nombre_formateado = obtener_dato_formato(heroe["nombre"])
        iniciales = extraer_iniciales(heroe["nombre"])
        return_auxiliar = (f"{nombre_formateado}({iniciales})")
    else:
        return_auxiliar = False
    
    return return_auxiliar   


def stark_imprimir_nombres_con_iniciales (lista:list):
    """
    Imprime el nombre de todos los heroes de la lista con sus iniciales.
    Recibe la lista de donde se tomaran los nombres para imprimir.
    No retorna nada. 
    """
    if type(lista) == list and len(lista) != 0:
        for heroes in lista:
            print(f"*{obtener_nombre_con_iniciales(heroes)}")
        return_auxiliar = True
    else:
        return_auxiliar = False

    return return_auxiliar

def generar_codigo_heroe(heroe:dict,id:int):
    """
    Le genera un codigo unico al heroe a traves de un id ingresado, variando por su genero.
    Recibe el heroe al que se le genera el codigo y el id al que corresponde.
    Retorna el codigo generado.
    """
    if (heroe["genero"] == "M" or heroe["genero"] == "F" or heroe["genero"] == "NB") and len(heroe["genero"]) != 0:
        genero = heroe["genero"]
        id = str(id)
        contador = 0
        codigo = ""
        
        if genero == "M":
            codigo_de_genero = "1"
        
        elif genero == "F":
            codigo_de_genero = "2"
        
        else:
            codigo_de_genero = "0"
        
        while len(codigo) != 10:
            id = id.zfill(contador)
            codigo = f"{genero}-{codigo_de_genero}{id}"
            contador += 1 
        
        return_auxiliar = codigo
    
    else:
        return_auxiliar = "N/A"
    
    return return_auxiliar

def agregar_codigo_heroe(diccionario:dict,id:int):
    '''
    Tiene como parametro el diccionario e id del heroe.
    Agrega la clave "Codigo_heroe" en el diccionario y el valor.
    Retorta True si logro agregarlo con exito.
    '''
    return_auxiliar = False
    
    if (len(diccionario) > 0):
            diccionario ["codigo_heroe"] = generar_codigo_heroe(diccionario,id)
            if (len(diccionario["codigo_heroe"]) == 10):
                return_auxiliar = True
    
    return return_auxiliar

def stark_generar_codigos_heroes(lista:list):
    """
    Genera el codigo de todos los heroes de la lista e informa cuandos codigos se asignaron.
    Recibe la lista de heroes.
    Retorna un Str con el nombre y los codigos de los heroes ademas del numero de codigos asignados.
    """
    if len(lista) != 0 and type(lista[0]) == dict:
        id = 1
        codigos_generados = ""
        for heroes in lista:
            codigo = generar_codigo_heroe(heroes,id)
            codigos_generados += f"{obtener_nombre_con_iniciales(heroes)} | {codigo}\n"
            agregar_codigo_heroe(heroes,id)
            id = id + 1
        codigos_generados = f"{codigos_generados} ***** \nSe asignaron {id} codigos"
        
        return_auxiliar = codigos_generados
    
    else:
        return_auxiliar = False
    
    return return_auxiliar

def stark_mostrar_codigos_heroes (lista:list):
    if len(lista) > 0:
        print(stark_generar_codigos_heroes(lista))
    else:
        print("Error: lista vacia")

def sanitizar_entero(numero_str:str):
    '''
    Tiene como parametro un Str.
    Transforma un Str en un entero si es posible.
    Retorna un entero.
    '''
    if (re.search("[a-zA-Z]+", numero_str)):
        return_auxiliar = -1
    elif(re.search("-[0-9]+", numero_str)):
        return_auxiliar = -2
    elif((re.search("[-.,]+", numero_str)) or len(numero_str) == 0 or numero_str == " "):
        return_auxiliar = -3
    else:
        if (numero_str.count(" ") > 0):
            numero_str = numero_str.replace(" ","")
        numero_int = int(numero_str)
        return_auxiliar = numero_int
    
    return return_auxiliar

def sanitizar_flotante(numero_str:str):
    '''
    Tiene como parametro un Str.
    Transforma un Str en un flotante si es posible.
    Retorna un flotante.
    '''
    if (re.search("[a-zA-Z]+", numero_str)):
        return_auxiliar = -1
    elif(re.search("-[0-9]+", numero_str)):
        return_auxiliar = -2
    elif((re.search("[-,]+", numero_str)) or len(numero_str) == 0) or numero_str == " ":
        return_auxiliar = -3
    else:
        if(numero_str.count(" ") > 0):
            numero_str = numero_str.replace(" ","")
        numero_str = float(numero_str)
        return_auxiliar = numero_str
    return return_auxiliar

def sanitizar_string(valor_str:str,valor_por_defecto = "-"):
    '''
    Tiene como parametro un Str y un parametro por defecto en caso de pasar un str vacio.
    Recibe un string a sanitizar.
    Retorna un str convertido en minusculas o un valor por defecto.
    '''
    if(re.search("[0-9]+", valor_str)):
        return_auxiliar = "N/A"
    elif(len(valor_str) == 0 or valor_str == " "):
        return_auxiliar = valor_por_defecto
    else:
        if(re.search("/",valor_str)):
            valor_str.replace("/"," ")
        return_auxiliar = valor_str.lower().strip()
        
    return return_auxiliar

def sanitizar_dato(heroe:dict,clave:str,tipo_dato):
    '''
    Tiene como parametro un diccionario, una clave y el tipo de dato.
    sanitiza el valor del diccionario correspondiente a la clave y al tipo de dato recibido.
    Retorna True si logro sanitizarlo.
    '''
    if type(heroe) == dict and clave in heroe and type(tipo_dato) == str:
        tipo_dato = tipo_dato.capitalize()
        return_auxiliar = False
        hay_clave = False
        for claves in heroe:
            if (claves == clave):
                if(tipo_dato == "String" or tipo_dato == "Entero" or tipo_dato == "Flotante"):
                    if(tipo_dato == "Entero"):
                        heroe[clave] = sanitizar_entero(heroe[clave])
                    elif(tipo_dato == "Flotante"):
                        heroe[clave] = sanitizar_flotante(heroe[clave])
                    elif(tipo_dato == "String"):
                        heroe[clave] = sanitizar_string(heroe[clave],"El string escrito esta vacio")
                    return_auxiliar = True
                    hay_clave = True
                    break
                else:
                    print("Tipo de dato no reconocido")
                    hay_clave = True
        if (hay_clave == False):
            print("La clave especificada no existe en el heroe")
    else:
        return_auxiliar = False
    
    return return_auxiliar

def stark_normalizar_datos(lista:list):
    '''
    Recibe una lista.
    Sanitiza los valores de determinadas claves.
    No retorna nada.
    '''
    if len(lista) != 0:
        lista_auxiliar = ["altura","peso"]
        lista_auxiliar_dos = ["color_ojos","color_pelo","inteligencia"]
        lista_auxiliar_tres = ["fuerza"]
        for heroes in lista:
            for elementos in lista_auxiliar:
                sanitizar_dato(heroes,elementos,"flotante")
            for elementos in lista_auxiliar_dos:
                sanitizar_dato(heroes,elementos,"string")
            for elementos in lista_auxiliar_tres:
                sanitizar_dato(heroes,elementos,"Entero") 
        print("datos normalizados")
    else:
        print("Error. Lista de heroes vacia")

def stark_imprimir_indice_nombre(lista:list):
    """
    Imprime el nombre de todos los heroes separados por un guion.
    Recibe una lista de heroes.
    No retorna nada.
    """
    if len(lista) != 0:
        cadena_nombres = ""
        for heroes in lista:
            nombre = heroes["nombre"].replace("the ","")
            nombre = re.sub(" ","-",nombre)
            cadena_nombres += nombre + "-"
        print(cadena_nombres[0:-1])
    else:
        print("Error al imprimir los indices")

def generar_separador(patron:str,largo:int,imprimir = True):
    '''
    Recibe como parametro un patro, un largo y un booleano en caso de que quiera o no imprimirse.
    Genera un separador y lo imprime en caso de que se quiera.
    Retorna el separador.
    '''
    if(len(patron) > 0 and len(patron) < 3 and largo > 0 and largo < 236) and type(largo) == int and type(patron) == str:
        separador = ""
        while(len(separador) < largo):
            separador += patron
        
        if(imprimir == True):
            print(separador)
        
        return_auxiliar = separador
    else:
        return_auxiliar = "N/A"
    return return_auxiliar

def generar_encabezado(titulo:str):
    '''
    Tiene como parametro un Str que representa el titulo.
    Genera un titulo entre dos separadores.
    Retorna un string.
    '''
    if type(titulo) == str:
        separadores = generar_separador("*",167,False)
        titulo = titulo.upper()
        return_auxiliar = f"{separadores}\n{titulo}\n{separadores}"
    else:
        return_auxiliar = False
    
    return return_auxiliar


def imprimir_ficha_heroe(diccionario:dict):
    '''
    Recibe un diccionario.
    Imprime la ficha del heroe (Un string). 
    '''
    if bool(diccionario):
        stark_generar_codigos_heroes(lista_personajes)
        titulo_principal = generar_encabezado("principal")
        nombre_del_heroe = f"NOMBRE: {obtener_nombre_con_iniciales(diccionario)}"
        identidad_secreta = f"IDENTIDAD SECRETA: {(diccionario['identidad'])}"
        consultora = f"CONSULTORA: {(diccionario['empresa'])}"
        codigo_heroe = f"CODIGO DE HEROE: {diccionario['codigo_heroe']}"
        titulo_fisico = generar_encabezado("fisico")
        altura = f"ALTURA: {diccionario['altura']} Mts."
        peso = f"PESO: {diccionario['peso']} Kg."
        fuerza = f"FUERZA: {diccionario['fuerza']} N"
        titulo_señas = generar_encabezado("SEÑAS PARTICULARES")
        color_ojos = f"COLOR DE OJOS: {diccionario['color_ojos']}"
        color_pelo = f"COLOR DE PELO: {diccionario['color_pelo']}"
        print(f"""{titulo_principal}\n{nombre_del_heroe}\n{identidad_secreta}\n{consultora}\n{codigo_heroe}\n{titulo_fisico}\n{altura}\n{peso}
{fuerza}\n{titulo_señas}\n{color_ojos}\n{color_pelo}""")
    else:
        print("El diccionario se encuentra vacio")

def stark_navegar_fichas(lista:list):
    '''
    Recibe una lista.
    Imprime la ficha del primer heroe y permite imprimir la ficha del heroe anterior o posterior.
    '''
    if len(lista) != 0:
        contador = 0
        imprimir_ficha_heroe(lista[contador])
        while(True):

            if len(lista) == contador + 1:
                contador = -1
            elif len(lista) == -contador:
                contador = 0

            respuesta = input("\n[1]Ir a la izquiera. [2]Ir a la derecha [3]Salir\n")
            if(respuesta == "1"):
                contador -= 1
                imprimir_ficha_heroe(lista[contador])
            elif(respuesta == "2"):
                contador += 1
                imprimir_ficha_heroe(lista[contador])
            elif(respuesta == "3"):
                break
            else:
                print("Ingrese nuevamente su respuesta.")
            
    else:
        print("La lista se encuentra vacia.")

def imprimir_menu():
    '''
    Imprime el menu con las funciones disponibles.
    No recibe ni retorna nada
    '''
    print("Seleccione la opcion que desee saber:\n 1.Imprimir la lista de nombres junto con sus iniciales \n 2.Imprimir la lista de nombres y" 
            " el código del mismo\n 3.Normalizar datos \n 4.Imprimir índice de nombres\n 5.Navegar fichas \n 6.Salir\n >")

def menu_principal():
    '''
    Imprime el menu de opciones y pide que el usuario ingrese la opcion deseada y valida la respuesta.
    Retorna la respuesta del usuario casteada a entero. En caso contrario, retorna un -1 
    '''
    imprimir_menu()
    respuesta = input()
    return respuesta

def main (lista:list):
    '''
    Se encarga de ejecutar el programa.
    Recibe una lista como parametro.
    Imprime por consola la opcion elegida.
    '''
    if len(lista) != 0:
        while(True):
            respuesta = menu_principal()
            if(respuesta == "1"):
                stark_imprimir_nombres_con_iniciales(lista)
            elif(respuesta == "2"):
                stark_mostrar_codigos_heroes(lista)
            elif(respuesta == "3"):
                stark_normalizar_datos(lista)
            elif(respuesta == "4"):
                stark_imprimir_indice_nombre(lista)
            elif(respuesta == "5"):
                stark_navegar_fichas(lista)
            elif(respuesta == "6"):
                break
            else:
                print("Error. Ingrese nuevamente su respuesta")
    else:
        print("La lista esta vacia")






    


























