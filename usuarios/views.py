from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario

# Create your views here.

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')

    elif request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        Usuario.objects.create(email=email, senha=senha)

        return HttpResponse('Usuário cadastrado com sucesso!')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    elif request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        try:
            Usuario.objects.get(email=email, senha=senha)
            return HttpResponse('Login realizado com sucesso!')
        except Usuario.DoesNotExist:
            return HttpResponse('Usuário ou senha inválidos')

def home(request):
    return render(request, 'usuarios/home.html')