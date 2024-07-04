from django.shortcuts import render
from django.http import HttpResponse

def view_func(request):
    return HttpResponse('time has come...')