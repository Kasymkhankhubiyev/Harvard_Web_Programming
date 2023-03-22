from django.shortcuts import render

from django.http import HttpRequest, HttpResponse, JsonResponse

posts = ['post1', 'post2', 'post3', 'post4', 'post5', 'post6', 
         'post7', 'post8', 'post9', 'post10', 'post11', 'post12', 
         'post13', 'post14', ]

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    # return HttpResponse('Hello, Kasym! It will be a scrollable page')
    return render(request, 'pages/index.html')

def news(request: HttpRequest) -> HttpResponse:
    return render(request, 'pages/news.html')

def posts(request: HttpRequest) -> HttpResponse:
    # Get start and end points
    start = int(request.GET.get('start') or 0)
    end = int(request.GET.get('end') or (start + 7))

    # Generate a list of posts:
    data = []
    for i in range(start, end + 1):
        data.append(f'Post #{i}')

    # return render(request, 'pages/news.html', {
    #     'posts': data
    # })
    return JsonResponse({
        "posts": data
    })
