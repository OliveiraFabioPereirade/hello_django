from django.shortcuts import render, HttpResponse
#                              |          |
#                              |          +--> transforma argumentos em resposta HTTP
#                              +--> renderiza HTML


# Create your views here.

def hello(request, nome, idade): # método "hello" que recebe os parâmetros da request, nome e idade
    return HttpResponse('<h1>Olá {} de {} anos de idade!' .format(nome, idade)) # e retorna resposta HTTP

def add(request, n1, n2): # método "add" que recebe os parâmetros da request, e os números n1 e n2
    total = n1 + n2 # soma os números n1 e n2
    return HttpResponse('<h1> Somando {} e {} temos: {}' .format(n1, n2, total)) # e retorna resposta HTTP

def sub(request, n1, n2): # método "sub" que recebe os parâmetros da request, e os números n1 e n2
    total = n1 - n2 # subtrai do número n1 o número n2
    return HttpResponse('<h1> Subtraindo {} de {} temos: {}' .format(n2, n1, total)) # e retorna resposta HTTP

def mul(request, n1, n2): # método "sub" que recebe os parâmetros da request, e os números n1 e n2
    total = n1 * n2 # multiplica os números n1 e n2
    return HttpResponse('<h1> Multiplicando {} por {} temos: {}' .format(n1, n2, total)) # e retorna resposta HTTP

def div(request, n1, n2): # método "div" que recebe os parâmetros da request, e os números n1 e n2
    total = n1 / n2 # divide o número n1 pelo número n2
    return HttpResponse('<h1> Dividindo {} por {} temos: {}' .format(n1, n2, total)) # e retorna resposta HTTP

