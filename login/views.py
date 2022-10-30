from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from beranda.views import show_beranda

# session and cookies
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def registrasi_user(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            role_user = request.POST.get('role_user')
            try:
                group = Group.objects.get(name=role_user)
            except:
                group = Group.objects.create(name=role_user)
            user.groups.add(group)
            return redirect('login:login_user')
    context = {'form': form}
    return render(request, 'registrasi.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse('beranda:show_beranda'))
            response.set_cookie('last_login', str(datetime.datetime.now()))

            try:
                user_type = request.user.groups.all()[0].name
            except:
                user_type = 'non_logged_in'
            request.session['user_type'] = user_type

            return response
            
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('beranda:show_beranda'))
    response.delete_cookie('last_login')
    return response