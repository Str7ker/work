from django.shortcuts import render
from django.http import HttpResponse
from .models import Company

def index(request):
    return HttpResponse("<h1>Компания</h1>")


