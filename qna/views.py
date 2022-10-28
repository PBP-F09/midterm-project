from django.shortcuts import get_object_or_404, render
from qna.models import Answer, Question
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from qna.forms import *
from django.contrib.auth.models import User
import datetime

# Create your views here.
def show_qna(request):
    return render(request, 'qna.html')

def json_qna(request):
    questions = Question.objects.all()
    return HttpResponse(serializers.serialize("json", questions, use_natural_foreign_keys=True, use_natural_primary_keys=True), content_type="application/json")

def json_answers(request):
    answers = Answer.objects.all()
    return HttpResponse(serializers.serialize("json", answers, use_natural_foreign_keys=True, use_natural_primary_keys=True), content_type="application/json")

@csrf_exempt
def create_question(request):
    question = QuestionForm()

    if request.method == "POST":
        question = QuestionForm(request.POST)
        if question.is_valid():
            text = question.cleaned_data['text']

            user = get_object_or_404(User, id = request.user.id)

            new_question = Question.objects.create(text=text, is_answered=False, user=user, date=datetime.date.today())
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
            question.is_answered = True
            question.save()

            user = get_object_or_404(User, id = request.user.id)

            new_answer = Answer.objects.create(text=text, question=question, user=user, date=datetime.date.today())
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
    return HttpResponse(status=400)

@csrf_exempt
def delete_question(request, id):
    if request.method == "DELETE":
        question = get_object_or_404(Question, id = id)
        if request.user == question.user:
            question.delete()
            return HttpResponse(status=202)
    return HttpResponse(status=400)

@csrf_exempt
def delete_answer(request, id):
    if request.method == "DELETE":
        answer = get_object_or_404(Answer, id = id)
        if request.user == answer.user:
            answer.delete()
            return HttpResponse(status=202, content=answer.question.pk)
    return HttpResponse(status=400)