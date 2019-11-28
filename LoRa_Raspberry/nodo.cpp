#include "stdio.h"
#include "time.h"
#include "arduPiLoRa.h"
//#include <SPI.h>

int e, paqueteEnviado = 0, paqueteRecibido = 0, paqOrigin = 0;
int snr, rssi, rssil, proxNodo;
int posicion = 1;
int p = 0;
int valor = 0;
char my_packet[300];
char mess[] = "echo '";
char mesEnd[] = ".txt";
bool mode = false;
bool mode1 = true;
double secs = 0;
time_t rawtime;
char info1[300];
char info2[300];
char infoT[300];
char toGnss[] = "sudo python  //home//pi//Desktop//LoRa//gnss.py ";
char toSave[] = "sudo python  //home//pi//Desktop//LoRa//saveData.py ";
char coma[] = " ";
char mgsA[] = "a";
char mgsB[] = "b";
char aux[1];
int numNodo =1;
// GNSS Comunicacion Serial
char buff[255];
char stringNodo[]  ="//home//pi//Desktop//data//nodo";

void setup(){
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
  e |= sx1272.setNodeAddress(numNodo);
  printf("Setting Node address: state %d\n", e);

  // Print a success message
  if (e == 0)
    printf("SX1272 successfully configured\n");
  else
    printf("SX1272 initialization failed\n");

  delay(1000);
}

void esclavo(void){
  e = sx1272.receivePacketTimeoutACK(10000);
  if (e == 0) {
    for (unsigned int i = 0; i < sx1272.packet_received.length; i++)    {
      my_packet[i] = (char)sx1272.packet_received.data[i];
    }
    if (my_packet[0] == 97) {
      paqOrigin = (int)sx1272.packet_received.src;
      paqueteRecibido = paqueteRecibido + 1;
      e = 1;
      int error = 0;
        while (e > 0){
        struct timeval start, stop;
        gettimeofday(&start, NULL);
        if (mode1){
        e = sx1272.sendPacketTimeoutACK(paqOrigin, buff);
        }else{
          e = sx1272.sendPacketTimeoutACK(paqOrigin, mgsB);
          if(e == 0){
            mode = true;
          }
        }
        if (e == 0){
          gettimeofday(&stop, NULL);
          secs = (double)(stop.tv_usec - start.tv_usec) / 1000000 + (double)(stop.tv_sec - start.tv_sec);
          paqueteEnviado = paqueteEnviado + 1;
          printf("Info regresada %s:\n", buff);
          }
        if (error==2){
          break;
        }
        error = error +1;
        }
    }
  }
}

void maestro(void){
  e = sx1272.getNodeAddress();
  int k = sx1272._nodeAddress;
  for (int i = 1; i < 6; i++)  {
    if (i != k)    {
      printf("Pregunta al Nodo %d\n", i);
      e = sx1272.sendPacketTimeoutACK(i, mgsA);
      if (e == 0) {
        printf("Enviada informacion a nodo %i\n", i);
        e = sx1272.receivePacketTimeoutACK(10000);
        if (e == 0){
          for (unsigned int j = 0; j < sx1272.packet_received.length; j++){
            my_packet[j] = (char)sx1272.packet_received.data[j];}
            printf("Info regresada %s\n", my_packet);
            if (strcmp (mgsB, my_packet) == 0){
              mode = false;
            }else{
              sprintf(info1, "%s%d%s%s",  toSave,i, coma ,my_packet);
              system(info1);
            }
        }     
      } 
    }
  }
}

int toString(char a[]) {
  int c, sign, offset, n;
 
  if (a[0] == '-') {  // Handle negative integers
    sign = -1;
  }
  if (sign == -1) {  // Set starting position to convert
    offset = 1;
  }
  else {
    offset = 0;
  }
  n = 0;
  for (c = offset; a[c] != '\0'; c++) {
    n = n * 10 + a[c] - '0';
  }
  if (sign == -1) {
    n = -n;
  }
  return n;
}

void createInfo(void){
  e = sx1272.getNodeAddress();
  e = sx1272.getRSSI();
  e = sx1272.getBW();
  e = sx1272.getMaxCurrent();
  e = sx1272.getPayloadLength();
  sprintf(info1, "%s%d%s%d%s%d%s%d%s%d%s%f%s%d%s%d",  toGnss,sx1272._nodeAddress, coma, sx1272._bandwidth, coma, sx1272._maxCurrent, coma, paqueteEnviado, coma, paqueteRecibido, coma, secs, coma, sx1272._RSSI, coma, sx1272._payloadlength);
  int a =system(info1);
  if (a == 0){
    FILE *fp;
    fp = fopen(infoT, "r");
    fgets(buff, 255, (FILE*)fp);
    fclose(fp);
  }
  int d =system("sudo python  //home//pi//Desktop//LoRa//modo.py");
  if (d == 0){
    mode1=true;
  }else{
    mode1=false;
  }
}

void datos(){
    e = sx1272.getNodeAddress();
    sprintf(infoT, "%s%d%s",  stringNodo,sx1272._nodeAddress,mesEnd);
    FILE *fp;
    fp = fopen(infoT, "r");
    fgets(buff, 255, (FILE*)fp);
    fclose(fp);
    char *p;
    int j = 1;
    p = strtok (buff,",");
    while (p!= NULL){
      printf("Info Leida %d\n",toString(p));
      if (j == 4){paqueteEnviado = toString(p);}
      if (j == 5){paqueteRecibido = toString(p);} 
      p = strtok (NULL, ",");
    j = j+1;
    }
}
 
int main(){
  setup();
  datos();
  while (1){    
  if (mode){maestro();}
    else{esclavo();}
    createInfo();
  }
  return (0);
}

