from django.db import models
from django.contrib.auth.models import User


class Artist(models.Model):
    artist_name = models.CharField(max_length=32)
    artist_image = models.ImageField(
        upload_to="artist/image/%Y/%m/%d/%H", null=True, blank=True)
    artist_image_url = models.URLField(
        default='',
        blank=True
    )

    def __str__(self):
        return self.artist_name


class ArtWork(models.Model):
    artwork_title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="artist_set")
    artwork_image = models.ImageField(
        upload_to="artwork/image/%Y/%m/%d/%H",
        null=True,
        blank=True
    )
    artwork_image_url = models.URLField(
        default='',
        blank=True
    )
    artwork_price = models.IntegerField()
    artwork_trade_date = models.DateField()
    artwork_material = models.CharField(max_length=32)
    artwork_size_width = models.CharField(max_length=32)
    artwork_size_height = models.CharField(max_length=32)

    def __str__(self):
        return self.artwork_title
