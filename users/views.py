from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from rolepermissions.roles import assign_role

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')


        user = User.objects.filter(username=username).first()
    
        if user:
            error_message = 'Já existe um usuário com esse username'
            return render(request, 'cadastro.html', {'error_message': error_message})
        
        user = User.objects.create_user(username=username, email=email, password=senha, first_name=first_name, last_name=last_name)
        user.save()
        assign_role(user, 'gerente')
        return redirect('login')

    
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('senha')
        user = authenticate(username=username, password=password)

        if user:
            auth_login(request, user)  # Usando o alias para a função login do Django
            return redirect('home')  # Substitua 'home' pelo nome da sua página inicial após o login
        else: 
            error_message = 'Nome de usuário ou senha inválidos'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')
