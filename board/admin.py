from django.contrib import admin

from board.models import BoardPost

# 관리자게시판에서 글을 검색할 수 있게 하는 기능
class BoardPostAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(BoardPost, BoardPostAdmin)
