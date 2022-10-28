from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from beranda.views import show_beranda

# Create your views here.
def registrasi_user(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            role_user = request.POST.get('role_user')
            new_group, created_group = Group.objects.get_or_create(name=role_user)
            if created_group:
                user.groups.add(created_group)
            else:
                user.groups.add(new_group)
            # print(f'===== {user}')
            # print(f'===== {role_user}')
            # print(f'===== {user.groups.all()}')
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
            # print(f'===== {user}')
            # print(f'===== {user.groups.all()}')
            return redirect('beranda:show_beranda')
    context = {}
    return render(request, 'login.html', context)

# @login_required(login_url='')
def logout_user(request):
    logout(request)
    return redirect('beranda:show_beranda')