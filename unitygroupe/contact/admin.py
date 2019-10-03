from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class ContactAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom',
        'prenom',
        'email',
        'tel',
        'message',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'date_add',
        'date_upd',
        'id',
        'nom',
        'prenom',
        'email',
        'tel',
        'message',
        'date_add',
        'date_upd',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Contact, ContactAdmin)
