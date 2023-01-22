"""djangoCrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from billetera import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('movimientos/', views.movimientos, name='movimientos'),
    path('movimientos/crearMovimientos/', views.crearMovimiento, name='crearMovimientos'),
    path('movimientos/<int:mov_id>', views.modificarMovimientos, name='modificarMovimientos'),
    path('movimientos/<int:mov_id>/borrar', views.eliminar, name='eliminar'),
    path('logout/', views.cerrarSesion, name='logout'),
    path('iniciarSesion/', views.iniciarSesion, name='iniciarSesion'),
    path('saldos/', views.saldos, name='saldos'),

]
