from django.urls import path
from artikel_kesehatan.views import show_artikel, tambah_artikel

app_name = 'artikel_kesehatan'

urlpatterns = [
    path('', show_artikel, name='show_artikel'),
    path('tambah-artikel/', tambah_artikel, name='tambah_artikel'),
]