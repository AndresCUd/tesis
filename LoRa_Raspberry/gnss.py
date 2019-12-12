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
            print(data)
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
    nmea =nodo+",0,0,0,0,0,0,0_$"
    line_prepender(nodo,nmea)

"""
import serial
import time, os
import pynmea2
import sys
import os
port = serial.Serial(port="/dev/ttyACM0",
                    baudrate=9600,
                    timeout=0.1,
                    bytesize=serial.EIGHTBITS)
fi=open("/home/pi//Desktop//nodo.txt", "a+")
port.close()
port.open()
while True:
    data = port.readline()
    if (data.startswith("$GNGGA")):
        msg = pynmea2.parse(data)
        fi.write(data)
        print(data)


"""
 



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


"""
import datetime

a = datetime.datetime.now()
users  = db.collection(u'users').get().to_dict()
for user in users:
  userTime =datetime.datetime.timestamp(timestamp)
  if userTime - a >= 36000 :
     db.collection(u'users').document(user.id).delete()




$GNGGA,001914.00,0438.09531,N,07404.10232,W,1,08,1.62,2587.1,M,4.7,M,,*5E
$GNGGA,001915.00,0438.09532,N,07404.10232,W,1,08,1.62,2586.9,M,4.7,M,,*55
$GNGGA,001916.00,0438.09532,N,07404.10233,W,1,08,1.62,2586.7,M,4.7,M,,*59
$GNGGA,001917.00,0438.09532,N,07404.10234,W,1,08,1.62,2586.5,M,4.7,M,,*5D
$GNGGA,001918.00,0438.09533,N,07404.10235,W,1,08,1.62,2586.3,M,4.7,M,,*54
$GNGGA,001919.00,0438.09533,N,07404.10238,W,1,08,1.62,2586.1,M,4.7,M,,*5A
$GNGGA,001920.00,0438.09533,N,07404.10239,W,1,08,1.62,2586.1,M,4.7,M,,*51
$GNGGA,001921.00,0438.09534,N,07404.10240,W,1,08,1.62,2585.9,M,4.7,M,,*52
$GNGGA,001922.00,0438.09538,N,07404.10241,W,1,08,1.62,2585.6,M,4.7,M,,*53
$GNGGA,001923.00,0438.09541,N,07404.10243,W,1,08,1.62,2585.5,M,4.7,M,,*5D
$GNGGA,001924.00,0438.09540,N,07404.10245,W,1,08,1.62,2585.4,M,4.7,M,,*5C
$GNGGA,001925.00,0438.09541,N,07404.10247,W,1,08,1.62,2585.2,M,4.7,M,,*58
$GNGGA,001926.00,0438.09544,N,07404.10247,W,1,08,1.62,2584.9,M,4.7,M,,*54
$GNGGA,001927.00,0438.09547,N,07404.10247,W,1,08,1.62,2584.7,M,4.7,M,,*58








"""