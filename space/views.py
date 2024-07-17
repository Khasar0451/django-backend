from django.shortcuts import *
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.urls import reverse

from .models import Planet, Satellite

def index(request):
    # planets = Planet.objects.all()
    planets = get_list_or_404(Planet)

    ctx = {
        "planets" : planets
    }
    return render(context=ctx, request=request, template_name="space/index.html")

def view_func(request):
    return HttpResponse('time has come...')

def details(request, id):
    planet = get_object_or_404(Planet, pk=id)
    return render(request, template_name='space/details.html', context={"planet":planet} )

def addSatellite(request, id):
    planet = get_object_or_404(Planet, pk=id)

    name = request.POST["name"]
    radius = request.POST["radius"]
    satellite = Satellite( name=name, radius=radius, planet_id=id)
    satellite.save()
    print(Satellite.objects.all())
    print(Satellite.objects.all())

    # HttpResponseRedirect prevents data from being posted twice if a
    # user hits the Back button.
    # RequestContext for csrf
    return HttpResponseRedirect(reverse("space:details", args=(planet.id,)), RequestContext(request))