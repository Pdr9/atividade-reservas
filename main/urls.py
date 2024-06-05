from django.contrib import admin
from django.urls import path
from core import views
from core.views import list_reserva, create, detail_reserva, delete_reserva

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', list_reserva, name='home'),
    path('create/', create, name='reserva_criar'),
    path('detail/<int:id>/', detail_reserva, name='detalhes_reserva'),
    path('delete/<int:id>/', delete_reserva, name='excluir_reserva'),
    path('edit/<int:id>/', views.edit_reserva, name='edit_reserva'),
]
