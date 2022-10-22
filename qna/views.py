from django.shortcuts import render

# Create your views here.
def show_qna(request):
    return render(request, 'qna.html')