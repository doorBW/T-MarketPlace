from django import forms
from .models import Market, Festival


class MarketForm(forms.ModelForm):
    class Meta:
        model = Market
        fields = ['user', 'url', 'content', 'photo', ]


class FestivalForm(forms.ModelForm):
    class Meta:
        model = Festival
        fields = ['name', 'market', 'url', 'content', 'photo', ]
