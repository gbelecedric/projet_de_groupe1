from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class ReservationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'phone',
        'date_from',
        'date_to',
        'typeYatch',
        'email',
        'number',
        'note',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'date_from',
        'date_to',
        'typeYatch',
        'status',
        'date_add',
        'date_upd',
        'id',
        'name',
        'phone',
        'date_from',
        'date_to',
        'typeYatch',
        'email',
        'number',
        'note',
        'status',
        'date_add',
        'date_upd',
    )
    search_fields = ('name',)


class YatchAdmin(admin.ModelAdmin):

    list_display = ('id', 'nom', 'types', 'status', 'date_add', 'date_upd')
    list_filter = (
        'types',
        'status',
        'date_add',
        'date_upd',
        'id',
        'nom',
        'types',
        'status',
        'date_add',
        'date_upd',
    )


class TypeYatchAdmin(admin.ModelAdmin):

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


class DestinationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'pays_depart',
        'pays_arrive',
        'prix',
        'date_depart',
        'date_arrive',
        'description',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'pays_depart',
        'pays_arrive',
        'date_depart',
        'date_arrive',
        'status',
        'date_add',
        'date_upd',
        'id',
        'pays_depart',
        'pays_arrive',
        'prix',
        'date_depart',
        'date_arrive',
        'description',
        'status',
        'date_add',
        'date_upd',
    )


class PaysAdmin(admin.ModelAdmin):

    list_display = ('id', 'nom', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'nom',
        'status',
        'date_add',
        'date_upd',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Reservation, ReservationAdmin)
_register(models.Yatch, YatchAdmin)
_register(models.TypeYatch, TypeYatchAdmin)
_register(models.Destination, DestinationAdmin)
_register(models.Pays, PaysAdmin)
