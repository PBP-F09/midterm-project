from django import forms
from catatbund.models import CatatbundModel
from django.utils.translation import gettext_lazy as _

# class TambahCatatanForm(forms.Form):
#     weight  = forms.FloatField(required=True)
#     height  = forms.FloatField(required=True)

# creating a form
class TambahCatatanForm(forms.ModelForm):
    class Meta:
        model = CatatbundModel
        fields = [
            "weight",
            "height",
        ]   
        widgets = {
            'weight': forms.TextInput(attrs={
                'required': True, 
                'label':'weight',
                'name':"weight",
                'min':0,
                'id':"weight",
                'class':"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white",
                'placeholder':"Berat Badan(kg)"
            }),
            'height': forms.TextInput(attrs={
                'required': True,
                'label':'height',
                'name':"height",
                'id':"height",
                'min':0,
                'placeholder':"Tinggi Badan(m)",
                'class':"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"			
            }),
        }

        error_messages = {
            'weight': {
                'required': _("Field cannot be empty"),
            },
            'height': {
                'required': _("Field cannot be empty"),
            }
        }