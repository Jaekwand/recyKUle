from django.db import models
from django.contrib.auth.models import User


# 게시판에 글을 쓰는 기능
class CollectionPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    head_image = models.ImageField(
        upload_to="board/image/%Y/%m/%d/%H",
        blank=True,
        null=True)

    def __str__(self):
        return self.subject

# 게시판에 답변을 다는 기능
class CollectionAnswer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(CollectionPost, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

