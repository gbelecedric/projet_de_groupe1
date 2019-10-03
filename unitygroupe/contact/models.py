from django.db import models

# Create your models here.

class  Contact(models.Model):
    nom = models.CharField(max_length=250)
    prenom = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    tel = models.IntegerField()
    message = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nom
