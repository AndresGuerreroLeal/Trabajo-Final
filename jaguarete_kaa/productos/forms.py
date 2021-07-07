from django import forms
from django.db.models import fields
from django.db.models.fields import PositiveBigIntegerField


from .models import nuevo

class NuevoForm(forms.ModelForm):
    class Meta:

        model=nuevo
        fields=('nombre','categoria','imagen','descri','precio')
