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

# Create your views here.
@login_required(login_url='/login/')
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
                }
            }
            return JsonResponse(context)
        return JsonResponse({'error': True})

@login_required(login_url='/login/')
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
                }
            } 
            return JsonResponse(context)
        return JsonResponse({'error': True})
        
@login_required(login_url='/login/')
@csrf_exempt
def delete_ajax(request, id):
    if (request.method == 'DELETE'):
        DiaryBund.objects.filter(id=id).delete()
        return HttpResponse(status=202)

@login_required(login_url='/login/') 
def show_json(request):
    data_diary = DiaryBund.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", data_diary), content_type="application/json")

@login_required(login_url='/login/')
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