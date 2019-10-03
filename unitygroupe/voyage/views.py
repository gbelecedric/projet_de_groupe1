from django.shortcuts import render,redirect
from .models import Destination
from unitygroupe.entreprise.models import Service
# Create your views here.
def home(request):
    if request.method == 'GET':
        voyage = Destination.objects.filter(status=True)[:6]
        data ={
            'voyage':voyage,
        }
        return render(request, 'pages/voyage/index.html',data)
    return redirect('home')

def about(request):
    return render(request, 'pages/voyage/about.html')

def service(request):
    if request.method == 'GET':
        service = Destination.objects.filter(status=True)
        data ={
            'service':service,
        }
        return render(request, 'pages/voyage/service.html',data)
    return redirect('home')

def testimonial(request):
    return render(request, 'pages/voyage/testimonial.html')

def projet_single(request):
    return render(request, 'pages/voyage/projet-single.html')