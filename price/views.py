from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from price.models import ArtWork, Artist
from price.forms import ArtistCommentsForm
from django.utils import timezone
from django.core.paginator import Paginator



import json


def price_main(request):
    artworks = ArtWork.objects.all()
    context = {
        "artworks": artworks

    }
    return render(request, "price/price-main.html", context)


def price_artist(request, artist_id):
    artwork = get_object_or_404(ArtWork, pk=artist_id)
    artist = get_object_or_404(Artist, pk=artist_id)
    page = int(request.GET.get('p', 1)) #없으면 1로 지정

    #최근 거래 내역
    recent_trades = ArtWork.objects.order_by('-artwork_trade_date')
    paginator = Paginator(recent_trades, 3) #한 페이지 당 몇개 씩 보여줄 지 지정
    artworks = paginator.get_page(page)
    context = {
        "post": artwork,
        "artist": artist,
        # "recent_price": recent_trades,
        "recent_trades": artworks,

    }
    return render(request, "price/price-artist.html", context)


def artist_comments(request, artist_id):
    post = get_object_or_404(Artist, pk=artist_id)
    if request.method == "POST":
        print(request.POST.keys())
        form = ArtistCommentsForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.post = post
            answer.save()
            return redirect('price:artist', artist_id=post.id)
    else:
        form = ArtistCommentsForm()
        context = {'artist_id': artist_id, 'form': form}
    return render(request, "price/price-artist.html", context)


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
