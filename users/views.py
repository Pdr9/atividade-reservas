from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import authenticate, login as auth_login  # Alias para a função de login do Django
from django.contrib.auth import logout

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()
    
        if user:
            error_message = 'Já existe um usuário com esse username'
            return render(request, 'cadastro.html', {'error_message': error_message})
        
        user = User.objects.create_superuser(username=username, email=email, password=senha)
        user.save()
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
