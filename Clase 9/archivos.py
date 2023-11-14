import os
"""archivo = open("hola.txt","r",encoding="utf-8")

leer_archivo = archivo.read()


archivo.close()
"""
#Solo lectura
#Verificar que exista el archivo
"""
if os.path.exists("hola.txt"):

    # Abrir el archivo.Se le agrega otra contrabarra en C:
    archivo = open("C:\\Users\Sebastian\Desktop\Facultad\Programacion_l\hola.txt","r",encoding="utf-8")

    #Se manipula el archivo
    leer_archivo = archivo.read()
    print(leer_archivo,end="")



    #Se cierra
    archivo.close()"""

#Escritura
archivo = open("hola_nuevo.txt","w",encoding="utf-8")

archivo.write("te amo mucho Flor")

archivo.close()

#writelines
"""archivo = open("hola_nuevo.txt","a",encoding="utf-8")

archivo.write("\n pete")

archivo.close()"""


with open("hola.txt","r",encoding="utf-8") as archivo:
    for linea in archivo:
        print(linea, end="")