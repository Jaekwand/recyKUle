from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from price.models import ArtWork, Artist

import json


def price_main(request):
    arts = ArtWork.objects.all()
    context = {
        "arts": arts
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
    result_list = Artist.objects.filter(name__contains=keyword)

    # {"payload": [{"artist": "정승연", "recent_selling": 10000000}]}
    for result in result_list:
        artworks_count = result.artworks.count()
        if artworks_count == 0:
            recent_sells = 0
        else:
            recent_sells = result.artworks.order_by("-price")[0].price

        data["payload"].append({
            "artist": result.name,
            "recent_selling": recent_sells
        })

    return JsonResponse(data, json_dumps_params={"ensure_ascii": False},)
