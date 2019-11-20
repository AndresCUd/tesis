import serial
import time, os
import sys
import os

nodo=str(sys.argv[1])
data=str(sys.argv[2])
f = open('/home/pi//Desktop/data/nodo'+ nodo+'.txt','r+')
content = f.read()
print(content)
print(data)
a =  data+ '\n' + content
print("Buneas")
print(a)
f.seek(0, 0)
f.write(data + '\n' + content)
f.close()