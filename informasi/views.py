from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

def show_json(request):
    data = Note.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def ajax_add(request):
    print(f'=========== ajax add')
    if request.method == "POST":
        lokasi = request.POST.get("lokasi")
        tanggal = request.POST.get("tanggal")
        waktu = request.POST.get("waktu")
        print(lokasi)
        print(tanggal)
        print(waktu)
        kapasitas_balita = request.POST.get("kapasitas_balita")
        Note.objects.create(lokasi=lokasi, tanggal=tanggal, waktu=waktu, kapasitas_balita=kapasitas_balita)
        return HttpResponse()
    else:
        print("here")
        return redirect("informasi:index")


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
def delete_ajax(request, id):
   print("========= delete ajax")
   #  if (request.method == 'DELETE'):
      #   print("========== inside if")
   Note.objects.filter(id=id).delete()
   return redirect("informasi:index")

def editInfos(request):
   infos = Note.objects.get(id=id)
   infos.kapasitas = request.POST['kapasitas']
   infos.isi = request.POST['isi']
   infos.save()

   return redirect("informasi:index")