import sys
import os
nodo=str(sys.argv[1])
print(nodo)
path = "//home//pi//Desktop//data"
filename = "nodo"+nodo+".txt"
file = os.path.join(path,filename)
data = open(file,'r').readlines()
lastData = data[len(data) - 1]
data =  lastData.split(",") 
print(int(data[3]))

os.system("sudo python //home//pi//Desktop//LoRa//datos1.py 0");
