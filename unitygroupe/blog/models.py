from django.db import models
from tinymce import HTMLField
from django.contrib.auth.models import User
# Create your models here.


class Categorie(models.Model):
    image = models.ImageField(upload_to='blog/category')
    titre = models.CharField(max_length=200)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now=True)
    date_upd = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'categorie'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.titre

class Article(models.Model):
    """Model definition for Article."""

    titre = models.CharField(max_length=100)
    content = HTMLField('content')
    image = models.ImageField(upload_to='blog/image')
    category = models.ForeignKey('Categorie', on_delete=models.CASCADE,related_name='category_article')
    tag = models.ManyToManyField('Tag')
    author = models.ForeignKey('Author', on_delete=models.CASCADE,related_name='author_article')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now=True)
    date_upd = models.DateTimeField(auto_now_add=True)
    class Meta:
        """Meta definition for Article."""

        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        """Unicode representation of Article."""
        return '{}'.format(self.titre) # TODO
    
    
class Tag(models.Model):
    """Model definition for Tag."""

    titre = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now=True)
    date_upd = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Tag."""

        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        """Unicode representation of Tag."""
        return '{}'.format(self.titre) # TODO

class Author(models.Model):
    """Model definition for Author."""
    author = models.OneToOneField(User, on_delete=models.CASCADE,related_name='author')
    image = models.ImageField(upload_to='blog/image')
    description = models.TextField()
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now=True)
    date_upd = models.DateTimeField(auto_now_add=True)
    class Meta:
        """Meta definition for Author."""

        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        """Unicode representation of Author."""
        return '{}'.format(self.author ) # TODO

class Comment(models.Model):
    """Model definition for Comment."""
    article = models.ForeignKey(Article, on_delete=models.CASCADE,related_name='article_comment')
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    website = models.URLField()
    message = models.TextField()
    image = models.ImageField(upload_to='blog/comment',default='default.jpg')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now=True)
    date_upd = models.DateTimeField(auto_now_add=True)
    class Meta:
        """Meta definition for Comment."""

        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        """Unicode representation of Comment."""
        return '{}'.format(self.author ) # TODO

#./manage.py admin_generator config_app >> config_app/admin.py