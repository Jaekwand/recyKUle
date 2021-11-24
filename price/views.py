from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from price.models import ArtWork, Artist

import json


def price_main(request):
    artworks = ArtWork.objects.all()
    context = {
        "artworks": artworks

    }
    return render(request, "price/price-main.html", context)


def price_artist(request):
    return render(request, "price/price-artist.html")


def search_artwork(request):
    request_body = json.loads(request.body)

    data = {
        "payload": [
        ]
    }

    keyword = request_body.get("keyword")
    artist_list = Artist.objects.filter(name__contains=keyword)

    # {"payload": [{"artist": "정승연", "recent_selling": 10000000}]}
    for artist in artist_list:
        expensive_artwork = None
        if artist.artworks.count() > 0:
            expensive_artwork = artist.artworks.order_by("-price")[0]

        data["payload"].append({
            "artist_name": artist.artist_namename,
            "expensive_artwork_title": getattr(expensive_artwork, 'title', 'xxxx'),
            "expensive_artwork_price": getattr(expensive_artwork, 'price', 0),
        })

    return JsonResponse(data, json_dumps_params={"ensure_ascii": False},)
