from django.db import models
from config_app.models import Social
# Create your models here.

class Service(models.Model):
    """Model definition for Service."""

    titre = models.CharField(max_length=50)
    description = models.TextField()
    font = models.ForeignKey('Font', on_delete=models.CASCADE,related_name='font_service')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now=True)
    date_upd = models.DateTimeField(auto_now_add=True)
    class Meta:
        """Meta definition for Service."""

        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        """Unicode representation of Service."""
        return '{}'.format(self.titre ) # TODO

class Address(models.Model):
    """Model definition for address."""

    address = models.CharField(max_length=500)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now=True)
    date_upd = models.DateTimeField(auto_now_add=True)
    class Meta:
        """Meta definition for address."""
        verbose_name = 'Address'
        verbose_name_plural = 'Addresss'

    def __str__(self):
        """Unicode representation of address."""
        return '{}'.format(self.address) # TODO

class Entreprise(models.Model):
    """Model definition for Entreprise."""

    email = models.EmailField(max_length=254)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='entreprise')
    description = models.TextField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE,related_name='address_entreprise')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now=True)
    date_upd = models.DateTimeField(auto_now_add=True)
    class Meta:
        """Meta definition for Entreprise."""

        verbose_name = 'Entreprise'
        verbose_name_plural = 'Entreprises'

    def __str__(self):
        """Unicode representation of Entreprise."""
        return '{}'.format(self.name ) # TODO

class Personnel(models.Model):
    """Model definition for Personnel."""

    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='entreprise/personnel')
    job = models.ForeignKey('Job', on_delete=models.CASCADE,related_name='job_presonnel')
    social = models.ManyToManyField(Social,related_name='social_personnel')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now=True)
    date_upd = models.DateTimeField(auto_now_add=True)
    class Meta:
        """Meta definition for Personnel."""

        verbose_name = 'Personnel'
        verbose_name_plural = 'Personnels'

    def __str__(self):
        """Unicode representation of Personnel."""
        return '{}'.format(self.name) 


class Font(models.Model):
    """Model definition for Font."""
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now=True)
    date_upd = models.DateTimeField(auto_now_add=True)
    class Meta:
        """Meta definition for Font."""
        verbose_name = 'Font'
        verbose_name_plural = 'Fonts'

    def __str__(self):
        """Unicode representation of Font."""
        return '{}'.format(self.name )

class Job(models.Model):
    """Model definition for Job."""
    titre = models.CharField(max_length=150)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now=True)
    date_upd = models.DateTimeField(auto_now_add=True)
    class Meta:
        """Meta definition for Job."""

        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'

    def __str__(self):
        """Unicode representation of Job."""
        return '{}'.format(self.titre ) # TODO
