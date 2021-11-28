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

class ArtWork(models.Model):
    artwork_title = models.CharField(max_length=100, null=True, blank=True)
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
    artwork_auction = models.CharField(max_length=32, null=True, blank=True)
    artwork_price = models.IntegerField(null=True, blank=True)
    artwork_price_ho = models.FloatField(null=True, blank=True)
    artwork_year = models.CharField(max_length=32, null=True, blank=True)
    artwork_trade_date = models.DateField(null=True, blank=True)
    artwork_genre = models.CharField(max_length=32, null=True, blank=True)
    artwork_material = models.CharField(max_length=32, null=True, blank=True)
    artwork_size_width = models.CharField(max_length=32, null=True, blank=True)
    artwork_size_height = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.artwork_title


class ArtistCommentsForm:
    pass


class ArtistComments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Artist, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)