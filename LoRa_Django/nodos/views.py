from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login as dj_login
from django.utils.encoding import  smart_str
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import nodos
import os, sys
import json
import pynmea2
path = "//home//pi//Desktop//datos"
#path = "C:\\Users\\varit\\Desktop\\datos\\"
 

def download(request,filename):
    name = "nodo"+ filename + ".txt"
    file = os.path.join(path,name)
    response = HttpResponse(open(file).read())#content_type='application/force-download') 
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(filename)
  #  response['X-Sendfile'] = smart_str(path) 
    # It's usually a good idea to set the 'Content-Length' header too. 
    # You can also set any other required headers: Cache-Control, etc. 
    return response 

def ver(request,filename):
    name = "nodo"+ filename + ".txt"
    file = os.path.join(path,name)
    file =open(file).read()
    # It's usually a good idea to set the 'Content-Length' header too. 
    # You can also set any other required headers: Cache-Control, etc. 
    return render(request, 'nodos/ver.html',{"data":file})


def maestro(request):
    path_m = path
    filename = "modo.txt"
    file = os.path.join(path_m,filename)
    f = open(file,'w')
    f.write("1,")
    f.close()
    dirs = os.listdir( path )
    return  render(request, 'nodos/index.html',{"data":dirs})

def esclavo(request):
    path_e = path 
    filename = "modo.txt"
    file = os.path.join(path_e,filename)
    f = open(file,'w')
    f.write("0,")
    f.close()
    dirs = os.listdir( path )
    return  render(request, 'nodos/index.html',{"data":dirs})

def actualizar(request):
    no =  nodos.objects.all()
    dirs = os.listdir( path )
    for file in dirs:
        file0 = os.path.join(path,file)
        data = open(file0).readlines()
        lastData = data[len(data)-1]
        data = lastData.split(",") 
        #9,1,2,3,4,5,6,0$GNGGA,185951.00,0438.09587,N,07404.10108,W,1,12,0.65,2601.3,M,4.7$
        try:
            n = nodos.objects.get(NumeroNodo = int(data[0])) 
            n.EstadoLora = True if int(data[1]) != 0 else False
            n.AnchoBanda = int(data[1])
            n.Corriente = int(data[2])
            n.PaquetesEnviados = int(data[3])
            n.PaquetesRecibidos = int(data[4])
            n.TiempoEnvio = float(data[5])
            n.FuerzaSenal = int(data[6])
            n.CargaUtil = data[7]
             #GNSS
            n.NumeroSatelites = data[8]
            n.dilucion =data[9]
            n.latitud = data[10]
            n.longitud = data[11]
            n.altitud = data[12]
            n.fixQuality= data[13]
            n.estadoGnss = True if int(data[13]) != 0 else False
            n.save()
        except nodos.DoesNotExist:
            n = nodos(
                    NumeroNodo = int(data[0]),
                    EstadoLora = True if int(data[1]) != 0 else False,
                    AnchoBanda = int(data[1]),
                    Corriente =int(data[2]),
                    PaquetesEnviados = int(data[3]),
                    PaquetesRecibidos =int(data[4]),
                    TiempoEnvio = float(data[5]),
                    FuerzaSenal = int(data[6]),
                    CargaUtil = data[7],
                    #GNSS
                    NumeroSatelites = data[8],
                    dilucion = data[9],
                    latitud = data[10],
                    longitud = data[11],
                    altitud = data[12],
                    fixQuality= data[13],
                    estadoGnss = True if int(data[13]) != 0 else False
            )
            n.save()
        
    return  render(request, 'nodos/index.html',{"data":no})

def detallesNodo(request,filename):
    name = "nodo"+ filename + ".txt"
    nodo = get_object_or_404(nodos,NumeroNodo = filename)
    return render(request, 'nodos/detalles.html', {"numero":nodo.NumeroNodo,"data":nodo,"file":name})

def index(request):
    n =  nodos.objects.all()
    return render(request, 'nodos/index.html',{"data":n})

#sudo python3 /home/pi/tesis/LoRa_Django/manage.py runserver 192.168.137.142:8080
    
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
