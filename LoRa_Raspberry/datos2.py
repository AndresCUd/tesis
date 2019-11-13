import sys
import os
nodo=str(sys.argv[1])
path = "//home//pi//Desktop//data"
filename = "nodo"+nodo+".txt"
file = os.path.join(path,filename)
data = open(file,'r').readlines()
lastData = data[len(data) - 1]
data =  lastData.split(",") 
if data[0] == nodo:
    exec("Bien")

