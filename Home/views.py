#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home_page(solicitacao):
    return HttpResponse('Olá, mundo!')