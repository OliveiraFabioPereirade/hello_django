from django.shortcuts import render, HttpResponse
#                              |          |
#                              |          +--> transforma argumentos em resposta HTTP
#                              +--> renderiza HTML


# Create your views here.

def hello(request, nome, idade): # método "hello" que recebe os parâmetros da request, nome e idade
    return HttpResponse('<h1>Olá {} de {} anos de idade!' .format(nome, idade)) # e retorna resposta HTTP
