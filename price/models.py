from django.db import models
from django.contrib.auth.models import User

class Artist(models.Model):
    name = models.CharField(max_length=32)
    image = models.ImageField()
    def __str__(self):
        return self.name

class ArtWork(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    art_image = models.ImageField()
    price = models.IntegerField()
    trade_date = models.DateField()
    material = models.CharField(max_length=32)
    size_width = models.CharField(max_length=32)
    size_height = models.CharField(max_length=32)
    def __str__(self):
        return self.title