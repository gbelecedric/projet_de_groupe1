
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about', views.about, name = 'about'),
    path('service', views.service, name = 'service'),
    path('testimonial', views.testimonial, name = 'testimonial'),
    path('single', views.projet_single, name = 'projet_single'),
]
