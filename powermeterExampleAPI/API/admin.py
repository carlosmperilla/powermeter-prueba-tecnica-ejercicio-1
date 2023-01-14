from django.contrib import admin

from .models import Medidor, Medicion

# Register your models here.
admin.site.register(Medidor)
admin.site.register(Medicion)