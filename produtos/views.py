from django.shortcuts import render
from django.http import HttpResponse
from . models import Pessoa

#Chamar página html dentro de templates 
#Tratar dados do banco de dados Controller / Views 
def ver_produto(request):
   if request.method == "GET": 
      nome = 'Carlos'
      return render(request, 'ver_produto.html', {'nome' : nome})
   elif request.method == "POST":
      nome = request.POST.get('nome')
      idade = request.POST.get('idade')

      #Salvar no banco de dados
      #pessoa = Pessoa(nome=nome, idade=idade)
      #pessoa.save()

      #Visualizar dados do banco de dados na views
      pessoas = Pessoa.objects.filter(nome=nome)
      print(pessoas)     

      return HttpResponse(pessoas)

def inserir_produto(request):
   return render(request, 'inserir_produto.html')
