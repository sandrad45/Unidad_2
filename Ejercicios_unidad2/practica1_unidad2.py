'''
Autor: González Manzano Sandra Dania 
Fecha: 8 de Noviembre del 2022
Descripciòn:
Esta Api proviene de una plataforma basada en un diccionario web por lo que 
la función de este api es proveer la definición de cualquier palabra insertada 
por el usuario, en este caso no contiene un  código de status como en otras Apis al momento 
de hacer la consulta:image.png
'''
import urllib.parse
import requests
'''
Las variables
utilizadas fueron el userId, key y word que contiene la palabra a definir 
'''
main_api = "https://www.abbreviations.com/service/v2/defs.php?format=json&"
userID = "8193"
key = "hUR2LjqmFI1k6YSs"

while True:
    palabra = input("Ingrese la palabra: ")
    if palabra == "quit" or palabra == "q":
        break
    ur1 = main_api + urllib.parse. urlencode ({"uid":userID,"tokenid":key,"word":palabra})
    print ("URL:"+ (url))
    print ("")
    json_data = requests.get(url).json()
    json_def = json_data ["result"][0]["definition"]
    
    print("La definiciòn de",palabra, "es:")
    print(json_def,"\n")

