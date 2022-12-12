from django.shortcuts import render
from catatbund.models import CatatbundModel
from django.http import HttpResponse,JsonResponse
from django.core import serializers
import datetime
from django.views.decorators.csrf import csrf_exempt
from .forms import TambahCatatanForm

import json;
# sdfghjkm,.
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.urls import reverse
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponseBadRequest

from django.contrib.auth.decorators import login_required
from login.decorators import allowed_users

from django.shortcuts import get_object_or_404, redirect, render, reverse

# Create your views here.

@login_required(login_url='/login/')
def show_catatbund(request):
    model_catatbund = CatatbundModel.objects.filter(user = request.user)
    form = TambahCatatanForm()
    user_type = request.user.groups.all()[0].name
    context = {
    'data_catatbund': model_catatbund,
    'form' : form,
    'user_type' : user_type,
    }
    return render(request, "catatbund.html", context)

def show_json(request):
    model_catatbund = CatatbundModel.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", model_catatbund), content_type="application/json")

def show_json_flutter(request, current_username):
    list_of_data = []
    current_user = User.objects.filter(username = current_username)[0]
    model_catatbund = CatatbundModel.objects.filter(user = current_user)

    for catat in model_catatbund:
        list_of_data.append({
            'user' : catat.user.pk,
            'date' : catat.date,
            'weight' : catat.weight,
            'height' : catat.height,
            'bmi' : catat.bmi,
        })
    return JsonResponse(list_of_data,safe=False)

@csrf_exempt
def add_request_flutter(request):
    data = json.loads(request.body)
    username = data['username']
    thisUser = User.objects.filter(username=username)[0]
    weight = data['weight']
    height = data['height']
    catat = CatatbundModel.objects.create(weight = weight, height = height, date = datetime.date.today(), user = thisUser)
    print(catat)
    bmi = catat.count_bmi()
    catat.bmi = round(catat.count_bmi(),2)
    bmi = round(catat.bmi, 2)
    catat.save()
    result = {
        
        'weight':catat.weight,
        'height':catat.height,
        'bmi':bmi,
        'date':catat.date,      
        'pk':catat.pk
    }
    return JsonResponse(result)

@login_required(login_url='/login/')
@csrf_exempt
def add_catatan(request):
    if request.method == 'POST':
        form = TambahCatatanForm(request.POST)
        if form.is_valid() & (form.cleaned_data.get('weight') != 0) & (form.cleaned_data.get('height') != 0):
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
        return JsonResponse({'status':"error"})

@login_required(login_url='/login/')
@csrf_exempt
def edit_catatan(request, id):
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
        return JsonResponse({'status':"error"})

@login_required(login_url='/login/')
@csrf_exempt
def delete_catatans(request, id):
    if (request.method == 'DELETE'):
        CatatbundModel.objects.filter(id=id).delete()
        return HttpResponse(status=202)