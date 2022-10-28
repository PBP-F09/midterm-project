from django import forms

class QuestionForm(forms.Form):
    text = forms.CharField(label='text')

class AnswerForm(forms.Form):
    text = forms.CharField(label='text')