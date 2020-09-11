from django import forms
from .models import Monster
from django.db.models.fields import BLANK_CHOICE_DASH

class MonsterSearchForm(forms.Form):
    key_word = forms.CharField(
        label='モンスター名', required=False,
        widget=forms.TextInput(attrs={'class': 'input'})
    )
    race = forms.ChoiceField(
        label='', required=False,
        choices=BLANK_CHOICE_DASH + list(Monster.RACE),
    )
    
