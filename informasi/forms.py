from .models import Note
from django import forms
from django.forms.widgets import DateInput

class NoteForm(forms.ModelForm):
    lokasi = forms.CharField(widget=forms.TextInput())
    tanggal= forms.DateField(initial="2022-11-30", widget=DateInput(attrs={'type': 'date'}))
    waktu = forms.CharField(widget=forms.TextInput())
    kapasitas_balita = forms.IntegerField(widget=forms.NumberInput())


    class Meta:
        model = Note
        fields = ('lokasi', 'tanggal', 'waktu', 'kapasitas_balita')