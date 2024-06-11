from django.urls import path
from .views import list_reserva, create, detail_reserva, delete_reserva, edit_reserva, lista_usuarios
from django.urls import path
from .views import financeiro, criar_stand, editar_stand, deletar_stand
urlpatterns = [
    path('', list_reserva, name='home'),
    path('create/', create, name='reserva_criar'),
    path('detail/<int:id>/', detail_reserva, name='detalhes_reserva'),
    path('delete/<int:id>/', delete_reserva, name='excluir_reserva'),
    path('edit/<int:id>/', edit_reserva, name='edit_reserva'),
    path('lista_usuarios/', lista_usuarios, name='lista_usuarios'),
    path('financeiro/', financeiro, name='financeiro'),
    path('criar_stand/', criar_stand, name='criar_stand'),
    path('editar_stand/<int:stand_id>/', editar_stand, name='editar_stand'),
    path('deletar_stand/<int:stand_id>/', deletar_stand, name='deletar_stand'),
]