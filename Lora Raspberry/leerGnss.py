import serail

port = serail.Serial("/dev/ttyAMA0",baudrate=9600,timeout = 3.0)
rcv = port.read(30)
print(rcv)

    