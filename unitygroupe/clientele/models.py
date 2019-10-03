from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Clent(models.Model):
    icon = models.CharField(max_length=250)
    titre = models.CharField(max_length=250)
    description = models.TextField()
    status = models.BooleanField()
    date_add = models.DateTimeField(auto_now=True)
    date_upd= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titre
    
class Testimonial(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='auteurTest')
    images = models.ImageField(upload_to='img')
    descriptions = models.TextField()
    status = models.BooleanField()
    date_add = models.DateTimeField(auto_now=True)
    date_upd= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titre
    
    
    
    
    
