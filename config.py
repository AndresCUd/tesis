
#Get raspbian lite
https://www.raspberrypi.org/downloads/raspbian/
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
sudo pip install Django==2.2.4
alias python='python3'
sudo apt-get install git
## Instaler ardupi
git clone https://github.com/AndresCUd/tesis.git


mkdir /home/pi/Desktop/LoRa
cd  /home/pi/tesis/LoRa_Raspberry
mv datos1.py /home/pi/Desktop/LoRa/
mv gnss.py  /home/pi/Desktop/LoRa/
mv saveData.py  /home/pi/Desktop/LoRa/
mv modo.py  /home/pi/Desktop/LoRa/
sudo rm -r /home/pi/Desktop/data/
mkdir /home/pi/Desktop/data
sudo python  //home//pi//Desktop//LoRa//datos1.py 1
sudo python  //home//pi//Desktop//LoRa//datos1.py 2
sudo python  //home//pi//Desktop//LoRa//datos1.py 3
sudo python  //home//pi//Desktop//LoRa//datos1.py 4
sudo python  //home//pi//Desktop//LoRa//datos1.py 5
sudo ./cook.sh nodo.cpp
sudo rm -r /home/pi/Desktop/LoRa/nodo.cpp_exe 
mv  nodo.cpp_exe   /home/pi/Desktop/LoRa/
sudo /home/pi/Desktop/LoRa/nodo.cpp_exe 


nano  //home//pi//Desktop//LoRa//modo.txt
0
cd  /home/pi/tesis/LoRa_Django
sudo pip3 install -r requirements.txt
sudo pip install pynmea2
cd /home/pi/tesis
unzip raspberrypi.zip && cd cooking/arduPi && chmod +x install_arduPi && ./install_arduPi && rm install_arduPi && cd ../..
unzip -u arduPi-api_LoRa_v1_4.zip && cd cooking/examples/LoRa && chmod +x cook.sh && cd ../../..
mv  /home/pi/tesis/LoRa_Raspberry/nodo.cpp  /home/pi/tesis/cooking/examples/LoRa 
cd  /home/pi/tesis/cooking/examples/LoRa 
sudo ./cook.sh nodo.cpp
mv  nodo.cpp_exe   /home/pi/Desktop/LoRa/
# /home/pi/datos/
sudo nano /etc/rc.local
# Add to end to the file
# /home/pi/datos/LoRa_Django/nodos/views.py
sudo nano /etc/rc.local
sudo python3  /home/pi/tesis/LoRa_Django/manage.py runserver 192.168.137.21:8080 &
sudo /home/pi/Desktop/LoRa/nodo.cpp_exe &
#
#sudo  rm -r /home/pi/Desktop/LoRa/nodo.cpp_exe &
#sudo /home/pi/cooking/examples/LoRa/nodo.cpp_exe &
*


sudo apt-get update -y 
sudo apt-get upgrade  --force-yes -y
sudo apt-get install hostapd 
sudo apt-get install dnsmasq 
sudo systemctl stop hostapd
sudo systemctl stop dnsmasq
sudo nano /etc/dhcpcd.conf
    ##add at end:
interface wlan0
static ip_address=192.168.0.10/24
nohook wpa_supplicant
    ##add at end:
sudo service dhcpcd restart
sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig
sudo nano /etc/dnsmasq.conf
#
interface=wlan0      # Use the require wireless interface - usually wlan0
dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h
#
sudo systemctl reload dnsmasq
sudo nano /etc/hostapd/hostapd.conf
#
interface=wlan0
driver=nl80211
ssid=lora
hw_mode=g
channel=7
wmm_enabled=0
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=lora
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP
#
sudo nano /etc/default/hostapd
DAEMON_CONF="/etc/hostapd/hostapd.conf"
sudo systemctl unmask hostapd
sudo systemctl enable hostapd
sudo systemctl start hostapd
sudo systemctl status hostapd
sudo systemctl status dnsmasq
sudo nano /etc/sysctl.conf
## find #net.ipv4.ip_forward=1
net.ipv4.ip_forward=1  
#  
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
sudo sh -c "iptables-save > /etc/iptables.ipv4.nat"
iptables-restore < /etc/iptables.ipv4.nat
sudo reboot
#Install re


# Buscar la trama que tenga GNRMC  => 16:25:24  $GNRMC,162524.00,A,0438.09185,N,07404.10138,W,0.043,,311019,,,A,V*0A
                                                $GNGGA$0        ,A,         0,N,          0,W,    0,,      ,,,V,V*0A'
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

sudo rm -r /home/pi/tesis/
sudo rm -r /home/pi/Desktop/data/
sudo rm -r /home/pi/Desktop/LoRa/
