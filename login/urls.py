from django.urls import path
from login.views import *

app_name = 'login'

urlpatterns = [
    path('signup/', registrasi_user, name='registrasi_user'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
]