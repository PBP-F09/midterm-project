from django.urls import path
from catatbund.views import *

app_name = 'catatbund'

urlpatterns = [
    path('', show_catatbund, name='show_catatbund'),
    path('json/', show_json, name='show_json'),
    path('add/', add_catatan, name='add_catatan'),
    path('edit/<int:id>', edit_catatan, name='edit_catatan'),
    path('json/<str:current_username>', show_json_flutter, name='show_json_flutter'),
    path('add_request_flutter/', add_request_flutter, name='add_request_flutter'),
    path('delete/<int:id>/', delete_catatans, name='delete_catatan'),
]