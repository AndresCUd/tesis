import os 
import os
path = "//home//pi//Desktop//LoRa//"
filename = "modo.txt"
file = os.path.join(path,filename)
data = open(file,'r').readlines()
try:
    if data == 0:
        print("")
except :
    exec("data")

