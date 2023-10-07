from django.contrib import admin
from .models import Reserva, Stand


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('cnpj', 'name', 'category', 'quitado')


@admin.register(Stand)
class StandAdmin(admin.ModelAdmin):
    list_display = ('location', 'price')
