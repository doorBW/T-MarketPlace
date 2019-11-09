from django import forms
from .models import Market, Festival


class MarketForm(forms.ModelForm):
    class Meta:
        model = Market
        fields = ['photo', ]


class FestivalForm(forms.ModelForm):
    class Meta:
        model = Festival
        fields = ['name', 'market', 'date', 'pay', 'host',
                  'address', 'url', 'content', 'photo', ]
