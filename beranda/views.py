from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def show_beranda(request):
    user_type = 'non_login'
    if request.user.is_authenticated:
        user_type = request.user.groups.all()[0].name
    return render(request, 'beranda.html', {'user_type':user_type})