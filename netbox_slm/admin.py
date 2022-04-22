from django.contrib import admin
from netbox_slm.models import SoftwareProduct, SoftwareProductVersion


class SoftwareProductVersionInline(admin.TabularInline):
    model = SoftwareProductVersion
    fields = ('name',)
    extra = 0


@admin.register(SoftwareProduct)
class SoftwareProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = (SoftwareProductVersionInline,)
