from django.shortcuts import render, redirect
from climateweb.models import EchoChoice
from author.models import Author, Article, User


def index(request):
    stories = Article.objects.all()
    echos = EchoChoice.objects.all()
    context = {
        'stories': stories,
        'echos': echos,
    }
    return render(request, 'home.html', context)


def detail(request, pk):
    story = Article.objects.get(pk=pk)
    return render(request, 'detail.html', {'story': story})


def detail2(request, pk):
    echo = EchoChoice.objects.get(pk=pk)
    return render(request, 'detail2.html', {'echo': echo})

