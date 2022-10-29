from django import forms

class QuestionForm(forms.Form):
    text = forms.CharField(
        label='text',
        widget= forms.Textarea (
            attrs={
                'class':'block p-4 w-full text-gray-900 bg-cream-muda rounded-lg border border-merah-muda sm:text-md focus:ring-merah-muda focus:border-merah-muda form-control px-3 py-1.5 text-base font-normal bg-clip-padding border-solid transition ease-in-out m-0 focus:text-gray-700 focus:bg-white',
                'id':'text',
                'rows':'5',
                'placeholder':'Ingin bertanya apa?',
    }))

class AnswerForm(forms.Form):
    text = forms.CharField(
        label='text',
        widget= forms.TextInput(
            attrs={
                'class':'form-control bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2 my-3',
                   'type':'text',
                   'name':'title',
                   'placeholder':'Tulis komentar...',
                   'id': 'input-answer-${data.pk}'
    }))

                                               