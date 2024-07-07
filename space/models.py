from django.db import models

# Create your models here.

class Planet(models.Model):
    name = models.CharField(max_length=50)
    size = models.PositiveBigIntegerField()
    def __str__(self):
        return self.name
    
    
class Satellite(models.Model):
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    size = models.PositiveBigIntegerField()
    def __str__(self):
        return self.name