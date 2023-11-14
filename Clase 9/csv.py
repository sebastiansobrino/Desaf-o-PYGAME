import os


def leer_csv(path):
    if os.path.exists(path):
        with open(path,"r",encoding="utf-8") as archivo:
            claves = archivo.readline()
            lista_claves = claves.replace("\n","")
            lista_claves = lista_claves.strip().split(",")
            lista = []

            for linea in archivo:
                elemento = {}
                elemento_aux = linea.strip().split(",")
                for i in range(len(lista_claves)):
                    clave = lista_claves[i]
                    print(elemento_aux)
                    elemento[clave] = elemento_aux[i]
                lista.append(elemento)
            return_auxiliar = lista
    else:
        return_auxiliar = False

    return return_auxiliar
 

"""puntajes = []

uno = {"nombre":"karl","puntaje":1000}
dos = {"nombre":"karlos","puntaje":500}
puntajes.append(uno)
puntajes.append(dos)"""





def generar_csv(nombre_archivo:str,lista:list):
    if len(lista) != 0:
        lista_claves = list(lista[0].keys())
        cabecera = ",".join(lista_claves)
        with open (nombre_archivo,"w",encoding="utf-8") as archivo:
            archivo.write(f"{cabecera}\n")
            for elemento in lista: 
                lista_valores_str = []
                lista_valores = list((elemento.values()))
                for value in lista_valores:
                    valor_a_str = str(value)
                    lista_valores_str.append(valor_a_str)
                valores = ",".join(lista_valores_str)
                archivo.write(f"{valores}\n")
"""
generar_csv("puntajes",puntajes)"""

def agregar_puntaje_nuevo(diccionario,csv):
    
    lista_valores_str = []
    valores = list(diccionario.values())
    for value in valores:
        valor_a_str = str(value)
        lista_valores_str.append(valor_a_str)
        valores = ",".join(lista_valores_str)
    archivo = open(csv,"a",encoding="utf-8")

    archivo.write(f"{valores}")

    archivo.close()

tres = {"nombre":"karls","puntaje":5000}

agregar_puntaje_nuevo(tres,"puntajes")

def ordenar_puntajes(lista):
    if len(lista) != 0:
        bandera = True
        for elementos in lista:
            elementos["puntaje"] = int(elementos["puntaje"])
        while bandera:
            bandera = False
            for i in range(len(lista) - 1):
                if lista[i]["puntaje"] > lista[i+1]["puntaje"]:
                    print("nm")
                    aux = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = aux
                    bandera = True
                
        


    


lista_puntajes = leer_csv("puntajes")

ordenar_puntajes(lista_puntajes)

print(lista_puntajes)