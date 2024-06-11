from django.urls import path
from . import views
from django.urls import path
from .views import user_logout

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('logout/', user_logout, name='logout'),
]