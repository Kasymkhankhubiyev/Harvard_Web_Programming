from django.shortcuts import render

from django.http import HttpRequest, HttpResponse

posts = ['post1', 'post2', 'post3', 'post4', 'post5', 'post6', 
         'post7', 'post8', 'post9', 'post10', 'post11', 'post12', 
         'post13', 'post14', ]

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    # return HttpResponse('Hello, Kasym! It will be a scrollable page')
    return render(request, 'pages/index.html')

def news(request: HttpRequest) -> HttpResponse:
    return render(request, 'pages/news.html', {
        'posts': posts[:7]
    })
