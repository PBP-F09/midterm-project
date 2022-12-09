from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from artikel_kesehatan.models import Artikel
from django.contrib.auth.decorators import login_required
from login.decorators import allowed_users
from artikel_kesehatan.forms import TambahArtikelForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def show_artikel(request):
    try:
        user_type = request.user.groups.all()[0].name
    except:
        user_type = 'non_logged_in'
    form = TambahArtikelForm()
    context = {
        'user': request.user,
        'user_type': user_type,
        'form': form,
        'last_login': request.COOKIES.get('last_login'),
    }
    return render(request, 'artikel.html', context)

@csrf_exempt
@allowed_users(allowed_roles=['admin'])
def tambah_artikel(request):
    if request.method == 'POST':
        judul = request.POST.get('judul')
        isi = request.POST.get('isi')
        author = request.user
        new_artikel = Artikel(judul=judul, isi=isi, author=author)
        new_artikel.save()
        result = {
            'pk': new_artikel.pk,
            'fields': {
                'judul': judul,
                'isi': isi,
                'tanggal': new_artikel.tanggal,
                'author': request.user.id,
            }
        }
        return JsonResponse(result)
#         return redirect('artikel_kesehatan:show_artikel')
#     return render(request, 'artikel.html')

def show_artikel_json_by_id(request, id):
    artikel = Artikel.objects.get(pk=id)
    return HttpResponse(serializers.serialize('json', [artikel]), content_type='application/json')

def show_artikel_by_id(request, id):
    artikel = Artikel.objects.get(pk=id)
    context = {
        'artikel': artikel
    }
    return render(request, 'artikel_by_id.html', context)

def show_artikel_json(request):
    artikel = Artikel.objects.all()
    return HttpResponse(serializers.serialize('json', artikel), content_type='application/json')

def hapus_artikel(request, id):
    artikel = Artikel.objects.get(pk=id)
    artikel.delete()
    return HttpResponse(status=202)
