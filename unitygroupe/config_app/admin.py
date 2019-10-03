from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class SocialAdmin(admin.ModelAdmin):

    list_display = ('id', 'icon', 'nom', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'icon',
        'nom',
        'status',
        'date_add',
        'date_upd',
    )


class DetailEntrepriseAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titre',
        'images',
        'descriptions',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'titre',
        'images',
        'descriptions',
        'status',
        'date_add',
        'date_upd',
    )


class FootAdmin(admin.ModelAdmin):

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


class Foot_LiensAdmin(admin.ModelAdmin):

    list_display = ('id', 'foot', 'lien', 'status', 'date_add', 'date_upd')
    list_filter = (
        'foot',
        'status',
        'date_add',
        'date_upd',
        'id',
        'foot',
        'lien',
        'status',
        'date_add',
        'date_upd',
    )


class GetFootAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titre',
        'images',
        'description',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'titre',
        'images',
        'description',
        'status',
        'date_add',
        'date_upd',
    )


class SectionAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'section',
        'titre',
        'sous_titre',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'section',
        'titre',
        'sous_titre',
        'status',
        'date_add',
        'date_upd',
    )


class MenuAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom',
        'titre',
        'descriptions',
        'images',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'nom',
        'titre',
        'descriptions',
        'images',
        'status',
        'date_add',
        'date_upd',
    )


class CartAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titre',
        'descriptions',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'titre',
        'descriptions',
        'status',
        'date_add',
        'date_upd',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Social, SocialAdmin)
_register(models.DetailEntreprise, DetailEntrepriseAdmin)
_register(models.Foot, FootAdmin)
_register(models.Foot_Liens, Foot_LiensAdmin)
_register(models.GetFoot, GetFootAdmin)
_register(models.Section, SectionAdmin)
_register(models.Menu, MenuAdmin)
_register(models.Cart, CartAdmin)
