from django.shortcuts import render, get_object_or_404, redirect
# from board.models import BoardPost, BoardAnswer
# from board.forms import BoardPostForm, BoardAnswerForm
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def collection_main(request):
    return render(request, "collection/collection-main.html")

