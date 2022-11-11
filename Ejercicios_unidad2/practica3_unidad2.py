'''
Autor: González Manzano Sandra Dania 
Fecha: 8 de noviembre del 2022
Descripciòn:
Esta api tiene un motor de búsqueda interesante pues regresa el antónimo y el sinónimo
de una palabra ingresada por el usuario, no cuenta con un status code ya que si se
presenta un error lo hace en un diccionario diferente por lo que si se hace referencia 
'''
import urllib.parse
import requests
'''
Las variables utilizadas son userID y key en la parte de autenticaciòn en la API, y la 
variables word como parametros para capturar la palabra 
'''
main_api = "https://www.stands4.com/services/v2/syno.php?format=json&"
userID = "8193"
key = "hUR2lJQMFi1k6YSs"

while True:
    palabra = input("Ingrese la palabra ")
    if palabra == "quit" or palabra == "q":
        break
    
    ur1 = main_api + urllib.parse. urlencode ({"uid":userID,"tokenid":key,"word":palabra})
    print ("URL:" + (url) ,"\n")
    json_data = requests.get(url).json()
    json_sin = json_data ["result"][0]["synonyms"]
    json_ant = json_data ["result"][0]["antonyms"]
    print ("================================================================") 
    print ("Palabra:",palabra)
    print ("Sinonimos:",json_sin,"\n")
    print ("Antonimos",json_ant)
    print ("================================================================") 
    
    

