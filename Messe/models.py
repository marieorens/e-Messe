from django.db import models

# Create your models here.

class Messe(models.Model):
    date = models.CharField(max_length=20)
    heure = models.CharField(max_length=60)
    intention = models.TextField()
    demandeur = models.TextField()
    Uid=models.CharField(max_length=50)

