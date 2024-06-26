from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReservaForm
from .models import Reserva
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from rolepermissions.checkers import has_permission
from django.shortcuts import render, get_object_or_404
from rolepermissions.checkers import has_permission
from .models import Reserva
from django.shortcuts import render
from django.db.models import Sum, Count
from .models import Reserva
from django.shortcuts import render, redirect
from .models import Stand
from .forms import StandForm

def permission_required(permission):
    def decorator(view_func):
        @login_required
        def _wrapped_view(request, *args, **kwargs):
            if has_permission(request.user, permission):
                return view_func(request, *args, **kwargs)
            else:
                return redirect('home')  # ou você pode redirecionar para uma página de erro ou login
        return _wrapped_view
    return decorator

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

    # Adicionando permissões ao contexto
    context = {
        'reservas': reservas,
        'can_create': has_permission(request.user, 'criar_reservas'),
        'can_delete': has_permission(request.user, 'deletar_reservas'),
        'can_edit': has_permission(request.user, 'editar_reservas'),
        'is_gerente': request.user.has_perm('is_gerente'),
    }

    return render(request, 'core/home.html', context)

@permission_required('criar_reservas')
def create(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')

    form = ReservaForm()
    return render(request, "core/form.html", {'form': form})

@permission_required('deletar_reservas')
def delete_reserva(request, id):
    get_object_or_404(Reserva, pk=id).delete()
    return redirect('home')

def detail_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    
    context = {
        'reserva': reserva,
        'can_delete': has_permission(request.user, 'deletar_reservas'),
        'can_edit': has_permission(request.user, 'editar_reservas'),
    }
    
    return render(request, 'core/detail.html', context)

@permission_required('editar_reservas')
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

def lista_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'core/lista_usuarios.html', {'usuarios': usuarios})

@permission_required('app_name.is_gerente')
def financeiro(request):
    # Valor total arrecadado
    total_arrecadado = Reserva.objects.aggregate(Sum('stand__price'))['stand__price__sum']

    # Dia que mais vendeu ingressos
    vendas_por_dia = Reserva.objects.values('date__date').annotate(total=Count('id')).order_by('-total')
    dia_mais_vendas = vendas_por_dia[0] if vendas_por_dia else None

    # Artista que vendeu mais
    artista_mais_vendas = Reserva.objects.values('stand__artista').annotate(total_vendas=Count('id')).order_by('-total_vendas').first()
    if artista_mais_vendas:
        nome_artista_mais_vendas = artista_mais_vendas['stand__artista']
        total_vendas_artista_mais_vendas = artista_mais_vendas['total_vendas']
    else:
        nome_artista_mais_vendas = None
        total_vendas_artista_mais_vendas = None

    context = {
        'total_arrecadado': total_arrecadado,
        'dia_mais_vendas': dia_mais_vendas,
        'nome_artista_mais_vendas': nome_artista_mais_vendas,
        'total_vendas_artista_mais_vendas': total_vendas_artista_mais_vendas,
    }

    return render(request, 'core/financeiro.html', context)


@permission_required('app_name.is_gerente')
def criar_stand(request):
    stands = Stand.objects.all()  # Obtenha todos os stands do banco de dados
    if request.method == 'POST':
        form = StandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StandForm()
    return render(request, 'core/criar_stand.html', {'form': form, 'stands': stands})

@permission_required('app_name.is_gerente')
def editar_stand(request, stand_id):
    stand = get_object_or_404(Stand, id=stand_id)
    if request.method == 'POST':
        form = StandForm(request.POST, instance=stand)
        if form.is_valid():
            form.save()
            return redirect('criar_stand')
    else:
        form = StandForm(instance=stand)
    return render(request, 'core/editar_stand.html', {'form': form})

@permission_required('app_name.is_gerente')
def deletar_stand(request, stand_id):
    stand = get_object_or_404(Stand, id=stand_id)
    stand.delete()
    return redirect('criar_stand')
