from socket import fromshare
from django import forms

from django.core.validators import MaxValueValidator, MinValueValidator

class TambahCatatanForm(forms.Form):
    weight  = forms.FloatField(required=True)
    height  = forms.FloatField(required=True)