'''
Autor: González Manzano Sandra Dania 
Fecha: 20 de octubre del 2022
'''

file = open('devices.txt','a')
newitem = ''
while True: 
    newitem = input("Agrega un nuevo elemento: ")
    if newitem == 'exit': 
        print('All Done!')
        break
file.write(newitem + "\n")
file.close()
