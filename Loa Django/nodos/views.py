from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login as dj_login
from django.utils.encoding import  smart_str
from django.shortcuts import get_object_or_404
from subprocess import Popen, PIPE, STDOUT
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
    print(file)
    return render(request, 'nodos/ver.html',{"data":file})


def actualizar(request):
    dirs = os.listdir( path )
    print(dirs)
    for file in dirs:
        print(file)
        file0 = os.path.join(path,file)
        data = open(file0).readlines()
        lastData = data[len(data)-1]
        words = lastData.split(",") 
        print(words)
        try:
            n = nodos.objects.get(NumeroNodo= lastData[0]) 
            n.EstadoLora = True if words[0] == 0 else False
            n.AnchoBanda = 500
            n.Canal = 10
            n.Corriente = 100
            n.PaquetesEnviados = 10
            n.PaquetesRecibidos = 10
            n.TiempoEnvio = 10
            n.FuerzaSenal = 10
            n.CargaUtil = 10
             #GNSS
            n.estadoGnss = False
            n.NumeroSatelites = 1
            n.dilucion =1
            n.latitud = 1
            n.longitud = 1
            n.altitud = 1
            n.fixQuality= 0
            n.save()
            print(n)
        except nodos.DoesNotExist:
            n = nodos(
                    EstadoLora = True if words[0] == 0 else False,
                    NumeroNodo = lastData[0],
                    AnchoBanda = 0,
                    Canal =0,
                    Corriente =0,
                    PaquetesEnviados = 0,
                    PaquetesRecibidos =0,
                    TiempoEnvio = 0,
                    FuerzaSenal = 0,
                    CargaUtil = 0,
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
    file = open(file,'r')
    print(file.readlines())
    return render(request, 'nodos/detalles.html', {"numero": 1,"file":filename})

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
