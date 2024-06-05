from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReservaForm
from .models import Reserva


def list_reserva(request):
    name = request.GET.get("name", "")
    date = request.GET.get("date", "")
    price = request.GET.get("price", "") 
    quitado = request.GET.get("quitado")

    reservas = Reserva.objects.all()

    if name:
        reservas = reservas.filter(name__icontains=name)
    if date:
        reservas = reservas.filter(date__contains=date)
    if price:
        reservas = reservas.filter(stand__price__icontains=price)
    if quitado is not None:
        if quitado.lower() == "true":
            reservas = reservas.filter(quitado=True)
        elif quitado.lower() == "false":
            reservas = reservas.filter(quitado=False)

    return render(request, 'core/home.html', {'reservas': reservas})


def create(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')

    form = ReservaForm()
    return render(request, "core/form.html", {'form': form})


def delete_reserva(request, id):
    get_object_or_404(Reserva, pk=id).delete()
    return redirect('home')


def detail_reserva(request, id):
    reserva = get_object_or_404(Reserva, pk=id)
    return render(request, 'core/detail.html', {'reserva': reserva})

def edit_reserva(request, id):
    reserva = get_object_or_404(Reserva, pk=id)
    if request.method == 'POST':
        form = ReservaForm(request.POST, request.FILES, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'core/form.html', {'form': form})