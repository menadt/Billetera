from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .forms import formCrearMovimiento
from .models import Movimiento

# Create your views here.
def home (request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form':UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            #register User
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect ('movimientos')
            except IntegrityError:
                return render(request, 'signup.html', 
                {'form':UserCreationForm,
                'error': 'Este usuario ya existe.'})

        else:
            return render(request, 'signup.html', 
                {'form':UserCreationForm,
                'error': 'Las constrasenias no coinciden.'})
@login_required
def movimientos(request):
    listaMovimientos = Movimiento.objects.all()
    return render(request,'movimientos.html',
    {'listaMovimientos':listaMovimientos})

@login_required
def crearMovimiento(request):
    if request.method == 'GET':
        return render(request, 'crearMovimientos.html', {
            'form':formCrearMovimiento
            })
    else:
        try:
            formulario = formCrearMovimiento(request.POST)
            nuevo_movimiento = formulario.save(commit=False)
            nuevo_movimiento.cuenta = request.user
            nuevo_movimiento.save()
           # cuenta = get_object_or_404(Cuenta, usuario=request.user)
           # if nuevo_movimiento.tipo == "Ingreso":
           #     cuenta.saldo+=nuevo_movimiento.monto
           # else:
           #     cuenta.saldo= cuenta.saldo - nuevo_movimiento.monto
           # cuenta.save()
            return redirect('movimientos')
        except:
            return render(request, 'crearMovimientos.html', {
            'form':formCrearMovimiento,
            'error': 'No se pudo crear el movimiento'
            }) 

@login_required
def modificarMovimientos(request, mov_id):
    if request.method == 'GET':
        mov = get_object_or_404(Movimiento, pk=mov_id)
        form = formCrearMovimiento(instance=mov)
        return render(request, 'modificarEliminarMovimiento.html',{
            'mov':mov,
            'form': form
        })
    else:
        try:
            mov = get_object_or_404(Movimiento, pk=mov_id)
            form = formCrearMovimiento(request.POST, instance=mov)
            form.save()
            return redirect('movimientos')
        except ValueError:
           return render(request, 'modificarEliminarMovimiento.html',{
            'mov':mov,
            'form': form,
            'error': 'No se pudo actualizar la tarea.'
        }) 

@login_required
def eliminar(request, mov_id):
    mov = get_object_or_404(Movimiento, pk=mov_id)
    if request.method == 'POST':
        mov.delete()
        return redirect('movimientos')


@login_required
def cerrarSesion(request):
    logout(request)
    return redirect('home')

def iniciarSesion(request):
    if request.method == 'GET':
        return render(request, 'iniciarSesion.html',
        {'form':AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'iniciarSesion.html',
            {'form':AuthenticationForm,
            'error':"usuario o password incorrecto"})
        else:
            login(request, user)
            return redirect('movimientos')

@login_required
def saldos(request):
    users = User.objects.all()
    saldos={}
    for user in users:
        operaciones = Movimiento.objects.filter(cuenta=request.user)
        suma=0
    return render(request, 'saldos.html', saldos)