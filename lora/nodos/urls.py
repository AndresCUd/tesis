from django.urls import path
from django.views.generic import RedirectView
from . import views
app_name = 'nodos'
urlpatterns = [
    path('', views.index, name='index'),
    path('download/<filename>/', views.download, name='download'),
    path('ver/<filename>/', views.ver, name='ver'),
    path('login/', views.loginUser, name='login'),
    path('pruebas/', views.file_maniputer, name='pruebas'),
    path('registro/', views.NewUser, name='registro'),
    path('detallesNodo/<filename>/',views.detallesNodo,name='detalles'),
]
