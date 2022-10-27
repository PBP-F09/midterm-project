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
            try:
                group = Group.objects.get(name=role_user)
            except:
                # print(f'===== create {role_user} group')
                group = Group.objects.create(name=role_user)
            # print(f'===== {group} existed')
            user.groups.add(group)
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

@login_required(login_url='/login')
def logout_user(request):
    logout(request)
    return redirect('login:login_user')