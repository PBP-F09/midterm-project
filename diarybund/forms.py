from django import forms
from diarybund.models import DiaryBund
from django.core.exceptions import NON_FIELD_ERRORS

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
                'label_tag':"Judul",
                'name':"Judul",
                'id':"title",
                'class':"form-control",
                'placeholder':"Judul"
            }),
            'abstract': forms.TextInput(attrs={
                'required': True,
                'label_tag':"Judul",
                'name':"abstract",
                'id':"abstract",
                'placeholder':"Deskripsi Singkat",
                'class':"form-control"			
            }),
            'description': forms.Textarea(attrs={
                'required': True,
                'type':"text",
                'label_tag':"Judul",
                'name':"description",
                'id':"description",
                'class':"form-control",
                'placeholder':"Deskripsi"
            }),
            'emotion': forms.Select(attrs={
                'required': True,
                'label_tag':"Judul",
                'name':"emotion",
                'id':"emotion",
                'placeholder':"Deskripsi Singkat",
                'class':"form-control"			
            }, choices=CHOICES),
        }