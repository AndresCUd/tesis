import os
import matplotlib.pyplot as plt
import numpy as np
import time as t

path = "C://Users//Alvaro//Desktop//tesis//datos//"
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.txt' in file:
            files.append(os.path.join(r, file))


def graficaDatos(datos):
    time =[]
    PaquetesEnviados = 0
    PaquetesRecibidos= 0
    for i in datos:
        if len(i)>2:
            data = i.split("_")
            data0 = data[0].split(",")
            PaquetesEnviados=PaquetesEnviados+1
            time.append(float(data0[5]))
        PaquetesRecibidos=PaquetesRecibidos+1
    suma = sum(time) / len(time)
    a = abs(((PaquetesEnviados-PaquetesRecibidos)/PaquetesRecibidos)*100)

    return  suma ,a

SF12_1_1 = graficaDatos(open(files[0],"r").readlines())
SF12_1_3 = graficaDatos(open(files[1],"r").readlines())
SF12_1_5 = graficaDatos(open(files[2],"r").readlines())

SF12_2_1 = graficaDatos(open(files[3],"r").readlines())
SF12_2_3 = graficaDatos(open(files[4],"r").readlines())
SF12_2_5 = graficaDatos(open(files[5],"r").readlines())

SF10_3_1 = graficaDatos(open(files[6],"r").readlines())
SF10_3_3 = graficaDatos(open(files[7],"r").readlines())
SF10_3_5 = graficaDatos(open(files[8],"r").readlines())

SF12_4_1 = graficaDatos(open(files[9],"r").readlines())
SF12_4_3 = graficaDatos(open(files[10],"r").readlines())
SF12_4_5 = graficaDatos(open(files[11],"r").readlines())

SF10_5_1 = graficaDatos(open(files[12],"r").readlines())
SF10_5_3 = graficaDatos(open(files[13],"r").readlines())
SF10_5_5 = graficaDatos(open(files[14],"r").readlines())


barWidth = 0.25

def grafPPerdids():
    plt.figure(figsize=(10,5))
    ERROR_12_1 =[SF10_3_1[1],SF10_5_1[1]]
    ERROR_12_5 =[SF10_3_5[1],SF10_5_5[1]]
    
    r1=np.arange(len(ERROR_12_1))
    r2=[x +barWidth for x in r1]
    
    plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
    plt.bar(r1,ERROR_12_1,color ='#6A5ACD',width=barWidth)
    plt.bar(r2,ERROR_12_5,color ='#6495ED',width=barWidth)
           
            
    R = 0, 1, 0.25,1.25
    plt.xlabel('Ancho de Banda BW')
    plt.xticks([r +barWidth for r in range(len(ERROR_12_1))],['125 Hz','250 Hz','500 Hz'])
    plt.ylabel('% Paqquetes Perdidos')
    plt.title('Paquetes Perdidos 100 Mensajes - Con SF = 7')
    
    plt.legend(['N1-N3','N5-N3'], loc=1, fontsize = 'large')
    
    
    label = [ERROR_12_1+ERROR_12_5]
    r4 = ERROR_12_1+ERROR_12_5
    # Text on the top of each barplot
    for i in range(len(R)):
        plt.text(x = R[i]-0.12 , y= label[0][i]+0.09, s = round(label[0][i],2), size = 12)
     
        
    plt.savefig('Paquetes_Perdidos_7.png')
    
    
    


def grafBar():
    barWidth = 0.25
    plt.figure(figsize=(10,5))
    bw_12_1 = [SF10_3_1[0],SF10_5_1[0]]
    bw_12_5 = [SF10_3_1[0],SF10_5_1[0]]
    r1=np.arange(len(bw_12_1))
    r2=[x +barWidth for x in r1]
    
    plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
    plt.bar(r1,bw_12_1,color ='#6A5ACD',width=barWidth)
    plt.bar(r2,bw_12_5,color ='#6495ED',width=barWidth)
           
            
    R = 0, 1, 0.25 ,1.25
    plt.xlabel('Ancho de Banda BW')
    plt.xticks([r +barWidth for r in range(len(bw_12_1))],['125 Hz','250 Hz','500 Hz'])
    plt.ylabel('Tiempo (Segundos)')
    plt.title('Respuesta Promedio de un paquete - Con SF = 7')
    
    plt.legend(['N1-N3','N5-N3'], loc=1, fontsize = 'xx-large')
    
    
    label = [bw_12_1+bw_12_5]
    r4 = bw_12_1+bw_12_5
    # Text on the top of each barplot
    for i in range(len(R)):
        print(R[i]-0.1)
        print(label[0][i])
        print(round(label[0][i],2))
        plt.text(x = R[i]-0.07 , y= label[0][i]+0.09, s = round(label[0][i],3), size = 12)
    plt.savefig('timepos_de envio_7.png')



grafPPerdids()