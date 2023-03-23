from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("container1", views.container1, name='container1'),
    path("container2", views.container2, name='container2'),
    path("grid", views.grid, name='grid'),
    path("typography", views.typography, name='typography'),
    path("color", views.color, name='color'),
]