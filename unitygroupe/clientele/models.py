from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Clent(models.Model):
    icon = models.ManyToManyField("Social", verbose_name=("social_clent"))
    nom = models.CharField(max_length=250)
    job = models.CharField(max_length=250)
    image = models.ImageField(upload_to='blog/comment',default='default.jpg')
    status = models.BooleanField()
    date_add = models.DateTimeField(auto_now=True)
    date_upd= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nom
    
class Testimonial(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='auteurTest')
    images = models.ImageField(upload_to='img')
    descriptions = models.TextField()
    status = models.BooleanField()
    date_add = models.DateTimeField(auto_now=True)
    date_upd= models.DateTimeField(auto_now=True)
    
    
class Social(models.Model):
    icon = models.CharField(max_length=250)
    nom = models.CharField(max_length=250)
    status = models.BooleanField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nom
    
    
    
    
    
