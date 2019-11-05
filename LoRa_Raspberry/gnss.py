import serial
import time, os
import pynmea2
import sys
import os

nodo=str(sys.argv[1])
bw=str(sys.argv[2])
maxCurrent=str(sys.argv[3])
paqueteEnviado=str(sys.argv[4])
paqueteRecibido=str(sys.argv[2])
RSSI=str(sys.argv[6])
payloadlength=str(sys.argv[7])
tiempoEnvio =str(sys.argv[8])
print(bw)
print(maxCurrent)
port = serial.Serial(port="/dev/ttyACM0",
                     baudrate=9600,
                     timeout=0.1,
                     bytesize=serial.EIGHTBITS)
# Inicia comunicacion serial con el sensor
port.close()
port.open()
txt = ''
data = ''
f = open('//home//pi//Desktop//data//nodo'+ nodo +'.txt', 'a+')
# nodo.txt se refiere a la  informacion propia de nodo tomanda desde el sensor
# Se deja un tiempo para que el GNSS inicie y de informacion util de ubicacion
i = 0

infoLora = str(nodo) + ','+ str(bw) + ','+ str(maxCurrent)+ ','+ str(paqueteEnviado) + ','+ str(paqueteRecibido) + ','+ str(tiempoEnvio) + ','+ str(RSSI) + ','+ str(payloadlength)
while True:
    while (port.in_waiting > 0):
        txt += port.read(1)
        data += txt
        if (txt == "$"):
            if ("GNGGA" in data):
                msg = pynmea2.parse(data[0:len(data) - 3])

                nmea = infoLora +','+str(msg.num_sats) + ',' + str(
                    msg.horizontal_dil) + ',' + str(msg.latitude) + ',' + str(
                        msg.longitude) + ',' + str(msg.altitude) + ',' + str(
                            msg.gps_qual) + '\r\n'
                f.write(nmea)
                data = ''
                i = 1
            data = ''
        txt = ''
    if i == 1:
        print(nmea)
        break
f.close()
port.close()

