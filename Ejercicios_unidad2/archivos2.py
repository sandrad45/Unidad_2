file = open ("devices.txt", "r")
bus  = input('Que dispositivo desea buscar? ')
devices =[]
for line in file:
    line = line.strip()
    devices.append (line)
print (line)
file.close()
   