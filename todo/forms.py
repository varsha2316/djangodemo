from django import forms
from .models import Item


class Itemform(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'done']
