from django.contrib import admin

from price.models import Artist, ArtWork, ArtistComments

admin.site.register(Artist)
admin.site.register(ArtWork)
admin.site.register(ArtistComments)

# 관리자게시판에서 글을 검색할 수 있게 하는 기능
# class Artist(admin.ModelAdmin):
#     search_fields = ['name']

