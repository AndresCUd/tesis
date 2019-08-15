from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login as dj_login
from django.utils.encoding import  smart_str
from subprocess import Popen, PIPE, STDOUT
from django.views.decorators.csrf import csrf_exempt
import os, sys
import json


path = "//home//pi//"
path = "C:\\Users\\varit\\Desktop\\"

def create_directory():
    command = ["bash", "nodos/scripst/file_manipulater.sh", "create"]
    try:
        process = Popen(command, stdout=PIPE, stderr=STDOUT)
        output = process.stdout.read()
        exitstatus = process.poll()
        if (exitstatus == 0):
            return {"status": "Success", "output": str(output)}
        else:
            return {"status": "Failed", "output": str(output)}
    except Exception as e:
        return {"status": "failed", "output": str(e)}


def delete_directory():
    command = ["bash", "easyaslinux/scripts/file_manipulater.sh", "delete"]
    try:
        process = Popen(command, stdout=PIPE, stderr=STDOUT)
        output = process.stdout.read()
        exitstatus = process.poll()
        if (exitstatus == 0):
            return {"status": "Success", "output": str(output)}
        else:
            return {"status": "Failed", "output": str(output)}
    except Exception as e:
        return {"status": "failed", "output": str(e)}



@csrf_exempt
def file_maniputer(request):
    action = "create"
    if action == "create":
        data = create_directory()
    elif action == "delete":
        data = delete_directory()
    else:
        data = {"status": "not defined", "output": "not defined"}
    print("Hola")
    response = HttpResponse(json.dumps(data), content_type='application/json', status=200)
    return response 
 

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
