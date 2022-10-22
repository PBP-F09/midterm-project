from django.urls import path
from artikel_kesehatan.views import show_artikel

app_name = 'artikel_kesehatan'

urlpatterns = [
    path('', show_artikel, name='show_artikel'),
]