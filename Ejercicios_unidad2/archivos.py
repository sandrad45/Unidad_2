file = open ("devices.txt", "r")
for line in file:
    line=line.strip ()
   
if "Switch" in line:
        print(line) 
   
file.close ()

