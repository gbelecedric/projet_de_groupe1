from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog, name="blog"),
    path('categorie/<int:category>', views.categorie_blog, name="categorie_blog"),
    path('single_blog/<int:id>', views.single_blog, name="single_blog"),
    path('tag_article/<int:tag>', views.tag_article, name="tag_article"),
    path('description/<int:auteur>', views.description, name="description"),
]



