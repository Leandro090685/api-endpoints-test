from django.db import models

# Create your models here.


class Registros(models.Model):
    city=models.CharField(max_length=128) 
    temperature = models.IntegerField()
    feels_like = models.IntegerField()
    humidity = models.IntegerField()

