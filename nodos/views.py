from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login as dj_login
from django.utils.encoding import  smart_str
from django.shortcuts import get_object_or_404
from nodos.models import nodos,maestroES
import os, sys
import json
import pynmea2
from django.core import serializers

path ="./datos/"


def download(request,filename):
    file = os.path.join(path,filename)
    response = HttpResponse(open(file).read())#content_type='application/force-download') 
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(filename)
    return response 

def ver(request,filename):
    file = os.path.join(path,filename)
    file =open(file).read()
    # It's usually a good idea to set the 'Content-Length' header too. 
    # You can also set any other required headers: Cache-Control, etc. 
    return render(request, 'nodos/ver.html',{"data":file})

def maestro(request):
    fil = os.path.join(path,"modo.txt")
    f1 = open(fil,'w')
    f1.write("1")
    f1.close()
    try:
        n = maestroES.objects.get(index = 0)
    except maestroES.DoesNotExist:
        n = maestroES(index = 0,maestro = True)
    n.save()
    n =  nodos.objects.all()
    m = maestroES.objects.all()
    data = serializers.serialize('json',nodos.objects.all(), fields=('NumeroNodo','latitud','longitud','estadoGnss'))
    return render(request, 'nodos/index.html',{"data":n,"data2":m,"dataJ":data})

#sudo reboot
def actualizar(request):
    dirs = os.listdir( path )
    try:
        m = maestroES.objects.get(index = 0)
    except maestroES.DoesNotExist:
        m = maestroES(index = 0,maestro = False)
        m.save()
    for file in dirs:
        if "nodo" in str(file):
            file0 = os.path.join(path,file)
            data = open(file0, "r").readlines()
            a = file.split(".")[0]
            lastData = data[0]
            if len(lastData) <5:
                lastData =a[len(a)-1]+",0,0,0,0,0,0,0_,"
            data0 = lastData.split("_") 
            data = data0[0].split(",")
            if len(data0[1]) > 10:  
                if "$GNGGA" in data0[1]:
                    msg = pynmea2.parse(data0[1].rstrip('\n'))
                else:
                    msg = pynmea2.parse("$GNGGA"+data0[1].rstrip('\n'))
            else:
                msg = pynmea2.parse("$GNGGA,190216.00,,,,,0,00,99.99,,,,,,*75")
            #9,1,2,3,4,5,6,0$GNGGA,185951.00,0438.09587,N,07404.10108,W,1,12,0.65,2601.3,M,4.7
            try:
                n = nodos.objects.get(NumeroNodo = int(data[0])) 
                n.EstadoLora = True if int(data[6]) != 0 else False
                n.AnchoBanda = int(data[1])
                n.Corriente = int(data[2])
                n.PaquetesEnviados = int(data[3])
                n.PaquetesRecibidos = int(data[4])
                n.TiempoEnvio = float(data[5])
                n.FuerzaSenal = int(data[6])
                n.CargaUtil = int(data[7])
                #GNSS
                n.NumeroSatelites = msg.num_sats
                n.dilucion =msg.horizontal_dil
                n.latitud = msg.latitude
                n.longitud = msg.longitude
                n.altitud = msg.altitude
                n.fixQuality= msg.gps_qual
                n.estadoGnss = True if int(msg.gps_qual) != 0 else False
                n.save()
            except nodos.DoesNotExist:
                n = nodos(
                        NumeroNodo = int(data[0]),
                        EstadoLora = True if int(data[6]) != 0 else False,
                        AnchoBanda = int(data[1]),
                        Corriente =int(data[2]),
                        PaquetesEnviados = int(data[3]),
                        PaquetesRecibidos =int(data[4]),
                        TiempoEnvio = float(data[5]),
                        FuerzaSenal = int(data[6]),
                        CargaUtil = int(data[7]),
                        #GNSS
                        NumeroSatelites = msg.num_sats,
                        dilucion =msg.horizontal_dil,
                        latitud = msg.latitude,
                        longitud = msg.longitude,
                        altitud = msg.altitude,
                        fixQuality= msg.gps_qual,
                        estadoGnss = True if int(msg.gps_qual) != 0 else False
                )
                n.save()
    no =  nodos.objects.all()
    data = serializers.serialize('json',nodos.objects.all(), fields=('NumeroNodo','latitud','longitud','estadoGnss'))
    return  render(request, 'nodos/index.html',{"data":no,"dataJ":data})

def detallesNodo(request,filename):
    name = "nodo"+ filename + ".txt"
    nodo = get_object_or_404(nodos,NumeroNodo = filename)
    return render(request, 'nodos/detalles.html', {"numero":nodo.NumeroNodo,"data":nodo,"file":name})

def index(request):
    n =  nodos.objects.all()
    m = maestroES.objects.all()
    data = serializers.serialize('json',nodos.objects.all(), fields=('NumeroNodo','latitud','longitud','estadoGnss'))
    return render(request, 'nodos/index.html',{"data":n,"maestro":m,"dataJ":data})


def loginUser(request):
    logout(request)
    if request.method == "POST":
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(username=usuario, password=clave)
        if user is not None:
            if user.is_active:
                dj_login(request, user)
                return redirect('nodos:index')
        else:
            return render(request,'inicio/login.html', {'error':'No se pudo iniciar secion'})

    return render(request, 'inicio/login.html')

def NewUser(request):
    if request.method == "POST":
        usuario = request.POST['username']
        clave = request.POST['password']
        clave_c = request.POST['password_conf']
        if usuario and clave:
            if (clave != clave_c):
                return render(request, 'inicio/register.html', {'error': 'La clave no coincide', 'nombre': usuario})
            else:
                if User.objects.filter(username__iexact=usuario).exists():
                    return render(request, 'inicio/register.html', {'error': 'Ya existe el usuario', 'nombre': usuario})
                User.objects.create_user(username=usuario, password=clave)
                return redirect('nodos:login')
        else:
            pass
    return render(request, 'inicio/register.html')

