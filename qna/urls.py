from django.urls import path
from qna.views import *

app_name = 'qna'

urlpatterns = [
    path('', show_qna, name='show_qna'),
]