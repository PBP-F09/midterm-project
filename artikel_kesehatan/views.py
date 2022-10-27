from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.core import serializers
from artikel_kesehatan.models import Artikel
from django.contrib.auth.decorators import login_required
from login.decorators import allowed_users

# Create your views here.
def show_artikel(request):
    return render(request, 'artikel.html')

@login_required(login_url='/login')
@allowed_users(allowed_roles=['admin', 'faskes'])
def tambah_artikel(request):
    if request.method == 'POST':
        judul = request.POST.get('judul')
        isi = request.POST.get('isi')
        author = request.user
        # print(f'====== {author.groups.all()}')
        # print(f"====== user allowed")
        # print(f"====== {judul}")
        # print(f"====== {isi}")
        # print(f"====== {author}")
        new_artikel = Artikel(judul=judul, isi=isi, author=author)
        new_artikel.save()
        return redirect('artikel_kesehatan:show_artikel')
    return render(request, 'artikel.html')

def show_artikel_by_id(request, id):
    artikel = Artikel.objects.get(pk=id)
    return HttpResponse(serializers.serialize('json', [artikel]), content_type='application/json')

def show_artikel_json(request):
    artikel = Artikel.objects.all()
    return HttpResponse(serializers.serialize('json', artikel), content_type='application/json')