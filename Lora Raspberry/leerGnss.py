import serail

port = serail.Serial("/dev/ttyAMA0",baudrate=9600,timeout = 3.0)
rcv = port.read(30)
print(rcv)

    #include <SoftwareSerial.h>

SoftwareSerial gps(4,3);

char dato=' ';

void setup()
{
 Serial.begin(115200);            
 gps.begin(9600); 
}


void loop()
{
  if(Serial.available())
  {
    dato=Serial.read();
    gps.print(dato);
  }
}
port = serial.Serial("/dev/serial0",baudrate=9600)
