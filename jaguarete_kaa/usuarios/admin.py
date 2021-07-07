from django.contrib import admin
from .models import perfil
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
# Register your models here.

# admin.site.register(perfil)

@admin.register(perfil)
class ProfileAdmin(admin.ModelAdmin):

    list_display=('pk','user','phone_number','picture')
    # list_display_links=('pk','user','phone_number')

class ProfileInline(admin.StackedInline):
    model=perfil
    can_delete=False
    verbose_name_plural='perfiles'

class UserAdmin(BaseUserAdmin):
    inlines=(ProfileInline,)

admin.site.unregister(User)
admin.site.register(User,UserAdmin)