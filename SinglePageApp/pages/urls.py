from django.urls import path

from . import views

app_name = 'pages'
urlpatterns = [
    path("", views.index, name='index'),
    path("news", views.news, name='news'),
]