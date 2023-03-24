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

def groupedbuttons(request: HttpRequest) -> HttpResponse:
    return render(request, 'container/groupbtns.html')

def badges(request: HttpRequest) -> HttpResponse:
    return render(request, 'container/badges.html')

def pagination(request: HttpRequest) -> HttpResponse:
    return render(request, 'container/pagination.html')

def cards(request: HttpRequest) -> HttpResponse:
    return render(request, 'container/cards.html')

def dropdowns(request: HttpRequest) -> HttpResponse:
    return render(request, 'container/dropdowns.html')

def navs(request: HttpRequest) -> HttpResponse:
    return render(request, 'container/navs.html')

def navbar(request: HttpRequest) -> HttpResponse:
    return render(request, 'container/navbar.html')

def carousel(request: HttpRequest) -> HttpResponse:
    return render(request, 'container/carousel.html')

def modals(request: HttpRequest) -> HttpResponse:
    return render(request, 'container/modals.html')

def toasts(request: HttpRequest) -> HttpResponse:
    return render(request, 'container/toasts.html')

def scrollspy(request: HttpRequest) -> HttpResponse:
    return render(request, 'container/scrollspy.html')
