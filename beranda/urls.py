from django.urls import path
from beranda.views import *

app_name = 'beranda'

urlpatterns = [
    path('', show_beranda, name='show_beranda')
]