from .models import Note
from django import forms

class NoteForm(forms.ModelForm):
    lokasi = forms.CharField(widget=forms.TextInput())
    tanggal = forms.CharField(widget=forms.TextInput())
    waktu = forms.CharField(widget=forms.TextInput())
    kapasitas_balita = forms.IntegerField(widget=forms.NumberInput())

    class Meta:
        model = Note
        fields = ('lokasi', 'tanggal', 'waktu', 'kapasitas_balita')