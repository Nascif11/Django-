from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def ver_produto (request):
    if request.method == "GET":
        nome = 'Caio'
        return render(request, 'ver_produtos.html',{'nome':nome})
    elif request.method=="POST":
        nome= request.POST
        print(nome)
        return HttpResponse('fui chamado')

def inserir_produto(request):
    return HttpResponse('Estou no inserir')