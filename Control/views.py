from django.shortcuts import render, HttpResponseRedirect
from Control.forms import Formulario1
from Control.models import Cliente

def home(request):
    return render(request, "Control/Home.html")

def menu(request):
    return render(request, "Control/Menu.html")

def formulario(request):
    return render(request, "Control/Formulario.html")

def formulario2(request):
    return render(request, "Control/Formulario2.html")

def carrito(request):
    return render(request, "Control/carrito.html")

def finscripcion(request):
    if request.method == "POST":
        form = Formulario1(request.POST)
        if form.is_valid():
            cliente = Cliente(
                nombre=form.cleaned_data['nombre'],
                apellidos=form.cleaned_data['apellidos'],
                RUT=form.cleaned_data['RUT'],
                mail=form.cleaned_data['mail'],
                telefono=form.cleaned_data['telefono'],
                direccion=form.cleaned_data['direccion']
            )
            cliente.save()
            return HttpResponseRedirect('/exito/')
    else:
        form = Formulario1()
    
    return render(request, 'formulario2.html', {'form': form})