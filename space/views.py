from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("index page")

def view_func(request):
    return HttpResponse('time has come...')