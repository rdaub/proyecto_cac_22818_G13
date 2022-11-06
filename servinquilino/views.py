from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from servinquilino.models import Expensa, Dato

from servinquilino.forms import DatosForm, ExpensasForm


def signin(request):
    if request.method == 'GET':
        return render(request, 'servinquilino/signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'servinquilino/signin.html',
                          {"form": AuthenticationForm, "error": "Usuario o Contraseña no válido."})
    login(request, user)
    return redirect('cuotas')

#def login(request):
#    return  render(request, 'servinquilino/login.html')

def usuarios(request):
    return  render(request, 'servinquilino/usuarios.html')

def nosotros(request):
    return render(request, 'servinquilino/nosotros.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'servinquilino/signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('cuotas')
            except IntegrityError:
                return render(request, 'servinquilino/signup.html', {"form": UserCreationForm, "error": "Usuario ya existe."})

        return render(request, 'servinquilino/signup.html', {"form": UserCreationForm, "error": "Contraseñas no coinciden."})

@login_required
def signout(request):
    logout(request)
    return redirect('home')

@login_required
def crear_datos(request):
    if request.method == "GET":
        return render(request, 'servinquilino/crear_datos.html', {"form": DatosForm})
    else:
        try:
            form = DatosForm(request.POST)
            new_dato = form.save(commit=False)
            new_dato.user = request.user
            new_dato.save()
            return redirect('datos')
        except ValueError:
            return render(request, 'servinquilino/crear_datos.html',
                          {"form": DatosForm, "error": "Error creando Datos Inquilino."})

@login_required
def crear_expensas(request):
    if request.method == "GET":
        return render(request, 'servinquilino/crear_expensas.html', {"form": ExpensasForm})
    else:
        try:
            form = ExpensasForm(request.POST)
            new_expensa = form.save(commit=False)
            new_expensa.user = request.user
            new_expensa.save()
            return redirect('cuotas')
        except ValueError:
            return render(request, 'servinquilino/crear_expensas.html', {"form": ExpensasForm, "error": "Error creando Cuota."})

@login_required
def cuotas(request):
    cuotas = Expensa.objects.filter(user=request.user)
    return render(request, 'servinquilino/cuotas.html', {"cuotas": cuotas})


@login_required
def cuotas_pagas(request):
    cuotas = Expensa.objects.filter(user=request.user,
                                    fechapago__isnull=False).order_by('-fechapago')
    return render(request, 'servinquilino/cuotas.html', {"cuotas": cuotas})

@login_required
def pagar_cuota(request, IdExpensa):
    cuota = get_object_or_404(Expensa, pk=IdExpensa, user=request.user)
    if request.method == 'POST':
        cuota.pagado = cuota.importe
        cuota.fechapago = timezone.now()
        cuota.save()
        return redirect('cuotas')

@login_required
def borrar_cuota(request, IdExpensa):
    cuota = get_object_or_404(Expensa, pk=IdExpensa, user=request.user)
    if request.method == 'POST':
        cuota.delete()
        return redirect('cuotas')

@login_required
def detalle_cuotas(request, IdExpensa):
    if request.method == 'GET':
        cuota = get_object_or_404(Expensa, pk=IdExpensa, user=request.user)
        form = ExpensasForm(instance=cuota)
        return render(request, 'servinquilino/detalle_cuotas.html', {'cuota': cuota, 'form': form})
    else:
        try:
            cuota = get_object_or_404(Expensa, pk=IdExpensa, user=request.user)
            form = ExpensasForm(request.POST, instance=cuota)
            form.save()
            return redirect('cuotas')
        except ValueError:
            return render(request, 'servinquilino/detalle_cuotas.html', {'cuota': cuota, 'form': form, 'error': 'Error actualizando cuota.'})

@login_required
def datos(request):
    datos = Dato.objects.filter(user=request.user)
    return render(request, 'servinquilino/datos.html', {"datos": datos})

@login_required
def detalle_datos(request, IdUsuario):
    if request.method == 'GET':
        dato = get_object_or_404(Dato, pk=IdUsuario, user=request.user)
        form = DatosForm(instance=dato)
        return render(request, 'servinquilino/detalle_datos.html', {'dato': dato, 'form': form})
    else:
        try:
            dato = get_object_or_404(Dato, pk=IdUsuario, user=request.user)
            form = DatosForm(request.POST, instance=dato)
            form.save()
            return redirect('datos')
        except ValueError:
            return render(request, 'servinquilino/detalle_datos.html', {'dato': dato, 'form': form, 'error': 'Error actualizando Datos.'})

@login_required
def borrar_dato(request, IdUsuario):
    dato = get_object_or_404(Dato, pk=IdUsuario, user=request.user)
    if request.method == 'POST':
        dato.delete()
        return redirect('datos')

