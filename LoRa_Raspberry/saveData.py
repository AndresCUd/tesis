import serial
import time, os
import sys
import os

nodo=str(sys.argv[1])
try:
    data=str(sys.argv[2])
except:
    data = ""
fi = open('/home/pi//Desktop/data/nodo'+ nodo+'.txt','r')
content = fi.read()
def line_prepender(nodo, line):  
    with open("/home/pi//Desktop/data/nodo"+ str(nodo)+".txt", "w") as f:
        f.seek(0,0)
        f.write(str(line)+'\n'+content)
        f.close()  
content1 = fi.readline()
if data > 30:
    line_prepender(nodo,data)
else:
    msg = nodo +",0,0,0,0,0,0,0_$ \n"
    line_prepender(nodo,msg)
fi.close()


"""
C:\Users\Alvaro\Desktop\datos
fi = open('C:/Users/Alvaro/Desktop/datos/nodo9.txt','r')
content = fi.readline()
"""