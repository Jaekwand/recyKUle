from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from price.models import ArtWork


def price_main(request):
    arts = ArtWork.objects.all()
    context = {
        "arts": arts
    }
    return render(request, "price/price-main.html", context)



def price_artist(request):
    return render(request, "price/price-artist.html")


def search_artwork(request):
    keyword = request.POST.get("keyword")
    result_list = ArtWork.objects.filter(artist__name__contains=keyword)
    data = {
        "payload": [

        ]
    }

    for result in result_list:
        data["payload"].append({
            "title": result.title,
            "artist": result.artist.name,
            "art_image": result.art_image.url
        })

    return JsonResponse(data)
