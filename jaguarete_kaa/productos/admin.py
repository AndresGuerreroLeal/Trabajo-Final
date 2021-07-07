from django.contrib import admin
from .models import nuevo
# Register your models here.
class NuevoAdmin(admin.ModelAdmin):
    list_display = ('pk','nombre', 'categoria', )

admin.site.register(nuevo, NuevoAdmin)