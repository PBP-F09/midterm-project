from unicodedata import name
from django.urls import path
from qna.views import *

app_name = 'qna'

urlpatterns = [
    path('', show_qna, name='show_qna'),
    path('add/', create_question, name='create_question'),
    path('json/', json_qna, name='json_qna'),
    path('json2/', json_answers, name='json_answers'),
    path('answer/<int:id>', create_answer, name='create_answer'),
    path('delete/<int:id>', delete_question, name='delete_question'),
    path('delete2/<int:id>', delete_answer, name='delete_answer'),
    path('like/<int:id>', like_question, name='like_question'),
]