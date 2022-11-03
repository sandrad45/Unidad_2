'''
Autor: González Manzano Sandra Dania 
Fecha: 20 de octubre del 2022
'''
file = open("devices.txt","r"); 
for line in file: 
    line = line.strip()
    if "Switch" in line:
     print(line)
bus  = input('Que dispositivo desea buscar? ')
res = False
for line in file: 
    line = line.strip()
    if bus in line: 
     res = True
     print(line)
if not res:
  print('No se encontro')
file.close()
