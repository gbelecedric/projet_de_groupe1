from django.shortcuts import render

# Create your views here.
def blog(request):
    
    
    data ={}

    return render(request, 'pages/blog/blog.html',data)


def categorie_blog(request):
    
    
    data ={}

    return render(request, 'pages/blog/categorie.html',data)
def single_blog(request):
        
    data ={}

    return render(request, 'pages/blog/single-blog.html',data)
def tag_article(request):
    
    
    data ={}

    return render(request, 'pages/blog/blog.html',data)
def description(request):
    
    
    
    data ={}

    return render(request, 'pages/blog/description.html',data)