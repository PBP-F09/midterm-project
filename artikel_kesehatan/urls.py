from django.urls import path
from artikel_kesehatan.views import show_artikel, show_artikel_by_id, tambah_artikel, show_artikel_json

app_name = 'artikel_kesehatan'

urlpatterns = [
    path('', show_artikel, name='show_artikel'),
    path('<int:id>/', show_artikel_by_id, name='show_artikel_by_id'),
    path('tambah-artikel/', tambah_artikel, name='tambah_artikel'),
    path('json/', show_artikel_json, name='show_artikel_json'),
]