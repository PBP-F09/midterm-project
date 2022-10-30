from django.shortcuts import get_object_or_404, render
from login.decorators import allowed_users
from qna.models import Answer, Question
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from qna.forms import *
from django.contrib.auth.models import User
import datetime

# Create your views here.
# @login_required(login_url='/account/login')
# @allowed_users(allowed_roles=['admin', 'bumil', 'faskes'])
def show_qna(request):
    question_form = QuestionForm()
    answer_form = AnswerForm()
    user_type = 'non_login'
    if request.user.is_authenticated:
        user_type = request.user.groups.all()[0].name
    context = {
        "question_form":question_form,
        "answer_form":answer_form,
        "user_type":user_type,
        "username":request.user,
    }
    return render(request, 'qna.html', context)

def json_questions(request):
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

            if 'user_type' in request.session:
                role_user = request.session['user_type']

            new_question = Question.objects.create(text=text, is_answered=False, user=user, date=datetime.date.today(), role_user=role_user)
            new_question.save()

            result = {
                'fields':{
                    'text':new_question.text,
                    'is_answered':new_question.is_answered,
                    'date':new_question.date,
                    'user':new_question.user.username,
                    'total_like':new_question.total_like,
                    'total_answer':new_question.total_answer,
                    'role_user':new_question.role_user,
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
            question.total_answer += 1
            question.save()

            user = get_object_or_404(User, id = request.user.id)

            if 'user_type' in request.session:
                role_user = request.session['user_type']

            new_answer = Answer.objects.create(text=text, question=question, user=user, date=datetime.date.today(), role_user=role_user)
            new_answer.save()

            result = {
                'fields':{
                    'text':new_answer.text,
                    'question_id':id,
                    'date':new_answer.date,
                    'user':new_answer.user.username,
                    'total_answer':question.total_answer,
                    'role_user':new_answer.role_user,
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
            question = get_object_or_404(Question, id = answer.question.pk)
            question.total_answer -= 1
            question.save()
            answer.delete()
            result = {
                'id':question.pk,
                'total_answer':question.total_answer,
            }
            return JsonResponse(status=202, data=result)
    return HttpResponse(status=400)

@csrf_exempt
def like_question(request, id):
    if request.method == "PATCH":
        question = get_object_or_404(Question, id = id)
        question.total_like += 1
        question.save()
    
    result = {
        'total_like':question.total_like,
    }
        
    return JsonResponse(result)

