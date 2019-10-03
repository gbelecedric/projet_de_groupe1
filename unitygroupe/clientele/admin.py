# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class ClentAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom',
        'job',
        'image',
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
        'job',
        'image',
        'status',
        'date_add',
        'date_upd',
    )
    raw_id_fields = ('icon',)


class TestimonialAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'autor',
        'images',
        'descriptions',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'autor',
        'status',
        'date_add',
        'date_upd',
        'id',
        'autor',
        'images',
        'descriptions',
        'status',
        'date_add',
        'date_upd',
    )


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


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Clent, ClentAdmin)
_register(models.Testimonial, TestimonialAdmin)
_register(models.Social, SocialAdmin)
