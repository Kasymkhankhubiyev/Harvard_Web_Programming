from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("buttons", views.buttons, name="buttons"),
    path("color", views.color, name='color'),
    path("container1", views.container1, name='container1'),
    path("container2", views.container2, name='container2'),
    path("grid", views.grid, name='grid'),
    path("image", views.image, name='image'),
    path("jumbotron", views.jumbotron, name='jumbotron'),
    path("table", views.table, name='color'),
    path("typography", views.typography, name='typography'),
]