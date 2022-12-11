from unicodedata import name
from django.urls import path
from qna.views import *

app_name = 'qna'

urlpatterns = [
    path('', show_qna, name='show_qna'),
    path('add/', create_question, name='create_question'),
    path('add-flutter/<role>/<int:id>', create_question_flutter, name='create_question_flutter'),
    path('json/', json_questions, name='json_questions'),
    path('json2/', json_answers, name='json_answers'),
    path('json2filter/<int:id>', json_answers_filter, name='json_answers_filter'),
    path('answer/<int:id>', create_answer, name='create_answer'),
    path('answer-flutter/<int:uid>/<role>/<int:qid>', create_answer_flutter, name='create_answer_flutter'),
    path('delete/<int:id>', delete_question, name='delete_question'),
    path('delete2/<int:id>', delete_answer, name='delete_answer'),
    path('delete2/<role>/<int:id>', delete_answer_flutter, name='delete_answer_flutter'),
    path('like/<int:id>', like_question, name='like_question'),
    path('like-flutter/<int:id>', like_question_flutter, name='like_question_flutter'),
]