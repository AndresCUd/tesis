from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('download/(?P<filename>\d+)/$', views.download, name='download'),
        path('ver/(?P<filename>\d+)/$', views.ver, name='ver'),
    
]