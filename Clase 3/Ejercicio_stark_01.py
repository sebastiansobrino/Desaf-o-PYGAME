from data_stark import *
from biblioteca import *
""""  {
    "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": "79.349999999999994",
    "peso": "18.449999999999999",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Yellow",
    "fuerza": "2",
    "inteligencia": ""
  },
  lista_personajes{[]}
  """

lista_personajes = sanitizar_datos(lista_personajes)

while True:
  respuesta = input("Seleccione la opcion:\n" 
                    "1.Imprimir datos de cada personaje\n"
                    "2-Muestra la identidad y peso del superheroe con mas fuerza.\n"
                    "3-Muestra nombre e identidad del superhéroe más bajo.\n"
                    "4-determina el peso promedio de los superhéroes masculinos \n" 
                    "5-muestra nombre y peso de los superhéroes (cualquier género) los cuales su fuerza " 
                    "supere a la fuerza promedio de todas las superhéroes de género femenino \n"
                    "6-Salir")  
  
  if respuesta == "1":
    mostrar_personajes(lista_personajes)
  elif respuesta == "2":
    mostrar_personaje_maximo_por_fuerza(lista_personajes)
  elif respuesta == "3":
    mostrar_personaje_minimo_por_altura(lista_personajes)
  elif respuesta == "4":
    mostrar_peso_promedio_hombres(lista_personajes)
  elif respuesta == "5":
    mostrar_personajes_que_superen_promedio(lista_personajes,"fuerza","f")
  elif respuesta == "6":
      break
    


