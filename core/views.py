from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .forms import ReservaForm
from .models import Reserva
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='/admin/login/?next=/')
def list_reserva(request):
    name = request.GET.get("name") if request.GET.get("name") is not None else ""
    date = request.GET.get("date") if request.GET.get("date") is not None else ""
    price = request.GET.get("price") if request.GET.get("price") is not None else "" 
    quitado = request.GET.get("quitado")

    if request.GET.get("name") is not None:
        reservas = Reserva.objects.filter(
            Q(name__icontains=name) &
            Q(date__contains=date) &
            Q(stand__price__icontains=price)
        )
        if quitado is not None:
            reservas = reservas.filter(quitado=quitado)
    else:
        reservas = Reserva.objects.all()

    paginator = Paginator(reservas, 5)

    page = request.GET.get('page')

    return render(request, 'core/home.html', {
        'reservas': reservas,
        'page_obj': paginator.get_page(page)})


@login_required(login_url='/admin/login/?next=/')
def create(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')

    form = ReservaForm()
    return render(request, "core/form.html", {'form': form})


@login_required(login_url='/admin/login/?next=/')
def delete_reserva(request, id):
    get_object_or_404(Reserva, pk=id).delete()
    return redirect('home')


@login_required(login_url='/admin/login/?next=/')
def detail_reserva(request, id):
    reserva = get_object_or_404(Reserva, pk=id)
    return render(request, 'core/detail.html', {'reserva': reserva})


def logout_view(request):
    logout(request)
    return redirect('home')
