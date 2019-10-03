from django.db import models

# Create your models here.

class Reservation(models.Model):
    """Model definition for Reservation."""

    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    typeYatch = models.ForeignKey('TypeYatch', on_delete=models.CASCADE,related_name='type_ yatch_reservation')
    email = models.EmailField(max_length=254)
    number = models.IntegerField()
    note = models.TextField()
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now=True)
    date_upd = models.DateTimeField(auto_now_add=True)
    class Meta:
        """Meta definition for Reservation."""

        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

    def __str__(self):
        """Unicode representation of Reservation."""
        return '{}'.format(self.name ) # TODO

class Yatch(models.Model):
    """Model definition for Yatch."""

    nom = models.CharField(max_length=150)
    types = models.ForeignKey('TypeYatch', on_delete=models.CASCADE,related_name='type_yatch')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now=True)
    date_upd = models.DateTimeField(auto_now_add=True)   

    class Meta:
        """Meta definition for Yatch."""

        verbose_name = 'Yatch'
        verbose_name_plural = 'Yatchs'

    def __str__(self):
        """Unicode representation of Yatch."""
        return '{}'.format(self.nom ) # TODO

class TypeYatch(models.Model):
    """Model definition for TypeYatch."""
    name = models.CharField(max_length=150)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now=True)
    date_upd = models.DateTimeField(auto_now_add=True)   
    class Meta:
        """Meta definition for TypeYatch."""

        verbose_name = 'TypeYatch'
        verbose_name_plural = 'TypeYatchs'

    def __str__(self):
        """Unicode representation of TypeYatch."""
        return '{}'.format(self.name ) # TODO


class Destination(models.Model):
    """Model definition for Destination."""

    pays_depart = models.ForeignKey('Pays', on_delete=models.CASCADE,related_name='pays_destination_depart')
    pays_arrive = models.ForeignKey('Pays', on_delete=models.CASCADE,related_name='pays_destination_arrive')
    prix = models.IntegerField()
    date_depart = models.DateTimeField()
    date_arrive = models.DateTimeField()
    description = models.TextField()
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now=True)
    date_upd = models.DateTimeField(auto_now_add=True)
    class Meta:
        """Meta definition for Destination."""

        verbose_name = 'Destination'
        verbose_name_plural = 'Destinations'

    def __str__(self):
        """Unicode representation of Destination."""
        return '{} - {}'.format(self.pays_depart,self.pays_arrive)
    
class Pays(models.Model):
    """Model definition for Pays."""
    nom = models.CharField(max_length=150)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now=True)
    date_upd = models.DateTimeField(auto_now_add=True)
    class Meta:
        """Meta definition for Pays."""

        verbose_name = 'Pays'
        verbose_name_plural = 'Pays'

    def __str__(self):
        """Unicode representation of Pays."""
        return '{}'.format(self.nom ) # TODO

