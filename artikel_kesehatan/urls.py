from django.urls import path
from artikel_kesehatan.views import index

app_name = 'artikel_kesehatan'

urlpatterns = [
    path('', index, name='index'),
]