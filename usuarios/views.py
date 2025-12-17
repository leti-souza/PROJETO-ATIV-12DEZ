from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario

# Create your views here.

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'usuarios/cadastro.html')

    elif request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        Usuario.objects.create(email=email, senha=senha)
        return HttpResponse('Usuário cadastrado com sucesso!')


def login(request):
    if request.method == 'GET':
        return render(request, 'usuarios/login.html')

    elif request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        try:
            Usuario.objects.get(email=email, senha=senha)
            return render(request, 'home/home.html')
        #return HttpResponse('Login realizado com sucesso!')
        except Usuario.DoesNotExist:
            return HttpResponse('Usuário ou senha inválidos')

