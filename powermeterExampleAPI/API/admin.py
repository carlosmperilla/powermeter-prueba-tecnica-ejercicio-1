from django.contrib import admin

from .models import Medidor, Medicion

# Registro sencillo para los dos modelos base.
admin.site.register(Medidor)
admin.site.register(Medicion)