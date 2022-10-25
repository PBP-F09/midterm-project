from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.core import serializers
from artikel_kesehatan.models import Artikel

# Create your views here.
def show_artikel(request):
    return render(request, 'artikel.html')

def tambah_artikel(request):
    if request.method == 'POST':
        judul = request.POST.get('judul')
        isi = request.POST.get('isi')
        author = request.user
        # print(f"====== {judul}")
        # print(f"====== {isi}")
        # print(f"====== {author}")
        new_artikel = Artikel(judul=judul, isi=isi, author=author)
        new_artikel.save()
        return redirect('artikel_kesehatan:show_artikel')
    return render(request, 'artikel.html')

def show_artikel_json(requets):
    artikel = Artikel.objects.all()
    return HttpResponse(serializers.serialize('json', artikel), content_type='application/json')