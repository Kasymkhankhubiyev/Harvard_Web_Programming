from django.shortcuts import render

from django.http import HttpRequest, HttpResponse

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'container/index.html')

def container1(request: HttpRequest) -> HttpResponse:
    return render(request, 'container/container1.html')

def container2(request: HttpRequest) -> HttpResponse:
    return render(request, 'container/container2.html')

def grid(request: HttpRequest) -> HttpResponse:
    return render(request, 'container/grid.html')

def typography(request: HttpRequest) -> HttpResponse:
    return render(request, 'container/typography.html')

def color(request: HttpRequest) -> HttpResponse:
    return render(request, 'container/colors.html')

def table(request: HttpRequest) -> HttpResponse:
    return render(request, 'container/table.html')

def image(request: HttpRequest) -> HttpResponse:
    return render(request, 'container/image.html')

def jumbotron(request: HttpRequest) -> HttpResponse:
    return render(request, 'container/jumbotron.html')

def buttons(request: HttpRequest) -> HttpResponse:
    return render(request, 'container/buttons.html')
