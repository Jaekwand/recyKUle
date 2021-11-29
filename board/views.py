from django.shortcuts import render, get_object_or_404, redirect
from board.models import BoardPost, BoardAnswer
from board.forms import BoardPostForm, BoardAnswerForm
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def board(request):
    return render(request, "board/board.html")


def board_list(request):
    """
    게시판 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1') # 페이지

    # 조회
    board_list = BoardPost.objects.order_by('-create_date')

    # 페이징 처리
    paginator = Paginator(board_list, 10) # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'board_list': page_obj}
    return render(request, 'board/board_list.html', context)


def board_list_cate1(request):
    """
    게시판 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1') # 페이지

    # 조회
    board_list = BoardPost.objects.filter(category__exact="자유롭게").order_by('-create_date')

    # 페이징 처리
    paginator = Paginator(board_list, 10) # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'board_list': page_obj}
    return render(request, 'board/board_cate1.html', context)


def board_list_cate2(request):
    """
    게시판 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1') # 페이지

    # 조회
    board_list = BoardPost.objects.filter(category__exact="전시소식").order_by('-create_date')

    # 페이징 처리
    paginator = Paginator(board_list, 10) # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'board_list': page_obj}
    return render(request, 'board/board_cate2.html', context)


def board_list_cate3(request):
    """
    게시판 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1') # 페이지

    # 조회
    board_list = BoardPost.objects.filter(category__exact="궁금해요").order_by('-create_date')

    # 페이징 처리
    paginator = Paginator(board_list, 10) # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'board_list': page_obj}
    return render(request, 'board/board_cate3.html', context)


def board_list_detail(request, board_id):
    """
    게시판 목록 출력
    """
    board_list_detail = get_object_or_404(BoardPost, pk=board_id)
    context = {'board_list_detail': board_list_detail}
    return render(request, 'board/board_list_detail.html', context)


# def answer_create(request, board_id):
#     '''
#     게시판 답변 등록
#     '''
#     board_list_detail = get_object_or_404(BoardPost, pk=board_id)
#     board_list_detail.boardanswer_set.create(content=request.POST.get('content'))
#     return redirect('board:detail', board_list_detail_id=board_list_detail.id)

@login_required(login_url='common:login')
def answer_create(request, board_id):
    """
    게시판 답변 등록
    """
    post = get_object_or_404(BoardPost, pk=board_id)
    if request.method == "POST":
        print(request.POST.keys())
        form = BoardAnswerForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user # author 속성에 로그인 계정 저장
            answer.create_date = timezone.now()
            answer.post = post
            answer.save()
            return redirect('board:detail', board_id=post.id)
    else:
        form = BoardAnswerForm()
    context = {'post': post, 'form': form}
    return render(request, 'board/board_list_detail.html)', context)

@login_required(login_url='common:login')
def post_create(request):
    """
    board 질문등록
    """
    if request.method == 'POST':
        form = BoardPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user # author 속성에 로그인 계정 저장
            post.create_date = timezone.now()
            post.category = request.POST["category"]
            if request.FILES.get("image"):
                post.head_image = request.FILES.get("image")
            post.save()
            return redirect('board:list')
    else:
        form = BoardPostForm()
    context = {'form': form}
    return render(request, 'board/post_form.html', context)

@login_required(login_url = 'common:login')
def post_modify(request, board_id):
    """
    board 질문수정
    """
    post = get_object_or_404(BoardPost, pk=board_id)
    if request.user != post.author:
        messages.error(request, "수정권한이 없습니다")
        return redirect('board:detail', board_id=post.id)

    if request.method == "POST":
        form = BoardPostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.modify_date = timezone.now()
            post.save()
            return redirect('board:detail', board_id=post.id)
    else:
        form = BoardPostForm(instance=post)
    context = {'form': form}
    return render(request, 'board/post_form.html', context)

@login_required(login_url = 'common:login')
def post_delete(request, board_id):
    """
    board 삭제
    """
    post = get_object_or_404(BoardPost, pk=board_id)
    post.delete()
    return redirect('board:list')


