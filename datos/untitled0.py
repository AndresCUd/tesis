# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 16:42:09 2020

@author: Alvaro
"""
import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
import datetime

BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

def encrypt(raw, password):
    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    raw = pad(raw)
    a ="piIsTheBest31415"
    cipher = AES.new(private_key, AES.MODE_CBC, str.encode(a))
    return base64.b64encode(str.encode(a) + cipher.encrypt(raw.encode())).decode()


def decrypt(password,enc):
    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[16:])).decode()

fecha = "2020-01-1T14:33:40+0500"

a=datetime.datetime.strptime(fecha, "%Y-%m-%dT%H:%M:%S%z")
def get_message_date(date):
    WEEKDAY = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
    MONTH = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'];
    hour = ''
    if date.hour < 12:
        hour = str(date.hour) + ":" +str(date.minute) + " am"
    if date.hour == 12:
        hour = str(date.hour) + ":" +str(date.minute) + " pm"
    else :
        hour = str(date.hour-12) + ":" +str(date.minute) + " pm" 
    day = WEEKDAY[date.weekday()] +" "+ str(date.day) + " del " +MONTH[date.month-1] +" de " + str(date.year)
    return day,hour 


print(get_message_date(a))










    