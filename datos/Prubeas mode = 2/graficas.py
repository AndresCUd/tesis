import os


#nodo1 = open("C://Users//Alvaro//Documents//GitHub//tesis//datos//Prubeas mode = 2//nodo1.txt","r")
#nodo3 = open("C://Users//Alvaro//Documents//GitHub//tesis//datos//Prubeas mode = 2//nodo3.txt","r")
#nodo5 = open("C://Users//Alvaro//Documents//GitHub//tesis//datos//Prubeas mode = 2//nodo5.txt","r")
nodo1 = open("C://Users//Alvaro//Desktop//tesis//datos//Prubeas mode = 2//nodo1.txt","r")
nodo3 = open("C://Users//Alvaro//Desktop//tesis//datos//Prubeas mode = 2//nodo3.txt","r")
nodo5 = open("C://Users//Alvaro//Desktop//tesis//datos//Prubeas mode = 2//nodo5.txt","r")


data1=nodo1.readlines()
data2=nodo3.readlines()
data3=nodo5.readlines()
time1 =[]
PaquetesEnviados1 = []
PaquetesRecibidos1= []
def ():
    for i in data1:
        if len(i)>5:
            data = i.split("_")
            data0 = data[0].split(",")
            if  float(data0[5]) > 0.1:
                PaquetesEnviados1.append(int(data0[3]))
                PaquetesRecibidos1.append(int(data0[4]))
                time1.append(float(data0[5]))

print(time1)
print(time2)
print(time3)












