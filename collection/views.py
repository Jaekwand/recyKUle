from django.shortcuts import render, get_object_or_404, redirect
from collection.models import CollectionPost, CollectionAnswer
from collection.forms import CollectionPostForm, CollectionAnswerForm
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def collection_list(request):
    """
    컬렉션 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1') # 페이지

    # 조회
    collection_list = CollectionPost.objects.order_by('-create_date')

    # 페이징 처리
    paginator = Paginator(collection_list, 10) # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'collection_list': page_obj}
    return render(request, 'collection/collection-main.html', context)


def collection_list_detail(request, collection_id):
    """
    컬렉션 목록 출력
    """
    collection_detail = get_object_or_404(CollectionPost, pk=collection_id)
    context = {'collection_detail': collection_detail}
    return render(request, 'collection/collection-detail.html', context)


@login_required(login_url='common:login')
def collection_answer_create(request, collection_id):
    """
    게시판 답변 등록
    """
    post = get_object_or_404(CollectionPost, pk=collection_id)
    if request.method == "POST":
        print(request.POST.keys())
        form = CollectionAnswerForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user # author 속성에 로그인 계정 저장
            answer.create_date = timezone.now()
            answer.post = post
            answer.save()
            return redirect('collection:detail', collection_id=post.id)
    else:
        form = CollectionAnswerForm()
    context = {'post': post, 'form': form}
    return render(request, 'collection/collection-detail.html', context)

@login_required(login_url='common:login')
def collection_create(request):
    """
    컬렉션 등록
    """
    if request.method == 'POST':
        form = CollectionPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user # author 속성에 로그인 계정 저장
            post.create_date = timezone.now()
            if request.FILES.get("image"):
                post.head_image = request.FILES.get("image")
            post.save()
            return redirect('collection:main')
    else:
        form = CollectionPostForm()
    context = {'form': form}
    return render(request, 'collection/collection-upload.html', context)

@login_required(login_url = 'common:login')
def collection_modify(request, collection_id):
    """
    컬렉션 수정
    """
    post = get_object_or_404(CollectionPost, pk=collection_id)
    if request.user != post.author:
        messages.error(request, "수정권한이 없습니다")
        return redirect('collection:detail', collection_id=post.id)

    if request.method == "POST":
        form = CollectionPostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.modify_date = timezone.now()
            post.save()
            return redirect('collection:detail', collection_id=post.id)
    else:
        form = CollectionPostForm(instance=post)
    context = {'form': form}
    return render(request, 'collection/collection-upload.html', context)

@login_required(login_url = 'common:login')
def collection_delete(request, collection_id):
    """
    컬렉션 삭제
    """
    post = get_object_or_404(CollectionPost, pk=collection_id)
    post.delete()
    return redirect('collection:main')


