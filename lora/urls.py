from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'nodos/',include('nodos.urls')),
    path('', RedirectView.as_view(url='/nodos/login/', permanent=True)),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)