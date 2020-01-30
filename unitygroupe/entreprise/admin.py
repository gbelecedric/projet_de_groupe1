from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titre',
        'description',
        'font',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'font',
        'status',
        'date_add',
        'date_upd',
        'id',
        'titre',
        'description',
        'font',
        'status',
        'date_add',
        'date_upd',
    )


class AddressAdmin(admin.ModelAdmin):

    list_display = ('id', 'address', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'address',
        'status',
        'date_add',
        'date_upd',
    )


class EntrepriseAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'email',
        'name',
        'phone',
        'logo',
        'description',
        'address',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'address',
        'status',
        'date_add',
        'date_upd',
        'id',
        'email',
        'name',
        'phone',
        'logo',
        'description',
        'address',
        'status',
        'date_add',
        'date_upd',
    )
    search_fields = ('name',)


class PersonnelAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'image',
        'job',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'job',
        'status',
        'date_add',
        'date_upd',
        'id',
        'name',
        'image',
        'job',
        'status',
        'date_add',
        'date_upd',
    )
    raw_id_fields = ('social',)
    search_fields = ('name',)


class FontAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'name',
        'status',
        'date_add',
        'date_upd',
    )
    search_fields = ('name',)


class JobAdmin(admin.ModelAdmin):

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


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Service, ServiceAdmin)
_register(models.Address, AddressAdmin)
_register(models.Entreprise, EntrepriseAdmin)
_register(models.Personnel, PersonnelAdmin)
_register(models.Font, FontAdmin)
_register(models.Job, JobAdmin)
