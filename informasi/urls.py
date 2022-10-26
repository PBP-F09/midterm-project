from django.urls import path
from informasi.views import *

app_name = 'informasi'

urlpatterns = [
    path('', show_informasi, name='show_informasi'),
]