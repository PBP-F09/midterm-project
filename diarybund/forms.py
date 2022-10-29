from django import forms
from diarybund.models import DiaryBund

# creating a form
class TambahDiaryForm(forms.ModelForm):
    class Meta:
        CHOICES= (
            (1,'Senang'),
            (2,'Biasa'),
            (3,'Sedih'),
            (4,'Marah'),
            )
        model = DiaryBund
        fields = [
            "title",
            "abstract",
            "description",
            "emotion",
        ]   
        widgets = {
            'title': forms.TextInput(attrs={
                'required': True,
                'type':"text",
                'name':"title",
                'id':"title",
                'class':"form-control",
                'placeholder':"Judul"
            }),
            'abstract': forms.TextInput(attrs={
                'required': True,
                'name':"abstract",
                'id':"abstract",
                'placeholder':"Deskripsi Singkat",
                'class':"form-control"			
            }),
            'description': forms.Textarea(attrs={
                'required': True,
                'type':"text",
                'name':"description",
                'id':"description",
                'class':"form-control",
                'placeholder':"Deskripsi"
            }),
        }
        error_messages = {
            'required':"Mohon isi informasi diary secara lengkap!"
        }