from django.shortcuts import render, HttpResponse
#                              |          |
#                              |          +--> transforma argumentos em resposta HTTP
#                              +--> renderiza HTML


# Create your views here.

def hello(request): # método "hello" que recebe os parâmetros da request
    return HttpResponse('Hello World!') # e retorna resposta HTTP
