from django.urls import path
from diarybund.views import show_diarybund
from diarybund.views import show_json
from diarybund.views import create_diary_ajax
from diarybund.views import delete_ajax
from diarybund.views import edit_diary_ajax
from diarybund.views import show_json_flutter
from diarybund.views import delete_ajax_flutter
from diarybund.views import create_diary_ajax_flutter

app_name = 'diarybund'

urlpatterns = [
    path('', show_diarybund, name='show_diarybund'),
    path('delete/<int:id>', delete_ajax, name='delete_ajax'),
    path('json/', show_json, name='show_json'),
    path('create-ajax/', create_diary_ajax, name='create_task_ajax'),
    path('edit/<int:id>', edit_diary_ajax, name='edit_diary_ajax'),
    path('json-flutter/<str:current_username>', show_json_flutter, name='show_json_flutter'),
    path('delete-flutter/<int:id>', delete_ajax_flutter, name='delete_ajax_flutter'),
    path('create-ajax-flutter/', create_diary_ajax_flutter, name='create_diary_ajax_flutter'),
]