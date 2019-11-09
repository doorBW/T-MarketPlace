from django import forms
from .models import *


class MarketForm(forms.ModelForm):
    class Meta:
        model = Market
        fields = ['author', 'photo', 'content', ]

        help_text = {
            'author': '작성자',
            'photo': '사진 업로드',
            'content': '간단한 설명'
        }
