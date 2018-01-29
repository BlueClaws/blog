from django.shortcuts import render
from django.http import HttpResponse
from .models import About
# Create your views here.

def index(request):
        a = About.objects.all()
        return render(request, 'about/index.html', {'a':a})
