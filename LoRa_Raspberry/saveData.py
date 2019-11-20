import serial
import time, os
import sys
import os

nodo=str(sys.argv[1])
data=str(sys.argv[2])
fi = open('/home/pi//Desktop/data/nodo'+ nodo+'.txt','r')
content = fi.read()
print(data)
def line_prepender(nodo, line):  
    with open("/home/pi//Desktop/data/nodo"+ str(nodo)+".txt", "w") as f:
        f.seek(0,0)
        f.write(str(line)+'\n'+contente)

line_prepender(nodo,data)
f.close()  
myfile.close()