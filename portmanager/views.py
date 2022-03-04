from django.shortcuts import render
from multiprocessing import context

# Create your views here.

def home(request):
    return render(request, 'portmaganer/pages/home.html')
