from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog, name="blog"),
    path('categorie', views.categorie_blog, name="categorie_blog"),
    path('single_blog', views.single_blog, name="single_blog"),
    path('tag_article', views.tag_article, name="tag_article"),
    path('description', views.description, name="description"),
]



