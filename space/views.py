from django.shortcuts import *
from django.http import HttpResponse
from django.template import loader

from .models import Planet

def index(request):
    planets = Planet.objects.all()
    ctx = {
        "planets" : planets
    }
    return render(context=ctx, request=request, template_name="space/index.html")

def view_func(request):
    return HttpResponse('time has come...')

def details(request, id):
    planet = get_object_or_404(Planet, pk=id)
    return render(request, template_name='space/details.html', context={"planet":planet} )