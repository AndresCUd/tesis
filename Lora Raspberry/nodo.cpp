#include "stdio.h"
#include "time.h"
#include "arduPiLoRa.h"
//#include <SPI.h>

int e, paqueteEnviado = 0, paqueterecibido = 0, paqOrigin = 0;
int snr, rssi, rssil, proxNodo;
char my_packet[300];
char mess[] = "echo '";
char mess1[] = "' >> /home/pi/Desktop/nodo";
char mess2[] = ".txt";
bool mode = true;
double secs = 0;
time_t rawtime;
char info1[300];
char info2[300];
char infoT[300];
char coma[] = ",";
char mgsA[] = "a";
char mgsB[] = "b";
char data;

// GNSS Comunicacion Serial
char buffer;

void setup()
{
  Serial.begin(9600);
  // Power ON the module
  e = sx1272.ON();
  printf("Setting power ON: state %d\n", e);

  // Set transmission mode
  e |= sx1272.setMode(4);
  printf("Setting Mode: state %d\n", e);

  // Set header
  e |= sx1272.setHeaderON();
  printf("Setting Header ON: state %d\n", e);

  // Select frequency channel
  e |= sx1272.setChannel(CH_10_868);
  printf("Setting Channel: state %d\n", e);

  // Set CRC
  e |= sx1272.setCRC_ON();
  printf("Setting CRC ON: state %d\n", e);

  // Select output power (Max, High or Low)
  e |= sx1272.setPower('H');
  printf("Setting Power: state %d\n", e);

  // Set the node address
  e |= sx1272.setNodeAddress(9);
  printf("Setting Node address: state %d\n", e);

  // Print a success message
  if (e == 0)
    printf("SX1272 successfully configured\n");
  else
    printf("SX1272 initialization failed\n");

  delay(1000);
}
void lectura()
{
  Serial.write()
  printf("LEctura GPS ");
}

void esclavo(void)
{
  e = sx1272.receivePacketTimeoutACK(9000);
  if (e == 0)
  {
    for (unsigned int i = 0; i < sx1272.packet_received.length; i++)
    {
      my_packet[i] = (char)sx1272.packet_received.data[i];
    }
    printf(my_packet);
    if (my_packet[0] == 97)
    {
      paqOrigin = (int)sx1272.packet_received.src;
      printf("Enviado al Nodo %d \n", paqOrigin);
      paqueterecibido = paqueterecibido + 1;
      struct timeval start, stop;
      // Formato Informacion
      // Nombre,#PaquetesEnviado,#PaquetesRecivudo,TimepoEnvio,RSSI,BW,Canal,Corriente,Payload
      e = sx1272.getNodeAddress();
      e = sx1272.getRSSI();
      e = sx1272.getBW();
      e = sx1272.getMaxCurrent();
      e = sx1272.getPayloadLength();
      // Esto de LoRa
      sprintf(info1, "%d%s%d%s%d%s%f%s%d%s%d%s%d%s%d%s%d", sx1272._nodeAddress, coma, sx1272._bandwidth, coma, sx1272._maxCurrent, coma, paqueteEnviado, coma, paqueterecibido, coma, secs, coma, sx1272._RSSI, coma, sx1272._payloadlength);
      // Estado GNSS + Datos
      //sprintf(info1,"%d%s%d%s%d%s%f%s%d%s%d%s%d%s%d%s%d",sx1272._nodeAddress,coma,paqueteEnviado,coma,paqueterecibido,coma,secs,coma,sx1272._RSSI,coma,sx1272._bandwidth,coma,sx1272._channel,coma,sx1272._maxCurrent,coma,sx1272._payloadlength);
      //Total Info
      //sprintf(info1,"%s%s",info,info2);
      e = 2;
      int error = 0;
      while (e > 1)
      {
        gettimeofday(&start, NULL);
        e = sx1272.sendPacketTimeoutACK(paqOrigin, info1);
        gettimeofday(&stop, NULL);
        secs = (double)(stop.tv_usec - start.tv_usec) / 1000000 + (double)(stop.tv_sec - start.tv_sec);
        paqueteEnviado = paqueteEnviado + 1;
        printf("Info regresada %s:\n ", info1);
        delay(500);
        error = error + 1;
        if (error == 4)
        {
          break;
        }
      }
    }
    else if (my_packet[0] == 98)
    {
      mode = true;
    }
  }
  else
  {
    printf("No hay hay Permiso\n");
  }
  delay(500);
}
void maestro(void)
{
  e = sx1272.getNodeAddress();
  int k = sx1272._nodeAddress;
  for (int i = 1; i < 10; i++)
  {
    if (i != k){
      e = sx1272.sendPacketTimeoutACK(i, mgsA);
      printf("Pregunta al nodo %d\n", i);
      if (e == 0)
      {
        e = 3;
        while (e > 2)
        {
          e = sx1272.receivePacketTimeoutACK(10000);
          if (e == 0)
          {
            //printf("Receive packet, state %d, Nodo %d \n",e,i);
            for (unsigned int j = 0; j < sx1272.packet_received.length; j++)
            {
              my_packet[j] = (char)sx1272.packet_received.data[j];
            }
            //e = sx1272.getNodeAddress();
            sprintf(info1, "%s%s%s%d%s", mess, my_packet, mess1, i, mess2);
            printf("Message :%s\n", my_packet);
            system(info1);
          }
        }
      }
      else
      {
        sprintf(info1, "%s%d%s%d%s", mess, i, mess1, i, mess2);
        system(info1);
      }
      delay(500);
    }else{
      e = sx1272.getNodeAddress();
      e = sx1272.getRSSI();
      e = sx1272.getBW();
      e = sx1272.getMaxCurrent();
      e = sx1272.getPayloadLength();
      // Esto de LoRa
      lectura();
      sprintf(info1, "%d%s%d%s%d%s%f%s%d%s%d%s%d%s%d%s%d", sx1272._nodeAddress, coma, sx1272._bandwidth, coma, sx1272._maxCurrent, coma, paqueteEnviado, coma, paqueterecibido, coma, secs, coma, sx1272._RSSI, coma, sx1272._payloadlength);
      system(info1);  
    }
  }
  while (mode)
  {
    for (int j = k + 1; j < 10; j++)
    {
      if (j != k)
      {
        printf("Message :%d\n", j);
        e = sx1272.sendPacketTimeoutACK(j, mgsB);
        if (e == 0)
        {
          mode = false;
          break;
        }
      }
    }
    k = 0;
  }
}
void datos(){
    data = system("python leerGNSS.py");
}
int main()
{
  setup();
  while (1)
  {

    if (mode)
    {
      maestro();
    }
    else
    {
      esclavo();
    }
  }
  return (0);
}
