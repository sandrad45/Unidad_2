'''
Autor: González Manzano Sandra Dania 
Fecha: 8 de noviembre del 2022
Descripciòn:
 Esta API consiste en regresar la letra de una canción definiendo el artista
 y evidentemente la canción, esta API si cuenta con un statuscode con el
 200 como consulta exitosa.
'''
import urllib.parse
import requests
'''
Las variables utilizadas son key para la clave, q_track para el
nombre de la canciòn, q_artista para definir el nombre del artista, 
y status_code para definir el status
'''
main_api = "https://api.musixmatch.com/ws/1.1/matcher.lyrics.get?"
key = "020d6a15da05a237fc1bbbb0dcdbcd15"

while True:
    artista = input("Ingrese el artista: ")
    if artista == "quit" or artista== "q":
        break
    cancion = input ("INgrese la cancion: ")
    if cancion == "quit" or cancion == "q":
        break
    url = main_api + urllib.parse. urlencode ({"q_track":cancion,"q_artist":artista,"apiKey":key})
    print ("URL:"+(url),"\n")
    json_data =status = requests.get (url).json ()
    json_status = json_data ["message"]["header"]["status_code"]
    if json_status == 200:
        json_letra =json_data ["message"]["body"]["lyrics"]["lyrics_body"]
        print ("================================================================") 
        print ("Codigo de estatus:", json_status, "La PI respondio correctamente")
        print ("================================================================") 
        print ("******************La letra de la cancion",cancion, "es:***************** \n \n",json_letra, "\n")
    elif json_status == 404:
        print ("================================================================") 
        print ("Codigo de estatus:",json_status, "No se encontro la cancion")
        print ("================================================================") 
        
    