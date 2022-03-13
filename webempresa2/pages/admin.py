from django.contrib import admin
from .models import Page

# Register your models here.

class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'order')

# Activamos en el admin.site.register el modelo Link, con el Admin de pruebas: PageAdmin
admin.site.register(Page, PageAdmin)
