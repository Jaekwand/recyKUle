from django import forms
from price.models import ArtistComments


class ArtistCommentsForm(forms.ModelForm):
    class Meta:
        model = ArtistComments
        fields = ['content']
        labels = {
            'content': '댓글',
        }
