from .models import Note
from django import forms
from django.forms.widgets import DateInput

class NoteForm(forms.ModelForm):
    lokasi = forms.CharField(help_text = "Enter your Name", widget=forms.TextInput())
    tanggal= forms.DateField(initial="2022-11-30", widget=DateInput(attrs={'type': 'date'}))
    waktu = forms.CharField(widget=forms.TextInput())
    kapasitas_balita = forms.IntegerField(widget=forms.NumberInput(), min_value = 0)

    class Meta:
        model = Note
        fields = ('lokasi', 'tanggal', 'waktu', 'kapasitas_balita')