import os 
import os
path = "//home//pi//Desktop//LoRa//"
filename = "modo.txt"
file = os.path.join(path,filename)
data = open(file,'r').readlines()
lastData = data[len(data) - 1]
data =  lastData.split(",") 

print(data[0])