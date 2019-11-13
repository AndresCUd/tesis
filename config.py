## Instaler Python
sudo apt-get update
sudo apt-get install build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev -y
wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tar.xz
tar xf Python-3.6.5.tar.xz
cd Python-3.6.5
./configure
make
sudo make altinstall

sudo rm -r Python-3.6.5
rm Python-3.6.5.tar.xz
sudo apt-get --purge remove build-essential tk-dev -y
sudo apt-get --purge remove libncurses5-dev libncursesw5-dev libreadline6-dev -y
sudo apt-get --purge remove libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev -y
sudo apt-get --purge remove libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev -y
sudo apt-get autoremove -y
sudo apt-get clean -y
## Install django
pip3.6 install Django==2.2.4

## Instaler ardupi

git clone https://github.com/AndresCUd/tesis.git
 mv tesis /home/pi/datos
cd datos/
unzip raspberrypi.zip && cd cooking/arduPi && chmod +x install_arduPi && ./install_arduPi && rm install_arduPi && cd ../..
unzip -u arduPi-api_LoRa_v1_4.zip && cd cooking/examples/LoRa && chmod +x cook.sh && cd ../../..
mv  /home/pi/datos/LoRa_Raspberry/nodo.cpp  /home/pi/datos/cooking/examples/LoRa 
cd  /home/pi/datos/cooking/examples/LoRa 
sudo ./cook.sh nodo.cpp
mv  nodo.cpp_exe   /home/pi/Desktop/LoRa
cd /home/pi/Desktop/
mkdir data
mkdir LoRa
cd  /home/pi/datos/LoRa_Raspberry
mv datos1.py /home/pi/Desktop/LoRa
mv gnss.py  /home/pi/Desktop/LoRa


# /home/pi/datos/
sudo rm -r db.sqlite3
sudo python3.6 manage.py runserver

sudo nano /etc/rc.local
# Add to end to the file
 

sudo /home/pi/Desktop/LoRa/nodo.cpp_exe &
#sudo /home/pi/cooking/examples/LoRa/nodo.cpp_exe &

cd /home/pi/Desktop/ 
mkdir data











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
