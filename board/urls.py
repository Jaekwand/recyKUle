from django.urls import path
from board import views

app_name = 'board'

urlpatterns = [
    path("", views.board, name='index'),
    path("list/", views.board_list, name='list'),
    path("list/<int:board_id>/", views.board_list_detail, name='detail'),
    path("answer/create/<int:board_id>/", views.answer_create, name='answer_create'),
    path("post/create/", views.post_create, name='post_create'),
    path("post/modify/<int:board_id>/", views.post_modify, name='post_modify'),

]
