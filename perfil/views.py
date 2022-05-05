import re
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def perfil(request):
    return render(request, 'perfil.html')
    


def sobre(request):
    return render(request, 'sobre.html')


def contato(request):
    return render(request, 'contato.html')