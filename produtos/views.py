from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def ver_produto (request):
    nome = 'Caio'
    return render(request, 'ver_produtos.html',{'nome':nome})

def inserir_produto(request):
    return HttpResponse('Estou no inserir')