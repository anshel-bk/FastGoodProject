from django.contrib import admin

# Register your models here.
from .models import *
#и зарегистрируем модель в админке:

admin.site.register(Shaurma_Food)