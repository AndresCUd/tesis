import serial
import time

port = serial.Serial(port = "/dev/ttyS0",
                    baudrate=9600,
                    timeout = 3.0,
                    bytesize=serial.EIGHTBITS )
port.open()
while 1: 
    if(ser.in_waiting >0):
        line = ser.readline()
        print(line)
        print("Hola")