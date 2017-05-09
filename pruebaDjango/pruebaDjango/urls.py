"""pruebaDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog import views as miApp
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^otro$',miApp.otro, name = 'otro'),
    url(r'^insertarUsuario$',miApp.insertarUsuario, name = 'insertarUsuario'),
    url(r'^verificarLogin$',miApp.verificarLogin, name = 'verificarLogin'),
    url(r'^nuevoEvento$',miApp.nuevoEvento, name = 'nuevoEvento'),
    url(r'^eventosPorUsuario$',miApp.eventosPorUsuario, name = 'eventosPorUsuario'),
    url(r'^eliminarEvento$',miApp.eliminarEvento, name = 'eliminarEvento'),
    url(r'^modificarEvento$',miApp.modificarEvento, name = 'modificarEvento'),
    url(r'^eventosPorDia$',miApp.eventosPorDia, name = 'eventosPorDia'),
    url(r'^eventosPorAnio$',miApp.eventosPorAnio, name = 'eventosPorAnio'),
    url(r'^eventosPorMes$',miApp.eventosPorMes, name = 'eventosPorMes'),
    url(r'^insertarUsuario2$',miApp.insertarUsuario2, name = 'insertarUsuario2'),
]
