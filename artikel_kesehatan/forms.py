
from django import forms
from artikel_kesehatan.models import Artikel

# creating a form
class TambahArtikelForm(forms.ModelForm):
    class Meta:
        model = Artikel
        fields = [
            "judul",
            "isi",
        ]   
        widgets = {
            'judul': forms.TextInput(attrs={
                'required': True,
                'type':"text",
                'name':"judul",
                'id':"judul",
                'class':"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white",
                'placeholder':"Title"
            }),
            'isi': forms.Textarea(attrs={
                'required': True,
                'name':"isi",
                'id':"isi",
                'placeholder':"Isi",
                'class':"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"			
            }),
        }

# class TambahArtikelForm(forms.Form):
#     judul = forms.CharField()
#     isi = forms.CharField(widget=forms.Textarea)