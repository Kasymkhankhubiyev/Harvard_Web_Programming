from django.shortcuts import render

from django.http import HttpRequest, HttpResponse

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, world!")

def kasym(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, Kasym!")

def azamat(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, Azamat!")