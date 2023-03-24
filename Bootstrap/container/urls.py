from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("badges", views.badges, name="badges"),
    path("buttons", views.buttons, name="buttons"),
    path("cards", views.cards, name='cards'),
    path("carousel", views.carousel, name='carousel'),
    path("color", views.color, name='color'),
    path("container1", views.container1, name='container1'),
    path("container2", views.container2, name='container2'),
    path("dropdowns", views.dropdowns, name='dropdowns'),
    path("grid", views.grid, name='grid'),
    path("groupedbuttons", views.groupedbuttons, name='goupedbuttons'),
    path("image", views.image, name='image'),
    path("jumbotron", views.jumbotron, name='jumbotron'),
    path("modals", views.modals, name='modals'),
    path("navs", views.navs, name='navs'),
    path("navbar", views.navbar, name='navbar'),
    path("pagination", views.pagination, name='pagination'),
    path("scrollspy", views.scrollspy, name='scrollspy'),
    path("table", views.table, name='color'),
    path("toasts", views.toasts, name='toasts'),
    path("typography", views.typography, name='typography'),
]