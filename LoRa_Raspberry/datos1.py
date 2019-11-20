import sys
import os

nodo=str(sys.argv[1])
path = "//home//pi//Desktop//data"
filename = "nodo"+nodo+".txt"
a = os.path.exists(path+filename)
hola = nodo + ",0,0,0,0,0,0,0$"
#9,1,2,3,4,5,6,0$
if not a:
    f = os.path.join(path,filename)
    data = open(f,'w')
    data.write(hola)
    data.close()    


"""
import sys
import os
import pynmea2
path = "/home/pi/Desktop/data/"
dir = os.listdir(path)
for f in dir:
    print(f)
    file = os.path.join(path,f)
    data = open(file, "r").readlines()
    dataLoRa = data[0].split("$")[0]
    dataGNSS = data[0].split("$")[1]
    LoRa = dataLoRa[0].split(",") 
    if len(dataGNSS) > 10:
        msg = pynmea2.parse(dataGNSS)
    else:
        msg = pynmea2.parse("GNGGA,0,0,N,0,W,0,0,0,0,M,0")
    print(int(dataLoRa[0]))

"""
