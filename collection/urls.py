from django.urls import path
from collection import views

app_name = 'collection'

urlpatterns = [
    path("", views.collection_list, name='main'),
    path("detail/<int:collection_id>/", views.collection_list_detail, name='detail'),
    path("answer/create/<int:collection_id>/", views.collection_answer_create, name='answer_create'),
    path("create/", views.collection_create, name='create'),
    path("modify/<int:collection_id>/", views.collection_modify, name='modify'),
    path("delete/<int:collection_id>/", views.collection_delete, name='delete'),

]
