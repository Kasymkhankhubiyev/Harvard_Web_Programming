from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("kasym", views.kasym, name="kasym"),
    path("azamat", views.azamat, name="azamat"),
]