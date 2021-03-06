"""CRUD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http.response import HttpResponse
from django.urls import path

#Importaciones locales
from Home import views as home_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('signup/', home_views.SignUp, name='signup'),
    path('login/', home_views.Login, name='login'),
    path('home/', home_views.Home, name='home'),
    path('logout/', home_views.Logout, name='logout'),
    path('agregar/', home_views.Agregar, name='agregar'),
    path('modificar/<int:id_asignatura>', home_views.Modificar, name='modificar'),
    path('eliminar/<int:id_asignatura>', home_views.Eliminar, name='eliminar'),
]
