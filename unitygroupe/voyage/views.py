from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'pages/voyage/index.html')

def about(request):
    return render(request, 'pages/voyage/about.html')

def service(request):
    return render(request, 'pages/voyage/service.html')

def testimonial(request):
    return render(request, 'pages/voyage/testimonial.html')

def projet_single(request):
    return render(request, 'pages/voyage/projet-single.html')