from django import forms
from board.models import BoardPost, BoardAnswer

class BoardPostForm(forms.ModelForm):
    class Meta:
        model = BoardPost #사용할 모델
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '내용',
        }

class BoardAnswerForm(forms.ModelForm):
    class Meta:
        model = BoardAnswer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }


