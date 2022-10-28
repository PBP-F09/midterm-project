from django.urls import path
from catatbund.views import show_catatbund, show_json, add_catatan, register, login_user, logout_user, edit_catatan

app_name = 'catatbund'

urlpatterns = [
    path('', show_catatbund, name='show_catatbund'),
    path('json/', show_json, name='show_json'),
    path('add/', add_catatan, name='add_catatan'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit/', edit_catatan, name='edit_catatan'),
    # path('edit/', edit, name='edit'),
]