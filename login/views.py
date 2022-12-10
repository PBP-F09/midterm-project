from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from beranda.views import show_beranda
from django.views.decorators.csrf import csrf_exempt

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
            auth_login(request, user)
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

@csrf_exempt
def login_flutter(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Redirect to a success page.
            try:
                user_type = request.user.groups.all()[0].name
            except:
                user_type = 'non_logged_in'
            return JsonResponse({
            "status": True,
            "message": "Successfully Logged In!",
            # Insert any extra data if you want to pass data to Flutter
            "data":{
                "username":username,
                "role_user":user_type,
            }}, status=200)
        else:
            return JsonResponse({
            "status": False,
            "message": "Failed to Login, Account Disabled."
            }, status=401)

    else:
        return JsonResponse({
        "status": False,
        "message": "Failed to Login, check your email/password."
        }, status=401)

@csrf_exempt
def register_flutter(request):
    if (request.method == "POST"):
        username = request.POST.get("username")
        password = request.POST.get("password1")
        confirm_password = request.POST.get("password2")
        role_user = request.POST.get("role_user")
        if (User.objects.filter(username=username)):
            return JsonResponse({
                "status": False,
                "message": "Username atau email sudah pernah didaftarkan!"
                }, status=401)
        elif (password == confirm_password):
            user = User.objects.create_user(username=username, password=password)
            try:
                group = Group.objects.get(name=role_user)
            except:
                group = Group.objects.create(name=role_user)
            user.groups.add(group)
            user.save()
            return JsonResponse({
                "status": True,
                "message": "Successfully create account!"
                # Insert any extra data if you want to pass data to Flutter
                }, status=200)
        else:
            return JsonResponse({
            "status": False,
            "message": "Password dan Confirm Password tidak sama!"
            }, status=401)