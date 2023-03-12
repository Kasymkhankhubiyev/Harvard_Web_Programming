from django.shortcuts import render

from django.http import HttpRequest, HttpResponse

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    # return HttpResponse("Hello, world!")
    return render(request, 'hello/index.html')

def kasym(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, Kasym!")

def azamat(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, Azamat!")

def greeting(request: HttpRequest, name: str) -> HttpResponse:
    """первый аргумент - это запрос,
    второй аргумент - это шаблон 
    третий аргумент - опциональный, содержит контекст, т.е. доп данные
    """
    # return HttpResponse(f'Hello, {name.capitalize()}!')
    return render(request, 'hello/greeting.html', {
        "name": name.capitalize(),
    })