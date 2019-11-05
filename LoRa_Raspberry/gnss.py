import serial
import time, os
import pynmea2

port = serial.Serial(port="/dev/ttyACM0",
                     baudrate=9600,
                     timeout=0.1,
                     bytesize=serial.EIGHTBITS)
# Inicia comunicacion serial con el sensor
port.close()
port.open()
txt = ''
data = ''
f = open('//home//pi//Desktop//data//nodo.txt', 'a+')
# nodo.txt se refiere a la  informacion propia de nodo tomanda desde el sensor
# Se deja un tiempo para que el GNSS inicie y de informacion util de ubicacion
i = 0
while True:
    while (port.in_waiting > 0):
        txt += port.read(1)
        data += txt
        if (txt == "$"):
            if ("GNGGA" in data):
                print("Este es el dato")
                print(data[0:len(data) - 2])
                msg = pynmea2.parse(data[0:len(data) - 3])
                nmea = str(msg.num_sats) + ',' + str(
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
