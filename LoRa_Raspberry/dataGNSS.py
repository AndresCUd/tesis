import serial
import time, os
import pynmea2
import sys
import os
from datetime import datetime

port = serial.Serial(port="/dev/ttyACM0",
                    baudrate=9600,
                    timeout=0.1,
                    bytesize=serial.EIGHTBITS)
port.close()
port.open()

fi=open("/home/pi//Desktop//pruebas.raw", "r")
contente =fi.read()
def line_prepender(line):  
    with open("/home/pi//Desktop//pruebas.raw", "w") as f:
        f.seek(0,0)
        f.write(str(line)+'\n'+contente)
        f.close()

while True:
    data = port.readline()
    print(data)
    line_prepender(data)

