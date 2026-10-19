from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def ver_produto (request):
    return HttpResponse('Ola tudo bem ?')

def inserir_produto(request):
    return HttpResponse('Estou no inserir')