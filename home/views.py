from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from .models import Usuario
# Create your views here.


def home(request):
    return render(request, 'home/home.html')


   # return render(request, "home.html", {"message": "Olá, mundo!"})

