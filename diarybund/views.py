import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from diarybund.models import DiaryBund
import datetime
from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers
from diarybund.forms import TambahDiaryForm
from login.decorators import allowed_users
from django.shortcuts import get_object_or_404
from django.core.serializers.json import DjangoJSONEncoder

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core import serializers
import datetime
from django.views.decorators.csrf import csrf_exempt

import json;
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404, render


# Create your views here.
@login_required(login_url='/account/login/')
@csrf_exempt
def create_diary_ajax(request):
    if request.method == 'POST':
        form = TambahDiaryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            abstract = form.cleaned_data.get('abstract')
            emotion = form.cleaned_data.get('emotion')
            diary = DiaryBund.objects.create(title = title, abstract = abstract, description = description, emotion = emotion, date = datetime.datetime.now(), user = request.user)
            diary.save()
            context = {
                'pk' : diary.pk,
                'fields' : {
                    'title' : diary.title,
                    'description' : diary.description,
                    'abstract' : diary.abstract,
                    'emotion' : diary.emotion,
                    'date' : diary.date,
                    'user' : diary.user.username,
                }
            }
            return JsonResponse(context)
        return JsonResponse({'error': True})

# @login_required(login_url='/account/login-flutter/')
@csrf_exempt
def create_diary_ajax_flutter(request):
    data = json.loads(request.body)
    username = data['username']
    thisUser = User.objects.filter(username=username)[0]
    title = data['title']
    description = data['description']
    abstract = data['abstract']
    emotion = data['emotion']
    diary = DiaryBund.objects.create(title = title, abstract = abstract, description = description, emotion = emotion, date = datetime.datetime.now(), user = thisUser)
    diary.save()
    context = {
                'pk' : diary.pk,
                'fields' : {
                    'title' : diary.title,
                    'description' : diary.description,
                    'abstract' : diary.abstract,
                    'emotion' : diary.emotion,
                    'date' : diary.date,
                    'user' : diary.user.username,
                }
            }
    return JsonResponse(context)

@login_required(login_url='/account/login/')
@csrf_exempt
def edit_diary_ajax(request, id):
    if request.method == 'POST':
        form = TambahDiaryForm(request.POST)
        if form.is_valid():
            diaryBaru = get_object_or_404(DiaryBund, id = id)
            diaryBaru.title = form.cleaned_data.get('title')
            diaryBaru.description = form.cleaned_data.get('description')
            diaryBaru.abstract = form.cleaned_data.get('abstract')
            diaryBaru.emotion = form.cleaned_data.get('emotion')
            diaryBaru.save()
            context = {
                'pk' : diaryBaru.pk,
                'fields' : {
                    'title' : diaryBaru.title,
                    'description' : diaryBaru.description,
                    'abstract' : diaryBaru.abstract,
                    'emotion' : diaryBaru.emotion,
                    'date' : diaryBaru.date,
                    'user' : diaryBaru.user.username,
                }
            } 
            return JsonResponse(context)
        return JsonResponse({'error': True})
        
@login_required(login_url='/account/login/')
@csrf_exempt
def delete_ajax(request, id):
    if (request.method == 'DELETE'):
        DiaryBund.objects.filter(id=id).delete()
        return HttpResponse(status=202)

# @login_required(login_url='/account/login-flutter/')
@csrf_exempt
def delete_ajax_flutter(request, id):
    if (request.method == 'DELETE'):
        DiaryBund.objects.filter(id=id).delete()
        return HttpResponse(status=202)

@login_required(login_url='/account/login/')
def show_json(request):
    data_diary = DiaryBund.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", data_diary), content_type="application/json")
 
# @login_required(login_url='/account/login-flutter/')   
@csrf_exempt
def show_json_flutter(request, current_username):
    list_of_data = []
    current_user = User.objects.filter(username = current_username)[0]
    model_diarybund = DiaryBund.objects.filter(user = current_user)

    for diary in model_diarybund:
        list_of_data.append({
            'pk' : diary.pk,
                'fields' : {
                    'title' : diary.title,
                    'description' : diary.description,
                    'abstract' : diary.abstract,
                    'emotion' : diary.emotion,
                    'date' : diary.date,
                    'user' : diary.user.username,
                }
        })
    return JsonResponse(list_of_data,safe=False)
    
@login_required(login_url='/account/login/')
def show_diarybund(request):
    modelDiary = DiaryBund.objects.filter(user = request.user)
    user_type = request.user.groups.all()[0].name
    form = TambahDiaryForm()
    context = {
        'data' : modelDiary,
        'form': form,
        'user_type' : user_type,
    }
    return render(request, 'diarybund.html', context)