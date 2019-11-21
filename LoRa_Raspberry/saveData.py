import serial
import time, os
import sys
import os

nodo=str(sys.argv[1])
data=str(sys.argv[2])
fi = open('/home/pi//Desktop/data/nodo'+ nodo+'.txt','r')
content = fi.read()
def line_prepender(nodo, line):  
    with open("/home/pi//Desktop/data/nodo"+ str(nodo)+".txt", "w") as f:
        f.seek(0,0)
        f.write(str(line)+'\n'+content)
        f.close()  
content1 = fi.readline()
if content1 > 30:
    line_prepender(nodo,data)
else:
    datos = nodo +",0,0,0,0,0,0,0_$ \n"
    line_prepender(nodo,datos)
fi.close()


"""
C:\Users\Alvaro\Desktop\datos
fi = open('C:/Users/Alvaro/Desktop/datos/nodo9.txt','r')
content = fi.readline()
"""