from unicodedata import name
from django.urls import path
from qna.views import *

app_name = 'qna'

urlpatterns = [
    path('', show_qna, name='show_qna'),
    path('add/', create_question, name='create_question'),
    path('json/', json_qna, name='json_qna'),
    path('answer/<int:id>', create_answer, name='create_answer'),
]