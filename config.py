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

pip3.6 install Django==2.2.4

git clone https://github.com/AndresCUd/tesis.git
mv tesis datos
cd datos/LoRa_Django/
# /home/pi/datos/
sudo rm -r db.sqlite3
sudo python3.6 manage.py runserver

sudo pip install pynmea2

sudo nano /etc/rc.local
# Add to end to the file
sudo python  /home/pi/datos/LoRa_Raspberry/gnss.py &
#sudo /home/pi/cooking/examples/LoRa/nodo.cpp_exe &
