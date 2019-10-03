from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Social(models.Model):
    icon = models.CharField(max_length=250)
    nom = models.CharField(max_length=250)
    status = models.BooleanField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nom
    
class DetailEntreprise(models.Model):
    titre = models.CharField(max_length=250)
    images = models.ImageField(upload_to='img')
    descriptions = models.TextField()
    status = models.BooleanField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titre
    
class Foot(models.Model):
    titre = models.CharField(max_length=250)
    status = models.BooleanField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titre
    
class Foot_Liens(models.Model):
    foot = models.ForeignKey(Foot, on_delete=models.CASCADE, related_name='Liens_Foot')
    lien = models.URLField()
    status = models.BooleanField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd= models.DateTimeField(auto_now=True)
    
class GetFoot(models.Model):
    titre = models.CharField(max_length=250)
    images = models.ImageField(upload_to='img')
    description = models.TextField()
    status = models.BooleanField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titre
    
class Section(models.Model):
    section = models.IntegerField()
    titre = models.CharField(max_length=250)
    sous_titre = models.CharField(max_length=250)
    status = models.BooleanField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titre
    
class Menu(models.Model):
    nom = models.CharField(max_length=250)
    titre = models.CharField(max_length=250)
    descriptions = models.TextField()
    images = models.ImageField(upload_to='menu')
    status = models.BooleanField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd= models.DateTimeField(auto_now=True)
    
class Cart(models.Model):
    titre = models.CharField(max_length=250)
    descriptions = models.TextField()
    status = models.BooleanField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd= models.DateTimeField(auto_now=True)
