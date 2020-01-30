from django.shortcuts import render,redirect
from .models import Article,Categorie,Tag,Author
from django.core.paginator import Paginator 
# Create your views here.
def blog(request):
    paginator = Paginator(Article.objects.filter(status=True).order_by('date_add'),6)
    if request.method == 'GET':
        page=request.GET.get('page',1)
        articles = paginator.page(page)
        data ={
            'articles':articles,
        }
        return render(request, 'pages/blog/blog.html',data)
    return redirect('home')

def categorie_blog(request,category):
    paginator = Paginator(Article.objects.filter(category=category).order_by('date_add'),6)
    if request.method == 'GET':
        page=request.GET.get('page',1)
        articles = paginator.page(page)
        data ={
            'articles':articles,
        }
        return render(request, 'pages/blog/categorie.html',data)
    return redirect('home')
def single_blog(request,id):
    if request.method == 'GET':
        articles = Article.objects.get(pk=id)
        data ={
            'articles':articles,
        }
        return render(request, 'pages/blog/single-blog.html',data)
    return redirect('home')
def tag_article(request,tag):
    paginator = Paginator(Article.objects.filter(tag=tag).order_by('date_add'),6)
    if request.method == 'GET':
        page=request.GET.get('page',1)
        articles = paginator.page(page)
        data ={
            'articles':articles,
        }
        return render(request, 'pages/blog/blog.html',data)
    return redirect('home')
def description(request,auteur):
    if request.method == 'GET':
        Auteur=Author.objects.get(pk=auteur)
        data ={
            'auteur':Auteur
        }
        return render(request, 'pages/blog/description.html',data)
    return redirect('home')