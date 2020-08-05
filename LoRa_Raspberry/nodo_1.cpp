#include "stdio.h"
#include "time.h"
#include "stdlib.h"
#include "arduPiLoRa.h"
//#include <SPI.h>

int posicion = 1;
int valor = 0;
int snr, rssi, rssil, proxNodo;
char my_packet[300];
char mess[] = "python //home//pi//Desktop//LoRa//pruebas.py ";
char info1[300];
char info2[300];
char infoT[300];
char coma[] = " ";
int nodo = 9;
int p = 0;
int paqueteEnviado;
int paqueteRecibido;
// GNSS Comunicacion Serial
char buff[250];


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



int main(){
    FILE *fp;
    fp = fopen ("/home/pi/Desktop/data/nodo9.txt", "r");
    fgets(buff, 255, (FILE*)fp);
    fclose(fp);
    char *p;
    int j = 1;
    p = strtok (buff,",");
    while (p!= NULL){
      if (j == 3){
        paqueteEnviado = toString(p);
      }
      if (j == 4){
        paqueteRecibido = toString(p);
     } 
      p = strtok (NULL, ",");
    j = j+1;
    }
}




/*

  char string[50] ="Test,string1,Test,string2:Test:string3";
  char *p;
  p = strtok (string,",");
  while (p!= NULL)
  {
    printf ("%s\n",p);
    p = strtok (NULL, ",");
  }
  return 0;
}



typedef void(*split_fn)(const char *, size_t, void *);
void split(const char *str, char sep, split_fn fun, void *data){
    unsigned int start = 0, stop;
    for (stop = 0; str[stop]; stop++) {
        if (str[stop] == sep) {
            fun(str + start, stop - start, data);
            start = stop + 1;
        }
    }
    fun(str + start, stop - start, data);
}

void print(const char *str, size_t len, void *data){
    printf("%.*s\n", (int)len, str);
}
 
int main(){
    char str[] = "first,second,third,fourth";
    split(str, ',', print, NULL);
    return 0;
}

*/

/*
   FILE *fp;
   char buff[255];
   fp = fopen ("//home//pi//Desktop//data//nodo9.txt", "r");
   fgets(buff, 255, (FILE*)fp);
   printf("3: %s\n", buff );
   fclose(fp);
    while (1) {
        if (p == 0){
            if (valor < 13){
            sprintf(info1, "%s%d%s%d%s%d", mess, nodo, coma, valor, coma, posicion );
            }else { break;}
            // Continue buscando el valor
        }else{
            valor =valor-1;
            if (valor == 10){sprintf(infoT, "%s%s",infoT,"," );}
            else if (valor == 11){sprintf(infoT, "%s%s",infoT,".");}
            else if (valor == 12){sprintf(infoT, "%s%s",infoT,"-" );}
            else if (valor < 10){sprintf(infoT, "%s%d",infoT,valor);}
            else{printf("El valor es :%s  \n", infoT);break;}
            posicion=posicion+1;
            valor=0;
            printf("Message :%s\n", infoT);
            sprintf(info1, "%s%d%s%d%s%d", mess, nodo," ", valor, " ", posicion );
        }
        p = system(info1);       
        valor =valor+1;
    }
    return (0);*/


/*
  int buenas = 1;
  while (buenas == 1) {
      if (p == 0){
          if (valor < 13){
          sprintf(info1, "%s%d%s%d%s%d", mess, numNodo, coma, valor, coma, posicion );
          }else {buenas = 2;}
          // Continue buscando el valor
      }else{
          valor =valor-1;
          if (valor == 10){sprintf(infoT, "%s%s",infoT,"," );}
          else if (valor == 11){sprintf(infoT, "%s%s",infoT,".");}
          else if (valor == 12){sprintf(infoT, "%s%s",infoT,"-" );}
          else if (valor < 10){sprintf(infoT, "%s%d",infoT,valor);}
          else{buenas = 2;}
          posicion=posicion+1;
          valor=0;

          sprintf(info1, "%s%d%s%d%s%d", mess, numNodo," ", valor, " ", posicion );
      }
      p = system(info1);       
      valor =valor+1;
  }
  */