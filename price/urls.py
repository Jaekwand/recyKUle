from django.urls import path
from price import views


app_name = 'price'

urlpatterns = [
    path("", views.price_main, name='main'),
    path("artist/<int:artist_id>/", views.price_artist, name="artist"),
    # path("list/", views.board_list, name='list'),
    # path("list/<int:board_id>/", views.board_list_detail, name='detail'),
    # path("answer/create/<int:board_id>/", views.answer_create, name='answer_create'),
    # path("post/create/", views.post_create, name='post_create'),
    # path("post/modify/<int:board_id>/", views.post_modify, name='post_modify'),
    path("test", views.search_artwork)
]
