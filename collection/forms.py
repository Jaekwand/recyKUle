from django import forms
from collection.models import CollectionAnswer, CollectionPost


class CollectionPostForm(forms.ModelForm):
    class Meta:
        model = CollectionPost #사용할 모델
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '내용',
        }


class CollectionAnswerForm(forms.ModelForm):
    class Meta:
        model = CollectionAnswer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }


