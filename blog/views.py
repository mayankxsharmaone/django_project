from django.shortcuts import render
from django.http import HttpResponse


posts = [

    {
        'author': 'Mayank',
        'title':'Blog post 1',
        'content': 'First Post Content',
        'date_posted':'January 13th, 2023 ' 

    },
    {
        'author': 'test',
        'title':'Blog post 2',
        'content': 'Second Post Content',
        'date_posted': 'January 14th, 2023 ' 

    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'}) 