from django.shortcuts import render

# Create your views here.
def show_beranda(request):
    return render(request, 'beranda.html')