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


path = "//home//pi//"
path = "C:\\Users\\varit\\Desktop\\datos\\"
 

def download(request,filename):
    file = os.path.join(path,filename)
    response = HttpResponse(open(file).read())#content_type='application/force-download') 
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(filename)
  #  response['X-Sendfile'] = smart_str(path) 
    # It's usually a good idea to set the 'Content-Length' header too. 
    # You can also set any other required headers: Cache-Control, etc. 
    return response 

def ver(request,filename):
    file = os.path.join(path,filename)
    file =open(file).read()
    # It's usually a good idea to set the 'Content-Length' header too. 
    # You can also set any other required headers: Cache-Control, etc. 
    print(nodo)
    return render(request, 'nodos/ver.html',{"data":file})


def actualizar(request):
    dirs = os.listdir( path )
    print(dirs)
    for file in dirs:
        print(file)
        file0 = os.path.join(path,file)
        data = open(file0).readlines()
        lastData = data[len(data)-1]
        data = lastData.split(",") 
        try:
            n = nodos.objects.get(NumeroNodo= data[0]) 
            n.EstadoLora = True if int(data[0]) != 0 else False
            n.AnchoBanda = int(data[1])
            n.Corriente = int(data[2])
            n.PaquetesEnviados = int(data[3])
            n.PaquetesRecibidos = int(data[4])
            n.TiempoEnvio = int(data[5])
            n.FuerzaSenal = int(data[6])
            n.CargaUtil = int(data[7])
             #GNSS
            n.estadoGnss = False
            n.NumeroSatelites = 1
            n.dilucion =1
            n.latitud = 1
            n.longitud = 1
            n.altitud = 1
            n.fixQuality= 0
            n.save()
        except nodos.DoesNotExist:
            n = nodos(
                    NumeroNodo = data[1],
                    EstadoLora = True if int(data[0]) != 0 else False,
                    AnchoBanda = int(data[1]),
                    Corriente =int(data[2]),
                    PaquetesEnviados = int(data[3]),
                    PaquetesRecibidos =int(data[4]),
                    TiempoEnvio = int(data[5]),
                    FuerzaSenal = int(data[6]),
                    CargaUtil = int(data[7]),
                    #GNSS
                    estadoGnss = lastData[0],
                    NumeroSatelites = 0,
                    dilucion = 0,
                    latitud = 0,
                    longitud = 0,
                    altitud = 0,
                    fixQuality= 0
            )
            n.save()
    return  render(request, 'nodos/index.html',{"data":dirs})

def detallesNodo(request,filename):
    file = os.path.join(path,filename)
    data = open(file,'r').readlines()
    lastData = data[len(data)-1]
    data = lastData.split(",") 
    nodo = get_object_or_404(nodos,NumeroNodo = data[0])
    print(nodo.EstadoLora)
    return render(request, 'nodos/detalles.html', {"numero":nodo.NumeroNodo,"data":nodo,"file":filename})

def index(request):
    dirs = os.listdir( path )
    return render(request, 'nodos/index.html',{"data":dirs})


    
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
