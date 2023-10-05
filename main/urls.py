from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listagem, name='listagem'),
    path('cadastrar/', reserva_criar, name='reserva_criar'),
    path('detalhes/<int:reserva_id>/', detalhes_reserva, name='detalhes_reserva'),
    path('excluir/<int:reserva_id>/', excluir_reserva, name='excluir_reserva'),
]
