from django.contrib import admin

# Register your models here.
from .models import *
#и зарегистрируем модель в админке:


class ShaurmaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug','composition','photo','price','sizes','sauces')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Shaurma_Food,ShaurmaAdmin)
