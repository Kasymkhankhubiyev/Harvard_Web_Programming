from django.shortcuts import render

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:  # if not loged in
        return HttpResponseRedirect(reverse("login"))
    return render(request, 'users/user.html')
    
def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        username = request.POST["username"]
        pswd = request.POST['password']
        user = authenticate(request, username=username, password=pswd)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, 'users/login.html', {
                "message": "invalid credentials.",
            })
    return render(request, "users/login.html")


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return render(request, 'users/login.html', {
        'message': 'Logged out.',
    })
