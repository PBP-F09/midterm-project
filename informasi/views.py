from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from login.decorators import allowed_users
from .models import Note
from .forms import NoteForm
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

def show_json(request):
    data = Note.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@allowed_users(allowed_roles=['faskes'], path='/periksa/main')
def index(request):
   # create object of note
   form = NoteForm(request.POST or None, request.FILES or None)
   
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
   }
   return render(request, "notes_page.html", context)

def viewInformasi(request):
   # create object of note
   form = NoteForm(request.POST or None, request.FILES or None)
        
   context = {
      'form': form,
   }
   return render(request, "view_informasi.html", context)

def load_notes_view(request):
# if request.is_ajax():
   notes = Note.objects.all()
   data = []
   for obj in notes:
      item = {
         'lokasi': obj.lokasi,
         'tanggal': obj.tanggal,
         'waktu': obj.waktu,
         'kapasitas_balita': obj.kapasitas_balita,
         'uploaded': obj.uploaded
      }
      data.append(item)
   return JsonResponse({'data':data})

@csrf_exempt
def ajax_add(request):
    if request.method == "POST":
        lokasi = request.POST.get("lokasi")
        tanggal = request.POST.get("tanggal")
        waktu = request.POST.get("waktu")
        kapasitas_balita = request.POST.get("kapasitas_balita")
        Note.objects.create(lokasi=lokasi, tanggal=tanggal, waktu=waktu, kapasitas_balita=kapasitas_balita)
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

   print("EDITINFOSSSS1")
   form = NoteForm(request.POST)
   
   if form.is_valid():
      print("EDITINFOSSSS3")
      infos = get_object_or_404(Note, id=id)

      infos.lokasi = form.cleaned_data['lokasi']
      infos.tanggal = form.cleaned_data['tanggal']
      infos.waktu = form.cleaned_data['waktu']
      infos.kapasitas_balita = form.cleaned_data['kapasitas_balita']
      infos.save()
      result = {
            'fields':{
               'lokasi':infos.lokasi,
               'tanggal':infos.tanggal,
               'waktu':infos.waktu,
               'kapasitas_balita':infos.kapasitas_balita
            },
            'pk':infos.pk
      }
      return redirect("informasi:index")
   return redirect("informasi:index")
      
