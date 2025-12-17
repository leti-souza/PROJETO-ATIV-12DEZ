from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from .models import Usuario
# Create your views here.

def home(request):
     if request.method == 'GET': 
        return render(request, 'home.html')
     elif request.method == 'POST': 
        nome = request.POST.get('nome') 
        email = request.POST.get('email') 
        # Instanciando e salvando 
        user = Usuario(nome=nome, email=email) 
        user.save() 
        return HttpResponse(f'Usuário {nome} salvo com sucesso!') 
     
     from django.shortcuts import render

def login(request):
    return render(request, 'home/login.html')


   # return render(request, "home.html", {"message": "Olá, mundo!"})

