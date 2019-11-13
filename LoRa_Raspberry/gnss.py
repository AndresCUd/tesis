import serial
import time, os
import pynmea2
import sys
import os

nodo=str(sys.argv[1])
bw=str(sys.argv[2])
maxCurrent=str(sys.argv[3])
paqueteEnviado=str(sys.argv[4])
paqueteRecibido=str(sys.argv[5])
tiempoEnvio =str(sys.argv[6])
RSSI=str(sys.argv[7])
payloadlength=str(sys.argv[8])

port = serial.Serial(port="/dev/ttyACM0",
                     baudrate=9600,
                     timeout=0.1,
                     bytesize=serial.EIGHTBITS)
port.close()
port.open()
data = ''

# nodo.txt se refiere a la  informacion propia de nodo tomanda desde el sensor
# Se deja un tiempo para que el GNSS inicie y de informacion util de ubicacion
i = 0

infoLora = str(nodo) + ','+ str(bw) + ','+ str(maxCurrent)+ ','+ str(paqueteEnviado) + ','+ str(paqueteRecibido) + ','+ str(tiempoEnvio) + ','+ str(RSSI) + ','+ str(payloadlength)
def line_prepender(nodo, line): 
    with open('/home/pi//Desktop/data/nodo'+ str(nodo)+'.txt', 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(str(line) + '\n' + content)
        f.close()

while True:
    data = port.readline()
    if (data.startswith("$GNGGA")):
        nmea = str(infoLora) + str(data.rstrip('$\r\n')) 
        msg = pynmea2.parse(data)
        if msg.num_sats > 3:
            i = 1
        line_prepender(nodo,nmea)
    if i == 1:
        break
 
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