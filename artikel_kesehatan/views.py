from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_artikel(request):
    return render(request, 'artikel.html')