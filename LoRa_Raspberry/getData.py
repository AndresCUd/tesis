import sys
import os
nodo=str(sys.argv[1])
path = "//home//pi//Desktop//data"
filename = "nodo"+nodo+".txt"
file = os.path.join(path,filename)
data = open(file,'r').readlines()
lastData = data[len(data) - 1]
valor =  int(sys.argv[2])
ubicacion =  int(sys.argv[3])
a = 0
b =True
try:
    a = int(lastData[ubicacion-1])
except:
    b = False
if valor < 10 and b:
    if a == valor:
       exec("Bien")
else:
    if lastData[ubicacion-1] == "," and valor == 10:#coma
        exec("Bien")
    if lastData[ubicacion-1] == "." and valor == 11:#punto
        exec("Bien")
    if lastData[ubicacion-1] == "-" and valor == 12:#menos
        exec("Bien")