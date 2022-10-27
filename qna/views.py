from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from qna.models import Answer, Question
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from qna.forms import *
import datetime

# Create your views here.
def show_qna(request):
    context = {'form':QuestionForm()}
    return render(request, 'qna.html', context)

def json_qna(request):
    questions = Question.objects.all()
    return HttpResponse(serializers.serialize("json", questions), content_type="application/json")

@csrf_exempt
def create_question(request):
    question = QuestionForm()

    if request.method == "POST":
        question = QuestionForm(request.POST)
        if question.is_valid():
            text = question.cleaned_data['text']

            new_question = Question.objects.create(text=text, is_answered=False, user=request.user, date=datetime.date.today())
            new_question.save()

            result = {
                'fields':{
                    'text':new_question.text,
                    'is_answered':new_question.is_answered,
                    'date':new_question.date,
                    'user':new_question.user.username,
                },
                'pk':new_question.pk
            }

            return JsonResponse(result)

@csrf_exempt
def create_answer(request, id):
    answer = AnswerForm()

    if request.method == "POST":
        answer = AnswerForm(request.POST)
        if answer.is_valid():
            text = answer.cleaned_data['text']

            question = get_object_or_404(Question, id = id)

            new_answer = Answer.objects.create(text=text, question=question, user=request.user, date=datetime.date.today())
            new_answer.save()

            result = {
                'fields':{
                    'text':new_answer.text,
                    'question_id':id,
                    'date':new_answer.date,
                    'user':new_answer.user.username,
                },
                'pk':new_answer.pk
            }

            return JsonResponse(result)