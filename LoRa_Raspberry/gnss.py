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
"""
        # Buscar la trama que tenga GNRMC  => 16:25:24  $GNRMC,162524.00,A,0438.09185,N,07404.10138,W,0.043,,311019,,,A,V*0A
        #GNRMC => Todo va separado por "," (Comas)
        #  A (0.1)  => A o V nos indica el estado de nuestra conexion GPS si es activa (A) o sin senal (V).
        # 0.043  (0.2) =>  velocidad experimentada en nudos 

        # Buscar la trama que tenga GNRMC  => GNGGA,162525.00,0438.09189,N,07404.10139,W,1,12,0.73,2609.1,M,4.7,M,,*54
        # 162524.00 => (1)  hora en coordenadas universales es decir en este caso tendremos las 16horas, 25minutos y 24.00 segundos
        # 0438.09189,N,07404.10139,W=> ubicacion latitud y longitud
        # 0438.09185,N => (2) 4 grados 38.09185 minutos emisferio Norte
        # 07404.10138,W => (3) 74 grados 04.10138 minutos emisferio Oeste
            #Realizamos conversiones a latitud y longitud  convertir los minutos a decimales de grados,
            #Latitud => 38.09185/60 = 0.6348641666666667‬  =>  dado que un grado tiene 60 minutos =>latitud  = 4.6348641666666667    si estamos en el sur (S) se agrega signo (-)
            #Longitud => 04.10138/60 = 0.0683563333333333 =>  dado que un grado tiene 60 minutos =>longitud = -74.0683563333333333  es menos es por ser oeste(W) 
        # 1 => (3) indica si la ubicación es arreglada si es 1 o no si es 0
        # 12 =>(4) cantidad de satélites que tenemos de seguimiento
        # 0.73  =>(5) dilución horizontal de la posición
        # 2609.1,M =>(6) Indican la altitud en metros sobre el nivel del mar esto es sumamente importante en sistemas de telemetría aéreos o para analizar los datos de vuelo de por ejemplo un Dron
        # 4.7,M, =>(7) indican una altitud relativa de la ubicación útil en aplicaciones de aproximación en la tierra mediante una elipsoide
      """