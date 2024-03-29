from django.shortcuts import render, redirect
from .models import Articles
# Create your views here.


def create(request):
    a = request.POST
    article = Articles()
    article.title = a.get('title')
    article.content = a.get('content')
    article.image = request.FILES.get('image')
    article.save()
    return render(request, 'Articles/create.html')


def delete(request, g_pk):
    a = Articles.objects.get(pk=g_pk)
    a.delete()
    return render(request, 'Articles/delete.html')


def delete_all(request):
    Articles.objects.all().delete()
    return redirect('/Articles')


def detail(request, g_pk):
    a = Articles.objects.get(pk=g_pk)
    context = {
        'a': a
    }
    return render(request, 'Articles/detail.html', context)


def edit(request, g_pk):
    a = Articles.objects.get(pk=g_pk)
    a.title = request.GET.get('title')
    a.content = request.GET.get('content')
    a.save()
    return render(request, 'Articles/create.html')


def fix(request, g_pk):
    a = Articles.objects.get(pk=g_pk)
    context = {
        'a': a
    }
    return render(request, 'Articles/fix.html', context)


def index(request):
    a = Articles.objects.all()
    context = {
        'a': a
    }
    return render(request, 'Articles/index.html', context)


def new(request):
    return render(request, 'Articles/new.html')






