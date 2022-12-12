from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from login.decorators import allowed_users
from .models import Note
from .forms import NoteForm
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404  
from django.contrib import messages
from django.utils.dateparse import parse_date
import datetime



def show_json(request):
    data = Note.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@allowed_users(allowed_roles=['faskes'], path='/periksa/main')
def index(request):
   # create object of note
   user_type = 'non_login'

   if request.user.is_authenticated:
      user_type = request.user.groups.all()[0].name

   form = NoteForm()
   if request.method == "PUT" :
      form = NoteForm(request.POST or None, request.FILES or None)
      user = request.user
      
      # check if form data is valid

      if form.is_valid():
         # save the form data to model
         instance = form.save()
         return JsonResponse({
            'lokasi': instance.lokasi,
            'tanggal': instance.tanggal,
            'waktu': instance.waktu,
            'kapasitas_balita': instance.kapasitas_balita
         })
         
   context = {
      'form': form,
      "user_type" : user_type,
      "username":request.user,
   }
   return render(request, "notes_page.html", context)


def getJsonNote(request):
   note = Note.objects.all()
   note = note.values()
   data = list(note)
   return JsonResponse({
      "data": data
   })

@csrf_exempt
def postJsonNote(request) :
   if request.method == "POST" :
      username = request.POST.get('username')
      lokasi = request.POST.get('lokasi')
      tanggal = request.POST.get('tanggal')
      waktu = request.POST.get('waktu')
      kapasitas_balita = request.POST.get('kapasitas_balita')

      user = User.objects.get(username=username)
      tanggal = datetime.datetime.strptime(tanggal, "%d-%m-%Y")

      note = Note.objects.create(
         user = user,
         lokasi = lokasi,
         tanggal = tanggal,
         waktu = waktu,
         kapasitas_balita = int(kapasitas_balita)
      )
      note.save()
      return JsonResponse({
         "message" : "succes"
      })


@csrf_exempt
def delete_info(request, pk):
   Note.objects.filter(pk=pk).delete()
   return JsonResponse({'message': 'success'})


@allowed_users(allowed_roles=['faskes'], path='/periksa/main')
def index1(request):
   # create object of note
   user_type = ''

   if request.user.is_authenticated:
      user_type = request.user.groups.all()[0].name

   form = NoteForm()
   if request.method == "PUT" :
      form = NoteForm(request.POST or None, request.FILES or None)
      user = request.user
      
      # check if form data is valid

      if form.is_valid():
         # save the form data to model
         instance = form.save()
         return JsonResponse({
            'lokasi': instance.lokasi,
            'tanggal': instance.tanggal,
            'waktu': instance.waktu,
            'kapasitas_balita': instance.kapasitas_balita
         })

   result = {

      'lokasi': instance.lokasi,
      'tanggal': instance.tanggal,
      'waktu': instance.waktu,
      'kapasitas_balita': instance.kapasitas_balita,
      'form': form,
      "user_type" : user_type,
      "username":request.user,
      
   }
   return JsonResponse(result)

def viewInformasi(request):
   # create object of note
   form = NoteForm(request.POST or None, request.FILES or None)
   user_type = 'non_login'
   if request.user.is_authenticated:
        user_type = request.user.groups.all()[0].name
   user = request.user
        
   context = {
      'form': form,
      "user_type" : user_type,
      "username" : request.user,
   }
   return render(request, "view_informasi.html", context)

@csrf_exempt
def ajax_add(request):
    if request.method == "POST":
        lokasi = request.POST.get("lokasi")
        tanggal = request.POST.get("tanggal")
        waktu = request.POST.get("waktu")
        kapasitas_balita = request.POST.get("kapasitas_balita")
        user = request.user

        Note.objects.create(lokasi=lokasi, tanggal=tanggal, user=user, waktu=waktu, kapasitas_balita=kapasitas_balita)
        return HttpResponse()
    else:
        print("here")
        return redirect("informasi:index")

@csrf_exempt
def delete_ajax(request, id):
   Note.objects.filter(id=id).delete()
   return redirect("informasi:index")

@csrf_exempt
def editInfos(request, id):
   if(request.method == 'POST') :
      infos = Note.objects.get(pk = id) 

      infos.lokasi = request.POST.get('lokasi')
      infos.tanggal = request.POST.get('tanggal')
      infos.waktu = request.POST.get("waktu")
      infos.kapasitas_balita = request.POST.get('kapasitas_balita')
      infos.user = request.user
      infos.save()

      result = {
            'fields':{
               'lokasi':infos.lokasi,
               'tanggal':infos.tanggal,
               'waktu':infos.waktu,
               'kapasitas_balita':infos.kapasitas_balita,
               'user': request.user,
               
            },
            'pk':infos.pk
      }
   return HttpResponse(200)  










