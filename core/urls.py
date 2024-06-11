from django.urls import path
from .views import list_reserva, create, detail_reserva, delete_reserva, edit_reserva, lista_usuarios

urlpatterns = [
    path('', list_reserva, name='home'),
    path('create/', create, name='reserva_criar'),
    path('detail/<int:id>/', detail_reserva, name='detalhes_reserva'),
    path('delete/<int:id>/', delete_reserva, name='excluir_reserva'),
    path('edit/<int:id>/', edit_reserva, name='edit_reserva'),
    path('lista_usuarios/', lista_usuarios, name='lista_usuarios'),
    
]