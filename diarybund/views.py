from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from diarybund.models import DiaryBund
import datetime
from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
# @login_required(login_url='/todolist/login/')
@csrf_exempt
def create_diary_ajax(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        abstract = request.POST.get('abstract')
        emotion = request.POST.get('emotion')
        if title != "" or description != "" or abstract != "" or emotion != "":
            diary = DiaryBund.objects.create(title = title, abstract = abstract, description = description, emotion = emotion, date = datetime.datetime.now(), user = request.user)
            context = {
                'pk' : diary.pk,
                'fields' : {
                    'title' : diary.title,
                    'description' : diary.description,
                    'emotion' : diary.emotion,
                    'date' : diary.date
                }
            }
            return JsonResponse(context)
        
# @login_required(login_url='/todolist/login/')
@csrf_exempt
def delete_ajax(request, id):
    if (request.method == 'DELETE'):
        DiaryBund.objects.filter(id=id).delete()
        return HttpResponse(status=202)
    
def show_json(request):
    data_diary = DiaryBund.objects.all()
    # data_diary = DiaryBund.objects.filter(user = request.user) #sesuai sama user yang lagi login
    return HttpResponse(serializers.serialize("json", data_diary), content_type="application/json")

def show_diarybund(request):
    context = {}
    return render(request, 'diarybund.html', context)