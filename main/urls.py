from django.contrib import admin
from django.urls import path
from core.views import list_reserva, create, detail_reserva, delete_reserva

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', list_reserva, name='listagem'),
    path('cadastrar/', create, name='reserva_criar'),
    path('detalhes/<int:reserva_id>/', detail_reserva, name='detalhes_reserva'),
    path('excluir/<int:reserva_id>/', delete_reserva, name='excluir_reserva'),
]
