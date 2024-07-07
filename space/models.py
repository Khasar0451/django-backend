from django.db import models

# Create your models here.

class Planet(models.Model):
    name = models.CharField(max_length=50)
    size = models.PositiveBigIntegerField()

class Satellite(models.Model):
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    size = models.PositiveBigIntegerField()
