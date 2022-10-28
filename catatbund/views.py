from django.shortcuts import render
from catatbund.models import CatatbundModel
from django.http import HttpResponse,JsonResponse
from django.core import serializers
import datetime
from django.views.decorators.csrf import csrf_exempt
from .forms import TambahCatatanForm

# sdfghjkm,.
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.urls import reverse
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponseBadRequest

from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404, redirect, render, reverse

# Create your views here.
@login_required(login_url='/catatbund/login/')
def show_catatbund(request):
    model_catatbund = CatatbundModel.objects.filter(user = request.user)
    form = TambahCatatanForm()
    context = {
    'data_catatbund': model_catatbund,
    'form' : form 
    }
    return render(request, "catatbund.html", context)

def show_json(request):
    model_catatbund = CatatbundModel.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", model_catatbund), content_type="application/json")

@csrf_exempt
def add_catatan(request):
    if request.method == 'POST':
        form = TambahCatatanForm(request.POST)
        print(form)
        if form.is_valid():
            weight = form.cleaned_data.get('weight')
            height = form.cleaned_data.get('height')
            catat = CatatbundModel.objects.create(weight = weight, height = height, date = datetime.date.today(), user = request.user)
            bmi = catat.count_bmi()
            catat.bmi = round(catat.count_bmi(),2)
            bmi = round(catat.bmi, 2)
            catat.save()
            result = {
                'fields':{
                    'weight':catat.weight,
                    'height':catat.height,
                    'bmi':bmi,
                    'date':catat.date
                    
                },
                'pk':catat.pk
            }
            return JsonResponse(result)
        return HttpResponseBadRequest()

@csrf_exempt
def edit_catatan(request, id):
    print("etst ")
    if request.method == 'POST':
        form = TambahCatatanForm(request.POST)
        if form.is_valid():
            weight = form.cleaned_data['weight']
            height = form.cleaned_data['height']
            catat = get_object_or_404(CatatbundModel, id = id)
            catat.weight=weight
            catat.height=height
            bmi = catat.count_bmi()
            catat.bmi = round(catat.count_bmi(),2)
            bmi = round(catat.bmi, 2)
            catat.save()
            result = {
                'fields':{
                    'weight':catat.weight,
                    'height':catat.height,
                    'bmi':bmi,
                    'date':catat.date
                },
                'pk':catat.pk
            }
            return JsonResponse(result)
        return HttpResponseBadRequest()

# wesdrfgthjkl
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('catatbund:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("catatbund:show_catatbund")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('catatbund:login'))
    response.delete_cookie('last_login')
    return response

# def edit(request):
#     pk = request.GET.get('pk')
#     object = get_object_or_404(CatatbundModel, pk = pk)
#     form = TambahCatatanForm(instance=object)
#     return render(request, 'edit.html', {
#         'object': object,
#         'pk': pk,
#         'form': form,
#         })