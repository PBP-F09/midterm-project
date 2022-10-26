from django.shortcuts import render

# Create your views here.
def show_informasi(request):
    return render(request, 'informasi.html')
