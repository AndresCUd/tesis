from django.shortcuts import render
from django.http import HttpResponse
import os, sys
from django.utils.encoding import smart_str 
#from .forms import UploadFileForm
# Create your views here.

def download(request,filename):
    path = "C:\\Users\\Andres\\Desktop\\obras\\obras\\obras\\urls.py"
    file_path = os.path.join(path)
    path_to_file="C:\\Users\\Andres\\Desktop\\obras\\obras\\obras"

    response = HttpResponse(content_type='application/force-download') 
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    response['X-Sendfile'] = smart_str(path_to_file) 
    # It's usually a good idea to set the 'Content-Length' header too. 
    # You can also set any other required headers: Cache-Control, etc. 
    return response 

def ver(request,filename):
    path_to_file="C:\\Users\\Andres\\Desktop\\obras\\obras\\obras\\"
    file = os.path.join(path_to_file,filename)
    file =open(file).read()
    # It's usually a good idea to set the 'Content-Length' header too. 
    # You can also set any other required headers: Cache-Control, etc. 
    print(file)
    return render(request, 'nodos/ver.html',{"data":file})



def index(request):
    path = "C:\\Users\\Andres\\Desktop\\obras\\obras\\obras"
    dirs = os.listdir( path )
    for file in dirs:
        print (os.path.getsize( path+"\\"+file))
    return render(request, 'nodos/index.html',{"data":dirs})