from django.shortcuts import render

from django.http import HttpRequest, HttpResponse
from .models import Flight

# Create your views here.
def index(request) -> HttpResponse:
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })
