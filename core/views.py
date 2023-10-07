from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Reserva
from .forms import ReservaForm


def create(request):
    """Cria uma nova reserva."""
    if request.method == 'POST':
        form = ReservaForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('listagem')

    form = ReservaForm()
    return render(request, "core/form.html", {'form': form})


def list_reserva(request):
    name = request.GET.get("nome") if request.GET.get("nome") is not None else ""
    date = request.GET.get("date") if request.GET.get("date") is not None else ""
    price = request.GET.get("price") if request.GET.get("price") is not None else "" 
    quitado = request.GET.get("quitado")

    if request.GET.get("name") is not None:
        reservas = Reserva.objects.filter(
            Q(nome_empresa__icontains=name) &
            Q(data_reserva__contains=date) &
            Q(stand__valor__icontains=price)
        )
        if quitado is not None:
            reservas = reservas.filter(quitado=quitado)
    else:
        reservas = Reserva.objects.all()

    return render(request, 'core/home.html', {'reservas': reservas})


def detail_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, pk=reserva_id)
    return render(request, 'core/detail.html', {'reserva': reserva})


def delete_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    reserva.delete()
    return redirect('listagem')
