<<<<<<< HEAD
from django.shortcuts import render, redirect, get_object_or_404
=======

from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
>>>>>>> 4798a7a7375c2592135db3e07638f89d7a77bb53
from .models import Reserva
from .forms import ReservaForm


def reserva_criar(request):
<<<<<<< HEAD
    """Cria uma nova reserva."""
    form = ReservaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('listagem')
=======
    if request.method == 'POST':
        form = ReservaForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('listagem')

    else:
        form = ReservaForm()

>>>>>>> 4798a7a7375c2592135db3e07638f89d7a77bb53
    return render(request, "core/cadastro.html", {'form': form})


def listagem(request):
<<<<<<< HEAD
    """Lista todas as reservas."""
    reservas = Reserva.objects.all()
    return render(request, 'core/listagem.html', {'reservas': reservas})

def detalhes_reserva(request, reserva_id):
    """Exibe os detalhes de uma reserva."""
    reserva = get_object_or_404(Reserva, id=reserva_id)
=======
    query = request.GET.get("q") if request.GET.get("q") is not None else ""
    data_reserva = request.GET.get("data_reserva") if request.GET.get("data_reserva") is not None else ""
    valor = request.GET.get("valor") if request.GET.get("valor") is not None else ""
    quitado = request.GET.get("quitado") 
    print(quitado)

    if request.GET.get("q") is not None:
        reservas = Reserva.objects.filter(
            Q(nome_empresa__icontains=query) &
            Q(data_reserva__contains=data_reserva) &
            Q(stand__valor__icontains=valor)
        )
        if quitado is not None:
            reservas = reservas.filter(quitado=quitado)
    else:
        reservas = Reserva.objects.all()

    return render(request, 'core/listagem.html', 
                  {'reservas': reservas, 'query': query, 'valor':valor, 'data_reserva':data_reserva, 'quitado':quitado})  


def detalhes_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, pk=reserva_id)
>>>>>>> 4798a7a7375c2592135db3e07638f89d7a77bb53
    return render(request, 'core/detalhes_reserva.html', {'reserva': reserva})


def excluir_reserva(request, reserva_id):
    """Exclui uma reserva."""
    reserva = get_object_or_404(Reserva, id=reserva_id)
    reserva.delete()
    return redirect('listagem')
