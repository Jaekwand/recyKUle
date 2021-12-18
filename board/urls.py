from django.urls import path
from board import views

app_name = 'board'

urlpatterns = [
    path("", views.board, name='index'),
    path("list/", views.board_list, name='list'),
    path("list/cate1/", views.board_list_cate1, name='cate1'),
    path("list/cate2/", views.board_list_cate2, name='cate2'),
    # path("list/cate3/", views.board_list_cate3, name='cate3'),
    path("list/<int:board_id>/", views.board_list_detail, name='detail'),
    path("answer/create/<int:board_id>/", views.answer_create, name='answer_create'),
    path("post/create/", views.post_create, name='post_create'),
    path("post/modify/<int:board_id>/", views.post_modify, name='post_modify'),
    path("post/delete/<int:board_id>/", views.post_delete, name='post_delete'),

]
