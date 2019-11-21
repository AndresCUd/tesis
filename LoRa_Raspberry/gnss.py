import serial
import time, os
import pynmea2
import sys
import os
from datetime import datetime

nodo=str(sys.argv[1])
bw=str(sys.argv[2])
maxCurrent=str(sys.argv[3])
paqueteEnviado=str(sys.argv[4])
paqueteRecibido=str(sys.argv[5])
tiempoEnvio =str(sys.argv[6])
RSSI=str(sys.argv[7])
payloadlength=str(sys.argv[8])
i = 0
infoLora = str(nodo) + ','+ str(bw) + ','+ str(maxCurrent)+ ','+ str(paqueteEnviado) + ','+ str(paqueteRecibido) + ','+ str(tiempoEnvio) + ','+ str(RSSI) + ','+ str(payloadlength)
data = ''
# nodo.txt se refiere a la  informacion propia de nodo tomanda desde el sensor
# Se deja un tiempo para que el GNSS inicie y de informacion util de ubicacion

fi=open("/home/pi//Desktop/data/nodo"+ str(nodo)+".txt", "r")
contente =fi.read()
def line_prepender(nodo, line):  
    with open("/home/pi//Desktop/data/nodo"+ str(nodo)+".txt", "w") as f:
        f.seek(0,0)
        f.write(str(line)+'\n'+contente)
        f.close()
now = datetime.now()

try:
    port = serial.Serial(port="/dev/ttyACM0",
                        baudrate=9600,
                        timeout=0.1,
                        bytesize=serial.EIGHTBITS)
    port.close()
    port.open()
    while True:
        data = port.readline()
        if (data.startswith("$GNGGA")):
            nmea = str(infoLora) +'_'+ str(data.rstrip('$\r\n')) +'_'
            msg = pynmea2.parse(data)
            if msg.gps_qual == 1:
                i = 1
                line_prepender(nodo,nmea)
        if i == 1:
            break
        now2 = datetime.now()
        asd = now2 -now
        if asd.seconds > 60:
            break
except :
    nmea =nodo+",0,0,0,0,0,0,0$0,0,0,0,0,0,0,0,000,0,0,0,000,0 \n"
    line_prepender(nodo,nmea)


 
"""
    while (port.in_waiting > 0):
        txt += port.read(1)
        data += txt
             data = ser.readline()
     if (data.startswith("$GPGGA")):
        if (txt == "$"):
            if ("GNGGA" in data):
                #msg = pynmea2.parse(data[0:len(data) - 3])
                nmea = infoLora + '$'+ data[0:len(data) - 3]
                if msg.latitude != 0:
                    i = 1
                line_prepender(nodo,nmea)
                data = ''
            data = ''
        txt = ''
    if i == 1:
        break
port.close()

python  /home/pi/Desktop/LoRa/gnss.py 9 0 0 0 0 0 0 0

                nmea = infoLora +','+str(msg.num_sats) + ',' + str(
                    msg.horizontal_dil) + ',' + str(msg.latitude) + ',' + str(
                        msg.longitude) + ',' + str(msg.altitude) + ',' + str(
                            msg.gps_qual) + ',' 
"""



#4.6349203333333335,-74.06839783333334
#4.6356665  ,-74.0682755