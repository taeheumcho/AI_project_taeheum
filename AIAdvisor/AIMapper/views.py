from django.shortcuts import render
from django.template.context_processors import request


# Create your views here.
def stockHome(request):
    return render(request, 'AIMapper/home.html')