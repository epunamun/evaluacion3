"""
URL configuration for evaluacion3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from biblioteca.views import listar_libros, agregar_libro, editar_libro, eliminar_libro, login, logout



urlpatterns = [
    path("admin/", admin.site.urls),
    path('listar/', listar_libros, name='listar_libros'),
    path('agregar/', agregar_libro, name='agregar_libro'),
    path('editar/<int:pk>/', editar_libro, name='editar_libro'),
    path('eliminar/<int:pk>/', eliminar_libro, name='eliminar_libro'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout')
]