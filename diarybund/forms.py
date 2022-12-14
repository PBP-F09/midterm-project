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
                'label_tag':"Judul",
                'name':"Judul",
                'id':"title",
                'class':"form-control",
                'placeholder':"Judul"
            }),
            'abstract': forms.TextInput(attrs={
                'required': True,
                'label_tag':"Deskripsi Singkat",
                'name':"abstract",
                'id':"abstract",
                'placeholder':"Deskripsi Singkat",
                'class':"form-control"			
            }),
            'description': forms.Textarea(attrs={
                'required': True,
                'label_tag':"Deskripsi Lengkap",
                'name':"description",
                'id':"description",
                'class':"form-control",
                'placeholder':"Deskripsi"
            }),
            'emotion': forms.Select(attrs={
                'required': True,
                'label_tag':"Emosi Si Kecil",
                'name':"emotion",
                'id':"emotion",
                'placeholder':"Deskripsi Singkat",
                'class':"form-control"			
            }, choices=CHOICES),
        }