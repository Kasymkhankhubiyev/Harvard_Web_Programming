from django.urls import path

from . import views

app_name = 'scrollable_page'
urlpatterns = [
    path("", views.index, name='index'),
    path("news", views.news, name='news'),
]