from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from login.models import MyUser

# Create your views here.
def registrasi_user(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            role_user = request.POST.get('role_user')
            form.save()
            user = form.cleaned_data.get('username')
            user_role = MyUser.objects.get(user__username=user)
            if role_user == 'faskes':
                user_role.is_faskes = True
            elif role_user == 'bumil':
                user_role.is_bumil = True
            else:
                user_role.is_admin = True
            user_role.save()
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
            return redirect('/beranda')
    context = {}
    return render(request, 'login.html', context)

@login_required(login_url='/login')
def logout_user(request):
    logout(request)
    return redirect('login:login_user')