from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class CategorieAdmin(admin.ModelAdmin):

    list_display = ('id', 'image', 'titre', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'image',
        'titre',
        'status',
        'date_add',
        'date_upd',
    )


class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titre',
        'content',
        'image',
        'category',
        'author',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'category',
        'author',
        'status',
        'date_add',
        'date_upd',
        'id',
        'titre',
        'content',
        'image',
        'category',
        'author',
        'status',
        'date_add',
        'date_upd',
    )
    raw_id_fields = ('tag',)


class TagAdmin(admin.ModelAdmin):

    list_display = ('id', 'titre', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'titre',
        'status',
        'date_add',
        'date_upd',
    )


class AuthorAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'author',
        'image',
        'description',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'author',
        'status',
        'date_add',
        'date_upd',
        'id',
        'author',
        'image',
        'description',
        'status',
        'date_add',
        'date_upd',
    )


class CommentAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'article',
        'name',
        'email',
        'website',
        'message',
        'image',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'article',
        'status',
        'date_add',
        'date_upd',
        'id',
        'article',
        'name',
        'email',
        'website',
        'message',
        'image',
        'status',
        'date_add',
        'date_upd',
    )
    search_fields = ('name',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Categorie, CategorieAdmin)
_register(models.Article, ArticleAdmin)
_register(models.Tag, TagAdmin)
_register(models.Author, AuthorAdmin)
_register(models.Comment, CommentAdmin)
