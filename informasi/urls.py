from django.urls import path
from .views import *

app_name = 'informasi'

urlpatterns = [
    path('', index, name='index'),
    

    path('data/', load_notes_view, name='notes-data'),

    path('json/', show_json, name='show_json'),
    path('delete/<int:id>', delete_ajax, name='delete_ajax'),

    path('ajax/submit/', ajax_add, name='ajax_add'),
]